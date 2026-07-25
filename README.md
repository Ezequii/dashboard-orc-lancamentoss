# Dashboard AMAGGI v6.2.3 — Fonte Compartilhada SharePoint

O dashboard lê uma única planilha corporativa no SharePoint para todos os usuários.

A URL informada já está em `wrangler.jsonc`. Para ativar, configure no Cloudflare Pages os secrets:

- `ENTRA_TENANT_ID`
- `ENTRA_CLIENT_ID`
- `ENTRA_CLIENT_SECRET`

O aplicativo Microsoft Entra precisa de permissão de aplicação para ler o arquivo no SharePoint, com consentimento administrativo. Recomenda-se restringir o acesso ao site necessário.

Após configurar, qualquer alteração salva na planilha central será vista por todos ao abrir o dashboard ou clicar em **Atualizar agora**. Se a integração falhar, o painel usa a base publicada de contingência e mostra o motivo.

Nunca coloque o Client Secret no repositório ou no ZIP.
