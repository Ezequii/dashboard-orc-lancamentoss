import test from'node:test';import assert from'node:assert/strict';import{cleanText,parseDate,uniqueBudgetRecords,slaTone,exportCsv}from'../src/utils/dataUtils.js';
test('remove espaços invisíveis',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('converte datas brasileiras e ISO',()=>{assert.equal(parseDate('24/07/2026').getFullYear(),2026);assert.equal(parseDate('2026-07-24').getMonth(),6)});
test('deduplica por fornecedor e orçamento',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('classifica SLA',()=>{assert.equal(slaTone(8),'day attention');assert.equal(slaTone(31),'day critical')});
test('exporta CSV UTF-8',()=>assert.ok(exportCsv([{status:'Concluído'}]).includes('Concluído')));
