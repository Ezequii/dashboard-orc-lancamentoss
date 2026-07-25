async function read(url,signal){const r=await fetch(`${url}?v=${Date.now()}`,{signal,cache:'no-store'});if(!r.ok)throw new Error(`Falha ao carregar ${url}: HTTP ${r.status}`);return r.json()}
export async function loadDashboardData(signal){const[records,meta]=await Promise.all([read('/data/orcamentos.json',signal),read('/data/meta.json',signal)]);return{records,meta}}
