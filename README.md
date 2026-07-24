# Dashboard AMAGGI v5.6 — Arquitetura Consolidada

## Estrutura
- Componentes separados para Sidebar, estados de carregamento/erro e produtividade.
- Serviços de dados isolados.
- Utilitários de datas, normalização, SLA, deduplicação e CSV.
- Design tokens AMAGGI centralizados.
- CSS separado em tokens, legado protegido e arquitetura.
- Regra de unicidade documentada como `fornecedor + orçamento`.
- Testes automatizados e GitHub Actions com teste antes do build.

## Preservado
Filtros múltiplos, chips, visão geral, acompanhamento, drawer, atualização Excel → JSON e Modo TV.
