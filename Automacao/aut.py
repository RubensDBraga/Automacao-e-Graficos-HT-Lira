import pyautogui
from time import sleep
import pandas
pyautogui.press('win')
pyautogui.PAUSE = 0.5
pyautogui.write('Opera')
pyautogui.press('enter')
sleep(1)
link = ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.write(link)
pyautogui.PAUSE = 0.5
pyautogui.press('enter')
sleep(2)
pyautogui.PAUSE = 0.5
pyautogui.click(x=831, y=394)
pyautogui.write('emailteste@outlook.com')
pyautogui.press('tab')
pyautogui.write('senhateste')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1.5)
tabela = pandas.read_csv('produtos.csv')
pyautogui.PAUSE = 0.5
for linha in tabela.index:
    pyautogui.click(x=903, y=277)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')


# pyautogui.click --> Clicar
# pyautogui.press --> Pressionar uma tecla
# pyautogui.write --> Escrever

# Passo 1: Abrir o sistema da empresa
# link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar a base de dados dos produtos
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar todos os produtos
