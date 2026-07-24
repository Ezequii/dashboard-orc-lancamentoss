import test from'node:test';import assert from'node:assert/strict';import{validateSettings,isStale,cleanText,uniqueBudgetRecords}from'../src/utils/dataUtils.js';import{DEFAULT_SETTINGS}from'../src/config/businessRules.js';
test('configuração padrão é válida',()=>assert.equal(validateSettings(DEFAULT_SETTINGS),true));
test('SLA fora de ordem é inválido',()=>assert.equal(validateSettings({...DEFAULT_SETTINGS,slaNormal:30,slaAttention:15}),false));
test('detecta base antiga',()=>assert.equal(isStale('2020-01-01T00:00:00-04:00',24),true));
test('normaliza espaços invisíveis',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('regra de unicidade',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
