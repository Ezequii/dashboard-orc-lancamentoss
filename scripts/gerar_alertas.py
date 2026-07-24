from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import json,os
R=Path(__file__).resolve().parents[1];O=R/'public/data';records=json.loads((O/'orcamentos.json').read_text(encoding='utf-8'));today=date.today();min_days=int(os.getenv('ALERT_MIN_DAYS','16'));critical=int(os.getenv('ALERT_CRITICAL_DAYS','30'));min_value=float(os.getenv('ALERT_MIN_VALUE','100000'))
def days(value):
 if not value:return None
 try:return max(0,(today-datetime.strptime(value,'%Y-%m-%d').date()).days)
 except:return None
items=[]
for r in records:
 if r.get('status')=='Concluído':continue
 base=r.get('recebimento')if r.get('status')=='Falta lançamento'else r.get('lancamento')if r.get('status')=='Falta pedido'else r.get('dataPedido')
 age=days(base);kind='critical'if age is not None and age>critical else'high-value'if (r.get('valorTotal')or 0)>=min_value else'attention'if age is not None and age>=min_days else None
 if kind:items.append({**r,'diasParado':age,'alertType':kind})
summary={'critical':sum(x['alertType']=='critical'for x in items),'attention':sum(x['alertType']=='attention'for x in items),'highValue':sum(x['alertType']=='high-value'for x in items),'total':len(items),'generatedAt':datetime.now(ZoneInfo('America/Cuiaba')).isoformat(timespec='seconds')}
(O/'alerts.json').write_text(json.dumps({'summary':summary,'items':items},ensure_ascii=False,indent=2),encoding='utf-8');print(summary)
