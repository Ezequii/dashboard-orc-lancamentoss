# Controle de Orçamentos de Serviços – v2

## Executar
```bash
npm install
npm run dev
```

## Publicar no Cloudflare
```bash
npx wrangler login
npm run deploy
```

### Regras
- Líder = Solicitante
- Serviço = número do orçamento único
- Valor = Valor Total
- Dias parados são calculados diariamente no navegador

## Versão 3
- Responsividade para TVs 4K/Full HD, monitores, notebooks, tablets e celulares
- Tabela convertida em cartões no celular
- Chave de serviço: fornecedor + número do orçamento
- Tooltips com nomes amigáveis
- Legenda mensal em ordem Recebidos / Concluídos
- Drawer com fornecedor no cabeçalho e valores com centavos
