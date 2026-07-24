import test from'node:test';import assert from'node:assert/strict';import{cleanText,parseDate,uniqueBudgetRecords,isStale,checksum}from'../src/utils/dataUtils.js';
test('normaliza texto',()=>assert.equal(cleanText(' CHARLES\u00a0 SANTOS '),'CHARLES SANTOS'));
test('interpreta data',()=>assert.equal(parseDate('24/07/2026').getFullYear(),2026));
test('deduplica',()=>assert.equal(uniqueBudgetRecords([{id:1,fornecedor:'A',orcamento:'1'},{id:2,fornecedor:'A',orcamento:'1'}]).length,1));
test('detecta base antiga',()=>assert.equal(isStale('2020-01-01T00:00:00-04:00'),true));
test('checksum é determinístico',()=>assert.equal(checksum([{a:1}]),checksum([{a:1}])));
