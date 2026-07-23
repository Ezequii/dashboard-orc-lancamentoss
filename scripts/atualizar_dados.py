from pathlib import Path
from datetime import datetime,date
from zoneinfo import ZoneInfo
import json
from openpyxl import load_workbook
R=Path(__file__).resolve().parents[1];f=R/'atualizar_dados/CONTROLE_DE_REQUISICOES_2026.xlsx';w=load_workbook(f,data_only=True,read_only=True)['Acompanhamento RC 2026']
def c(v):
 if v in(None,'','*','-'):return None
 if isinstance(v,(datetime,date)):return v.strftime('%Y-%m-%d')
 if isinstance(v,str):return ' '.join(v.replace('\u00a0',' ').split()).strip() or None
 return v
def n(v):
 try:return float(v or 0)
 except:return 0
def d(v):
 v=c(v)
 if not v:return None
 if isinstance(v,str):
  for p in ('%Y-%m-%d','%d/%m/%Y','%d.%m.%Y','%d-%m-%Y'):
   try:return datetime.strptime(v,p).strftime('%Y-%m-%d')
   except ValueError:pass
 return None
def st(v):return {'CONCLUÍDO':'Concluído','CONCLUIDO':'Concluído','FALTA NF':'Falta NF','FALTA O PEDIDO':'Falta pedido','FALTA PEDIDO':'Falta pedido','FALTA LANÇAMENTO':'Falta lançamento','FALTA LANCAMENTO':'Falta lançamento'}.get(str(v or '').strip().upper(),str(v or 'Não informado').strip())
a=[]
for i,r in enumerate(w.iter_rows(min_row=3,max_col=18,values_only=True),3):
 if not c(r[16]):continue
 x,y,p,e,forn,o,vs,vp,vt,l,osn,req,ped,dp,nf,dnf,s,obs=r
 a.append(dict(id=i-2,recebimento=d(x),lancamento=d(y),prefixo=c(p),equipamento=c(e),fornecedor=c(forn),orcamento=c(o),valorServico=n(vs),valorPecas=n(vp),valorTotal=n(vt) if c(vt)!=None else n(vs)+n(vp),solicitante=c(l),ordemServico=c(osn),requisicao=c(req),pedido=c(ped),dataPedido=d(dp),nf=c(nf),dataNF=d(dnf),status=st(s),observacoes=c(obs)))
(R/'src/data/orcamentos.json').write_text(json.dumps(a,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
now=datetime.now(ZoneInfo('America/Cuiaba'));(R/'src/data/meta.json').write_text(json.dumps({'atualizadoEmTexto':now.strftime('%d/%m/%Y às %H:%M'),'linhasProcessadas':len(a),'arquivo':f.name},ensure_ascii=False,indent=2),encoding='utf-8');print(len(a))
