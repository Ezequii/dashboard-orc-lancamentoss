import test from'node:test';import assert from'node:assert/strict';import{cleanText,sortOperational,uniqueBudgetRecords}from'../src/utils/dataUtils.js';
test('normaliza espaços',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('ordem operacional obrigatória',()=>{const rows=[{status:'Concluído'},{status:'Falta NF'},{status:'Falta lançamento'},{status:'Falta pedido'}].sort(sortOperational);assert.deepEqual(rows.map(x=>x.status),['Falta lançamento','Falta pedido','Falta NF','Concluído'])});
test('deduplica',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
