# Dashboard AMAGGI v6.2.5 — Sem Node.js no computador

## Requisitos no computador

- Python 3.12
- Git for Windows ou GitHub Desktop com o comando `git` disponível
- **Node.js não é necessário no computador**

## Como funciona

1. O Python converte a planilha em `public/data/orcamentos.json` e `meta.json`.
2. O arquivo BAT cria o commit e faz o push pelo Git.
3. O Cloudflare conectado ao GitHub executa o build no servidor.
4. Todos os usuários recebem a atualização.

## Uso

Primeira vez: `CONFIGURAR_PRIMEIRA_VEZ_SEM_NODE.bat`

Atualizações: substitua a planilha e execute `ATUALIZAR_E_ENVIAR_SEM_NODE.bat`.

A pasta precisa ser o repositório Git clonado, contendo a subpasta `.git`. Não execute em uma cópia ZIP isolada.
