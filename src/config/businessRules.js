export const STATUS_ORDER=['Falta lançamento','Falta pedido','Falta NF','Concluído'];
export const STATUS_LABELS={'Falta lançamento':'Não lançado','Falta pedido':'Sem pedido','Falta NF':'Sem NF','Concluído':'Concluído'};
export const STATUS_WEIGHT=Object.fromEntries(STATUS_ORDER.map((status,index)=>[status,index]));
