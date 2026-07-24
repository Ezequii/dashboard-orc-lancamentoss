export const SLA={normal:7,attention:15,high:30};
export const cleanText=v=>typeof v==='string'?v.replace(/\u00a0/g,' ').replace(/\s+/g,' ').trim():v;
export const normalizeRecord=r=>({...r,solicitante:cleanText(r.solicitante),fornecedor:cleanText(r.fornecedor),status:cleanText(r.status),orcamento:cleanText(r.orcamento)});
export function uniqueBudgetRecords(records){const m=new Map();for(const r of records){const f=cleanText(r.fornecedor)||'SEM_FORNECEDOR',o=cleanText(r.orcamento),k=o?`${f}|${o}`:`LINHA|${r.id}`;if(!m.has(k))m.set(k,r)}return[...m.values()]}
export function parseDate(v){if(!v)return null;const t=String(v).trim();let m=t.match(/^(\d{4})-(\d{2})-(\d{2})$/);if(m)return safe(+m[1],+m[2],+m[3]);m=t.match(/^(\d{2})[/.\-](\d{2})[/.\-](\d{4})$/);return m?safe(+m[3],+m[2],+m[1]):null}
function safe(y,m,d){const x=new Date(y,m-1,d,12);return x.getFullYear()===y&&x.getMonth()===m-1&&x.getDate()===d?x:null}
export const formatDate=v=>parseDate(v)?.toLocaleDateString('pt-BR')||'Não informado';
export const daysSince=v=>{const d=parseDate(v);return d?Math.max(0,Math.floor((Date.now()-d.getTime())/86400000)):null};
export const slaTone=n=>n==null?'day':n>SLA.high?'day critical':n>SLA.attention?'day high':n>SLA.normal?'day attention':'day';
export function exportCsv(records){const cols=['status','diasParado','recebimento','orcamento','fornecedor','solicitante','valorTotal'];const esc=v=>`"${String(v??'').replaceAll('"','""')}"`;return '\ufeff'+[cols.join(';'),...records.map(r=>cols.map(c=>esc(r[c])).join(';'))].join('\n')}
