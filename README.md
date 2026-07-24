# Dashboard AMAGGI v6.0 — Produção Corporativa

## Entregas
- Quality Gate: processamento, testes e build antes da publicação.
- Checksum SHA-256 da base e versão de esquema.
- Arquivo de saúde do pipeline em `public/data/health.json`.
- Módulo Produção com prontidão, saúde, atualização e auditoria local.
- Registro local das navegações e falhas de carregamento.
- Estrutura preparada para Microsoft Entra ID via `.env.example`.
- Credenciais e IDs reais não são incluídos no ZIP; precisam ser configurados pelo administrador do tenant.
- Dados externos ao bundle, metadados rastreáveis e relatório de validação.
- Visual AMAGGI, filtros, Acompanhamento, drawer e Modo TV preservados.

## Ativação futura do Entra ID
Preencha `VITE_ENTRA_TENANT_ID`, `VITE_ENTRA_CLIENT_ID`, `VITE_ALLOWED_DOMAIN` e altere `VITE_AUTH_MODE=entra` após registrar o aplicativo no tenant corporativo.
