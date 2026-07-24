import test from'node:test';import assert from'node:assert/strict';import{cleanText,uniqueBudgetRecords,executiveMetrics}from'../src/utils/dataUtils.js';
test('normaliza texto',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('deduplica',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('calcula métricas executivas',()=>{const result=executiveMetrics([{status:'Concluído',valorTotal:100,fornecedor:'A'},{status:'Falta NF',valorTotal:50,diasParado:40,fornecedor:'B',solicitante:'C'}]);assert.equal(result.total,150);assert.equal(result.pending.length,1);assert.equal(result.critical.length,1);assert.equal(result.completionRate,50)});
