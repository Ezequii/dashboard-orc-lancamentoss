from pathlib import Path
from datetime import datetime, date
from zoneinfo import ZoneInfo
import json, math, sys
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'atualizar_dados' / 'CONTROLE_DE_REQUISICOES_2026.xlsx'
OUTPUT = ROOT / 'src' / 'data' / 'orcamentos.json'
META = ROOT / 'src' / 'data' / 'meta.json'
SHEET = 'Acompanhamento RC 2026'

if not INPUT.exists():
    raise SystemExit(f'ERRO: arquivo nao encontrado: {INPUT}')

wb = load_workbook(INPUT, data_only=True, read_only=True)
if SHEET not in wb.sheetnames:
    raise SystemExit(f'ERRO: aba obrigatoria nao encontrada: {SHEET}')
ws = wb[SHEET]

EXPECTED = [
    'DATA DE RECEBIMENTO DO ORÇAMENTO','DATA DE LANÇAMENTO DO ORÇAMENTO','PREFIXO',
    'EQUIPAMENTO','FORNECEDOR','Nº ORÇ. FINAL','VALOR SERVIÇO','VALOR PEÇAS',
    'VALOR TOTAL','SOLICITANTE','Nº DA ORDEM DE SERVIÇO','Nº REQUISIÇÃO',
    'Nº PEDIDO DE COMPRA','DATA PEDIDO','Nº NF/DANFE','DATA DE LANÇAMENTO DA NF',
    'STATUS','OBSERVAÇÕES ADICIONAIS'
]

def norm_text(v):
    return ' '.join(str(v or '').strip().upper().split())

header_row = None
for idx, row in enumerate(ws.iter_rows(min_row=1, max_row=20, values_only=True), start=1):
    vals = [norm_text(v) for v in row[:18]]
    if vals and ('DATA DE RECEBIMENTO' in vals[0] or vals[0] == norm_text(EXPECTED[0])):
        header_row = idx
        break
if header_row is None:
    raise SystemExit('ERRO: cabecalho da planilha nao foi localizado nas primeiras 20 linhas')

headers = [norm_text(ws.cell(header_row, c).value) for c in range(1, 19)]
required_positions = {4:'FORNECEDOR', 5:'ORÇ', 8:'VALOR TOTAL', 9:'SOLICITANTE', 16:'STATUS'}
for pos, key in required_positions.items():
    if key not in headers[pos]:
        raise SystemExit(f'ERRO: coluna obrigatoria inesperada na posicao {pos+1}: esperado {key}, encontrado {headers[pos]}')

def clean(v):
    if v in (None, '', '*', '-'): return None
    if isinstance(v, (datetime, date)): return v.strftime('%Y-%m-%d')
    if isinstance(v, float) and math.isnan(v): return None
    return v

def number(v):
    if v in (None, '', '*', '-'): return 0.0
    try: return float(v)
    except Exception: raise ValueError(f'valor numerico invalido: {v!r}')

def status(v):
    s = norm_text(v)
    mapping = {
        'CONCLUÍDO':'Concluído','CONCLUIDO':'Concluído','FALTA NF':'Falta NF',
        'FALTA O PEDIDO':'Falta pedido','FALTA PEDIDO':'Falta pedido',
        'FALTA LANÇAMENTO':'Falta lançamento','FALTA LANCAMENTO':'Falta lançamento'
    }
    return mapping.get(s, str(v or 'Não informado').strip())

records, errors = [], []
for excel_row, values in enumerate(ws.iter_rows(min_row=header_row+1, max_col=18, values_only=True), start=header_row+1):
    if not any(v not in (None, '') for v in values): continue
    # Ignora rodapes, totais e linhas auxiliares sem status.
    if not clean(values[16]): continue
    try:
        receb,lanc,prefixo,equip,forn,orc,serv,pecas,total,solic,osn,req,pedido,data_pedido,nf,data_nf,st,obs = values
        rec = {
            'id': excel_row-header_row,
            'recebimento': clean(receb), 'lancamento': clean(lanc),
            'prefixo': clean(prefixo), 'equipamento': clean(equip),
            'fornecedor': clean(forn), 'orcamento': clean(orc),
            'valorServico': number(serv), 'valorPecas': number(pecas),
            'valorTotal': number(total) if clean(total) is not None else number(serv)+number(pecas),
            'solicitante': clean(solic), 'ordemServico': clean(osn),
            'requisicao': clean(req), 'pedido': clean(pedido),
            'dataPedido': clean(data_pedido), 'nf': clean(nf), 'dataNF': clean(data_nf),
            'status': status(st), 'observacoes': clean(obs)
        }
        if not rec['fornecedor']: errors.append(f'linha {excel_row}: fornecedor vazio')
        records.append(rec)
    except Exception as e:
        errors.append(f'linha {excel_row}: {e}')

if not records: raise SystemExit('ERRO: nenhum registro valido foi encontrado')
if errors:
    print('\n'.join(errors[:30]), file=sys.stderr)
    raise SystemExit(f'ERRO: atualizacao cancelada; {len(errors)} inconsistencia(s) obrigatoria(s)')

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(records, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
now = datetime.now(ZoneInfo('America/Cuiaba'))
meta = {
    'atualizadoEm': now.isoformat(timespec='seconds'),
    'atualizadoEmTexto': now.strftime('%d/%m/%Y às %H:%M'),
    'arquivo': INPUT.name,
    'linhasProcessadas': len(records)
}
META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'OK: {len(records)} registros gerados em {OUTPUT}')
print(f'OK: ultima atualizacao {meta["atualizadoEmTexto"]}')
