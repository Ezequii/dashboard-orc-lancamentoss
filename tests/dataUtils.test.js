import test from'node:test';import assert from'node:assert/strict';import{cleanText,parseDate,uniqueBudgetRecords,slaTone,exportCsv}from'../src/utils/dataUtils.js';
test('normaliza espaço invisível',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('interpreta data BR e ISO',()=>{assert.equal(parseDate('24/07/2026').getFullYear(),2026);assert.equal(parseDate('2026-07-24').getMonth(),6)});
test('deduplica conforme regra documentada',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('SLA centralizado',()=>{assert.equal(slaTone(8),'day attention');assert.equal(slaTone(31),'day critical')});
test('CSV preserva UTF-8',()=>assert.ok(exportCsv([{status:'Concluído'}]).includes('Concluído')));
