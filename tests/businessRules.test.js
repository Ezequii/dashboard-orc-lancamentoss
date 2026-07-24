import test from'node:test';import assert from'node:assert/strict';import{cleanText,parseDate,uniqueBudgetRecords,criticality,stageDuration,exportCsv}from'../src/utils/dataUtils.js';
test('normaliza Charles Santos',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('datas BR e ISO',()=>{assert.equal(parseDate('24/07/2026').getFullYear(),2026);assert.equal(parseDate('2026-07-24').getMonth(),6)});
test('regra de unicidade',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('criticidade SLA',()=>{assert.equal(criticality(8),'attention');assert.equal(criticality(16),'high');assert.equal(criticality(31),'critical')});
test('duração entre etapas',()=>assert.equal(stageDuration('2026-07-01','2026-07-10'),9));
test('CSV filtrado',()=>assert.ok(exportCsv([{status:'Concluído'}]).includes('Concluído')));
