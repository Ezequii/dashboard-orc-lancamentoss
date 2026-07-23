from pathlib import Path
from datetime import datetime, date
from zoneinfo import ZoneInfo
import json
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "atualizar_dados" / "CONTROLE_DE_REQUISICOES_2026.xlsx"
SHEET = "Acompanhamento RC 2026"


def clean(value):
    if value in (None, "", "*", "-"):
        return None
    if isinstance(value, (datetime, date)):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, str):
        value = " ".join(value.replace("\u00a0", " ").split()).strip()
        return value or None
    return value


def number(value):
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def normalize_status(value):
    key = str(value or "").strip().upper()
    return {
        "CONCLUÍDO": "Concluído",
        "CONCLUIDO": "Concluído",
        "FALTA NF": "Falta NF",
        "FALTA O PEDIDO": "Falta pedido",
        "FALTA PEDIDO": "Falta pedido",
        "FALTA LANÇAMENTO": "Falta lançamento",
        "FALTA LANCAMENTO": "Falta lançamento",
    }.get(key, str(value or "Não informado").strip())


workbook = load_workbook(SOURCE, data_only=True, read_only=True)
worksheet = workbook[SHEET]
records = []
issues = []

for row_number, row in enumerate(
    worksheet.iter_rows(min_row=3, max_col=18, values_only=True), start=3
):
    if not clean(row[16]):
        continue
    (
        received, launched, prefix, equipment, supplier, budget,
        service_value, parts_value, total_value, requester,
        service_order, requisition, order, order_date, invoice,
        invoice_date, status, notes,
    ) = row
    record = {
        "id": row_number - 2,
        "recebimento": clean(received),
        "lancamento": clean(launched),
        "prefixo": clean(prefix),
        "equipamento": clean(equipment),
        "fornecedor": clean(supplier),
        "orcamento": clean(budget),
        "valorServico": number(service_value),
        "valorPecas": number(parts_value),
        "valorTotal": number(total_value) if clean(total_value) is not None else number(service_value) + number(parts_value),
        "solicitante": clean(requester),
        "ordemServico": clean(service_order),
        "requisicao": clean(requisition),
        "pedido": clean(order),
        "dataPedido": clean(order_date),
        "nf": clean(invoice),
        "dataNF": clean(invoice_date),
        "status": normalize_status(status),
        "observacoes": clean(notes),
    }
    if not record["fornecedor"]:
        issues.append(f"Linha {row_number}: fornecedor vazio")
    if record["valorTotal"] < 0:
        issues.append(f"Linha {row_number}: valor total negativo")
    records.append(record)

(ROOT / "src" / "data" / "orcamentos.json").write_text(
    json.dumps(records, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
)
now = datetime.now(ZoneInfo("America/Cuiaba"))
(ROOT / "src" / "data" / "meta.json").write_text(
    json.dumps(
        {
            "atualizadoEm": now.isoformat(timespec="seconds"),
            "atualizadoEmTexto": now.strftime("%d/%m/%Y às %H:%M"),
            "arquivo": SOURCE.name,
            "linhasProcessadas": len(records),
            "inconsistencias": len(issues),
            "origem": SOURCE.name,
        },
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)
print(f"OK: {len(records)} registros; {len(issues)} inconsistências")
