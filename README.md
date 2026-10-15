# Lembrete de Vencimento via WhatsApp

Automação em Python que lê uma planilha de clientes e envia, pelo WhatsApp Web, uma mensagem personalizada de cobrança para cada um, informando a data de vencimento e a chave Pix para pagamento.

Projeto de estudo, criado para praticar Python (leitura de planilhas, automação de tarefas e manipulação de datas) a partir de um tutorial em vídeo.

## Objetivo

Substituir o envio manual de lembretes de cobrança. Em vez de abrir cada conversa e digitar a mensagem, o programa faz isso automaticamente para todos os clientes da planilha.

## Como funciona

1. Abre o WhatsApp Web no navegador (é preciso estar logado).
2. Lê a planilha `clientes_vencimento.xlsx`, linha por linha, pegando nome, telefone e data de vencimento.
3. Monta uma mensagem personalizada com o nome do cliente e a data de vencimento.
4. Abre a conversa do cliente com a mensagem já digitada, usando um link do WhatsApp.
5. Envia a mensagem e fecha a aba.
6. Se algum envio falhar, registra o nome e o telefone do cliente no arquivo `errors.csv`.

## Tecnologias

- Python 3
- [openpyxl](https://openpyxl.readthedocs.io/): leitura da planilha Excel
- [pyautogui](https://pyautogui.readthedocs.io/): automação do mouse e do teclado
- Bibliotecas padrão: `webbrowser`, `urllib.parse`, `time`, `pathlib`

## Formato da planilha

A planilha deve se chamar `clientes_vencimento.xlsx`, ficar na mesma pasta do `app.py` e ter uma aba chamada `Clientes`, com estas colunas a partir da linha 2 (a linha 1 é o cabeçalho):

| Nome | Telefone | Data de Vencimento |
|---|---|---|
| Maria Exemplo | 5511999990000 | 25/10/2026 |

- **Telefone:** formato internacional, sem espaços, traços ou `+`: código do país (55) + DDD + número. Formate a coluna como **texto** para o Excel não alterar o número.
- **Data de Vencimento:** use uma data de verdade do Excel (não texto).

> A planilha real não é enviada ao GitHub porque contém dados pessoais de clientes (ela está no `.gitignore`). Crie a sua própria seguindo o modelo acima.

## Como executar

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```powershell
   pip install openpyxl pyautogui
   ```

4. Coloque a sua `clientes_vencimento.xlsx` na mesma pasta do `app.py`.
5. Deixe o WhatsApp Web logado no navegador e rode:

   ```powershell
   python app.py
   ```

O programa espera 30 segundos no início (tempo para o WhatsApp Web carregar ou para escanear o QR code) e depois começa a enviar as mensagens.

## Personalizando a mensagem

O texto da mensagem fica na variável `mensagem` dentro do `app.py`. Edite o texto e a chave Pix para os seus dados.

## Avisos importantes

- **O navegador precisa ficar aberto e visível** enquanto o programa roda, porque ele controla o mouse e o teclado.
- **Use só com clientes que concordaram em receber mensagens.** O envio automático em massa pode violar os termos de uso do WhatsApp e levar ao bloqueio do número.
- **Teste primeiro com o seu próprio número** antes de rodar com a lista completa.
- Não suba para o GitHub planilhas com dados reais nem informações pessoais.

## Possíveis melhorias

- Enviar mensagem só para clientes cujo vencimento está próximo ou já passou.
- Ajustar a mensagem conforme a situação (vence hoje, vencido, a vencer).
- Registrar no `errors.csv` o motivo de cada falha.
- Usar a API oficial do WhatsApp Business no lugar da automação pela interface.