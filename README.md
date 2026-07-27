# Dashboard PCM OS - V1 com substituicao integral

## Comportamento da importacao
A nova carga e validada no navegador e novamente no servidor. Os registros sao gravados em `staging_orders`. A tabela ativa `orders` so e apagada depois que a quantidade esperada e a quantidade gravada forem iguais e não houver erros. Se qualquer etapa falhar, a base anterior permanece intacta.

### Bloqueios
- arquivo ausente, corrompido ou sem `Planilha1`;
- colunas obrigatorias ausentes;
- nenhuma ordem valida;
- Ordem ou Data de entrada ausente/invalida;
- numero de Ordem duplicado com dados divergentes;
- divergencia entre contagem validada e contagem gravada no D1;
- queda superior a 50% sem confirmacao explicita.

### Avisos
- notificador nao localizado;
- prefixo vazio;
- centro vazio ou desconhecido;
- OFICINA aberta sem texto iniciado por RC.

## Atualizacao no GitHub
Substitua os arquivos do repositorio pelos deste pacote. Renomeie `wrangler.example.jsonc` para `wrangler.jsonc` e informe o UUID real do D1. Nunca deixe numeros ou texto fora das chaves do JSON.

## D1
Execute o conteudo de `migrations/0001_initial.sql` no Console do D1. Se as tabelas antigas ja existirem com outra estrutura, para uma V1 limpa, apague as tabelas antigas e execute esta migracao novamente.

## Cloudflare Pages
Build: `npm run build`
Deploy: `CLOUDFLARE_API_TOKEN="$PAGES_API_TOKEN" npx wrangler pages deploy dist --project-name=dashboard-pcm-os --branch=main`

O bucket R2 deve se chamar `dashboard-os-importacoes`. Depois de uma substituicao concluida, os arquivos originais de importacoes anteriores sao removidos do R2, mas o historico resumido fica no D1.
