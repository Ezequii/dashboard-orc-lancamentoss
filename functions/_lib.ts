export interface Env { DB:D1Database; FILES:R2Bucket }
export const json=(data:unknown,status=200)=>new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json; charset=utf-8'}});
export const email=(request:Request)=>request.headers.get('Cf-Access-Authenticated-User-Email')||'usuario-nao-identificado';
export const centers:Record<string,string>={MAG:'Mecanica Agricola',OFICINA:'Oficina / SCAE',LUB:'Lubrificacao',ELA:'Eletrica',BOR:'Borracharia',LAV:'Lavador',CAL:'Solda / Caldeiraria',TOR:'Tornearia',HIDR:'Hidraulica'};
export const isClosed=(status:string)=>status.toUpperCase().split(/\s+/).includes('ENCE');
