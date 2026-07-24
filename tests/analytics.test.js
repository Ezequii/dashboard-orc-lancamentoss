import test from'node:test';import assert from'node:assert/strict';import{cleanText,parseDate,uniqueBudgetRecords,criticality,stageDuration,analytics}from'../src/utils/dataUtils.js';
test('normaliza Charles Santos',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('datas BR e ISO',()=>assert.equal(parseDate('24/07/2026').getFullYear(),2026));
test('regra de unicidade',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('criticidade',()=>assert.equal(criticality(31),'critical'));
test('duração',()=>assert.equal(stageDuration('2026-07-01','2026-07-10'),9));
test('analytics cria faixas e líderes',()=>{const data=[{status:'Falta NF',diasParado:35,valorTotal:100,solicitante:'A'}];const result=analytics(data);assert.equal(result.pending.length,1);assert.equal(result.bucketData[3].count,1);assert.equal(result.leaders[0].criticos,1)});
