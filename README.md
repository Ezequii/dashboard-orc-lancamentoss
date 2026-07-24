# Dashboard AMAGGI v6.1.1 Corrigido

Correções desta entrega:

- Planilha atualiza `public/data/orcamentos.json` e `public/data/meta.json`.
- GitHub Actions monitora exatamente a planilha da pasta `atualizar_dados`.
- Workflow executa conversão, testes, build, commit, rebase e push.
- Removida a dependência de `health.json`, evitando o conflito “file does not exist on main”.
- Fontes aumentadas no desktop, Full HD, TV, tabelas, cards, filtros e drawer.
- Fluxo fixado nesta ordem operacional:
  1. Não lançado
  2. Sem pedido
  3. Sem NF
  4. Concluído
- Acompanhamento usa a mesma ordem; dentro de cada etapa, mostra primeiro quem tem mais dias parado.

## Como atualizar

Substitua somente o arquivo:

`atualizar_dados/CONTROLE_DE_REQUISICOES_2026.xlsx`

Depois faça commit e push. O workflow `Atualizar planilha e publicar dashboard` cuidará do restante.
