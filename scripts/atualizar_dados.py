from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import json
from openpyxl import load_workbook
R=Path(__file__).resolve().parents[1];F=R/'atualizar_dados/CONTROLE_DE_REQUISICOES_2026.xlsx';O=R/'public/data';O.mkdir(parents=True,exist_ok=True);W=load_workbook(F,data_only=True,read_only=True)['Acompanhamento RC 2026']
def c(v):
 if v in(None,'','*','-'):return None
 if isinstance(v,(datetime,date)):return v.strftime('%Y-%m-%d')
 if isinstance(v,str):return ' '.join(v.replace('\u00a0',' ').split()).strip() or None
 return v
def n(v):
 try:return float(v or 0)
 except:return 0.0
def d(v):
 v=c(v)
 if not v:return None
 for p in('%Y-%m-%d','%d/%m/%Y','%d.%m.%Y','%d-%m-%Y'):
  try:return datetime.strptime(v,p).strftime('%Y-%m-%d')
  except(ValueError,TypeError):pass
 return None
def st(v):return{'CONCLUÍDO':'Concluído','CONCLUIDO':'Concluído','FALTA NF':'Falta NF','FALTA O PEDIDO':'Falta pedido','FALTA PEDIDO':'Falta pedido','FALTA LANÇAMENTO':'Falta lançamento','FALTA LANCAMENTO':'Falta lançamento'}.get(str(v or'').strip().upper(),c(v)or'Não informado')
a=[];alerts=[]
for i,r in enumerate(W.iter_rows(min_row=3,max_col=18,values_only=True),3):
 if not c(r[16]):continue
 x,y,p,e,forn,o,vs,vp,vt,l,osn,req,ped,dp,nf,dnf,s,obs=r
 z=dict(id=i-2,recebimento=d(x),lancamento=d(y),prefixo=c(p),equipamento=c(e),fornecedor=c(forn),orcamento=c(o),valorServico=n(vs),valorPecas=n(vp),valorTotal=n(vt)if c(vt)!=None else n(vs)+n(vp),solicitante=c(l),ordemServico=c(osn),requisicao=c(req),pedido=c(ped),dataPedido=d(dp),nf=c(nf),dataNF=d(dnf),status=st(s),observacoes=c(obs));a.append(z)
 if not z['solicitante']:alerts.append({'nivel':'atenção','linha':i,'mensagem':'Solicitante ausente'})
 if not z['orcamento']:alerts.append({'nivel':'atenção','linha':i,'mensagem':'Orçamento ausente'})
 if z['valorTotal']<=0:alerts.append({'nivel':'crítico','linha':i,'mensagem':'Valor não positivo'})
 if z['status']=='Concluído'and not z['nf']:alerts.append({'nivel':'informativo','linha':i,'mensagem':'Concluído sem NF'})
seen=set();dups=0
for z in a:
 k=f"{z['fornecedor']}|{z['orcamento']}"if z['orcamento']else f"LINHA|{z['id']}"
 if k in seen:dups+=1
 seen.add(k)
text=json.dumps(a,ensure_ascii=False,separators=(',',':'));P=O/'orcamentos.json';old=P.read_text(encoding='utf-8')if P.exists()else None;changed=old!=text
if changed:P.write_text(text,encoding='utf-8')
M=O/'meta.json'
if changed or not M.exists():
 now=datetime.now(ZoneInfo('America/Cuiaba'));M.write_text(json.dumps({'atualizadoEm':now.isoformat(timespec='seconds'),'atualizadoEmTexto':now.strftime('%d/%m/%Y às %H:%M'),'arquivo':F.name,'linhasProcessadas':len(a),'duplicidadesAgrupadas':dups,'alertasValidacao':len(alerts)},ensure_ascii=False,indent=2),encoding='utf-8')
(R/'validation-report.json').write_text(json.dumps({'resumo':{'criticos':sum(x['nivel']=='crítico'for x in alerts),'atencao':sum(x['nivel']=='atenção'for x in alerts),'informativos':sum(x['nivel']=='informativo'for x in alerts)},'alertas':alerts},ensure_ascii=False,indent=2),encoding='utf-8');print(f'OK: {len(a)} registros; {dups} duplicidades; {len(alerts)} alertas; mudou={changed}')
