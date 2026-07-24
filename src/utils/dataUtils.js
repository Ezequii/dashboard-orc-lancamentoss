import{STATUS_WEIGHT}from'../config/businessRules.js';
export const cleanText=v=>typeof v==='string'?v.replace(/\u00a0/g,' ').replace(/\s+/g,' ').trim():v;
export const normalizeRecord=r=>({...r,solicitante:cleanText(r.solicitante),fornecedor:cleanText(r.fornecedor),status:cleanText(r.status),orcamento:cleanText(r.orcamento)});
export function uniqueBudgetRecords(records){const map=new Map();for(const record of records){const supplier=cleanText(record.fornecedor)||'SEM_FORNECEDOR',budget=cleanText(record.orcamento),key=budget?`${supplier}|${budget}`:`LINHA|${record.id}`;if(!map.has(key))map.set(key,record)}return[...map.values()]}
export function parseDate(value){if(!value)return null;const text=String(value).trim();let m=text.match(/^(\d{4})-(\d{2})-(\d{2})$/);if(m)return safe(+m[1],+m[2],+m[3]);m=text.match(/^(\d{2})[/.\-](\d{2})[/.\-](\d{4})$/);return m?safe(+m[3],+m[2],+m[1]):null}
function safe(y,m,d){const date=new Date(y,m-1,d,12);return date.getFullYear()===y&&date.getMonth()===m-1&&date.getDate()===d?date:null}
export const formatDate=v=>parseDate(v)?.toLocaleDateString('pt-BR')||'Não informado';
export const daysSince=v=>{const date=parseDate(v);return date?Math.max(0,Math.floor((Date.now()-date.getTime())/86400000)):null};
export const sortOperational=(a,b)=>(STATUS_WEIGHT[a.status]??99)-(STATUS_WEIGHT[b.status]??99)||(b.diasParado||0)-(a.diasParado||0);
