from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import json
from openpyxl import load_workbook
R=Path(__file__).resolve().parents[1];src=R/'atualizar_dados/CONTROLE_DE_REQUISICOES_2026.xlsx';ws=load_workbook(src,data_only=True,read_only=True)['Acompanhamento RC 2026']
def c(v):
 if v in(None,'','*','-'):return None
 if isinstance(v,(datetime,date)):return v.strftime('%Y-%m-%d')
 return v
def n(v):
 try:return float(v or 0)
 except:return 0
def s(v):return {'CONCLUÍDO':'Concluído','CONCLUIDO':'Concluído','FALTA NF':'Falta NF','FALTA O PEDIDO':'Falta pedido','FALTA PEDIDO':'Falta pedido','FALTA LANÇAMENTO':'Falta lançamento','FALTA LANCAMENTO':'Falta lançamento'}.get(str(v or '').strip().upper(),str(v or 'Não informado').strip())
a=[]
for i,r in enumerate(ws.iter_rows(min_row=3,max_col=18,values_only=True),3):
 if not c(r[16]):continue
 x,y,p,e,f,o,vs,vp,vt,l,osn,req,ped,dp,nf,dnf,st,obs=r;a.append({'id':i-2,'recebimento':c(x),'lancamento':c(y),'prefixo':c(p),'equipamento':c(e),'fornecedor':c(f),'orcamento':c(o),'valorServico':n(vs),'valorPecas':n(vp),'valorTotal':n(vt) if c(vt)!=None else n(vs)+n(vp),'solicitante':c(l),'ordemServico':c(osn),'requisicao':c(req),'pedido':c(ped),'dataPedido':c(dp),'nf':c(nf),'dataNF':c(dnf),'status':s(st),'observacoes':c(obs)})
(R/'src/data/orcamentos.json').write_text(json.dumps(a,ensure_ascii=False,separators=(',',':')),encoding='utf-8');now=datetime.now(ZoneInfo('America/Cuiaba'));(R/'src/data/meta.json').write_text(json.dumps({'atualizadoEm':now.isoformat(timespec='seconds'),'atualizadoEmTexto':now.strftime('%d/%m/%Y às %H:%M'),'arquivo':src.name,'linhasProcessadas':len(a)},ensure_ascii=False,indent=2),encoding='utf-8');print(f'OK: {len(a)} registros')
