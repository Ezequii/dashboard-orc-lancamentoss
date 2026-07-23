# Dashboard de Orçamentos — v4.5

Revisão de qualidade sobre a v4.4, mantendo o visual premium, seleção múltipla e atualização automática pela planilha.

## Ajustes desta revisão

- Conversor ignora corretamente linhas auxiliares e rodapés sem status.
- 2.294 linhas válidas processadas na base atual.
- Estado vazio quando nenhum registro corresponde aos filtros.
- Chips também para as datas selecionadas.
- Dias parados com destaque progressivo por faixa.
- Tabela móvel convertida em cartões identificados.
- Navegação por teclado nas linhas.
- Foco visível em botões e campos.
- Drawer fecha com `Esc` e permite copiar o número do orçamento.
- Rótulos e títulos de acessibilidade nos controles principais.
- Revisão do build e do workflow Excel → JSON.

## Atualizar a planilha sem terminal

1. Atualize o Excel.
2. Mantenha o nome `CONTROLE_DE_REQUISICOES_2026.xlsx`.
3. Substitua o arquivo em `atualizar_dados/`.
4. Faça commit e push pelo GitHub Desktop.
5. Na aba **Actions** do GitHub, aguarde **Atualizar dados do dashboard** ficar verde.
6. O GitHub gera o JSON e a data de atualização; o Cloudflare publica para todos.
