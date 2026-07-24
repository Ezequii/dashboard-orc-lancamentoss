from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import json
R=Path(__file__).resolve().parents[1];O=R/'public/data';records=json.loads((O/'orcamentos.json').read_text(encoding='utf-8'));today=date.today()
def age(r):
 value=r.get('recebimento')if r.get('status')=='Falta lançamento'else r.get('lancamento')if r.get('status')=='Falta pedido'else r.get('dataPedido')
 try:return max(0,(today-datetime.strptime(value,'%Y-%m-%d').date()).days)
 except:return None
for r in records:r['diasParado']=age(r)if r.get('status')!='Concluído'else None
pending=[r for r in records if r.get('status')!='Concluído'];critical=[r for r in pending if(r.get('diasParado')or 0)>30]
suppliers={};leaders={}
for r in records:
 s=r.get('fornecedor')or'Não informado';suppliers.setdefault(s,{'name':s,'value':0,'count':0});suppliers[s]['value']+=r.get('valorTotal')or 0;suppliers[s]['count']+=1
for r in pending:
 l=r.get('solicitante')or'Não informado';leaders.setdefault(l,{'name':l,'value':0,'count':0});leaders[l]['value']+=r.get('valorTotal')or 0;leaders[l]['count']+=1
summary={'generatedAt':datetime.now(ZoneInfo('America/Cuiaba')).isoformat(timespec='seconds'),'services':len(records),'pending':len(pending),'critical':len(critical),'totalValue':sum(r.get('valorTotal')or 0 for r in records),'pendingValue':sum(r.get('valorTotal')or 0 for r in pending),'completionRate':round((len(records)-len(pending))/len(records)*100)if records else 0,'topSuppliers':sorted(suppliers.values(),key=lambda x:x['value'],reverse=True)[:10],'topLeaders':sorted(leaders.values(),key=lambda x:x['count'],reverse=True)[:10]}
(O/'executive-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(summary)
