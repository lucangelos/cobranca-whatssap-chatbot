# Descrever os passos manuais e depois transformar isso em código

import openpyxl
from pathlib import Path
# Possibilita mandar mensagens especiais no whatssap
from urllib.parse import quote 
# Para conseguir abrir o seu navegador
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(30)
# Pasta onde o app.py está
pasta = Path(__file__).parent

# Carrega a planilha que está na mesma pasta do app.py
workbook = openpyxl.load_workbook(pasta / 'clientes_vencimento.xlsx')
paginaClientes = workbook['Clientes']

for linha in paginaClientes.iter_rows(min_row=2):
    # nome, telefone, vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f"Olá {nome}, seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Por favor, pagar no pix, a chave pix é: lucasangelossilva@gmail.com"

    # Criar links personalizados do whatssap e enviar para cada cliente com base nos dados da planilha
    link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
    webbrowser.open(link_mensagem_whatsapp)
    sleep(15)
    try:
        # Clicar na seta
        sleep(5)
        pyautogui.press('enter')
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except Exception as erro:
        print(f"Não foi possível mandar mensagem para {nome}")
        print(erro)
        with open('errors.csv','a',newline='',encoding='utf -8') as arquivo: 
            arquivo.write(f'{nome},{telefone}\n')


