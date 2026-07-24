import test from'node:test';import assert from'node:assert/strict';import{validateAlertRules,DEFAULT_ALERT_RULES}from'../src/config/alertRules.js';import{classifyAlert,cleanText,uniqueBudgetRecords}from'../src/utils/dataUtils.js';
test('regras padrão válidas',()=>assert.equal(validateAlertRules(DEFAULT_ALERT_RULES),true));
test('limite crítico inválido',()=>assert.equal(validateAlertRules({...DEFAULT_ALERT_RULES,criticalDays:10}),false));
test('classifica crítico',()=>assert.equal(classifyAlert({status:'Falta NF',diasParado:45,valorTotal:1},DEFAULT_ALERT_RULES),'critical'));
test('classifica alto valor',()=>assert.equal(classifyAlert({status:'Falta pedido',diasParado:2,valorTotal:200000},DEFAULT_ALERT_RULES),'high-value'));
test('normaliza e deduplica',()=>{assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS');assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1)});
