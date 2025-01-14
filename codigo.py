import pyautogui
import time

pyautogui.PAUSE = 0.5

#1 PASSO: ENTRAR NO SITE
pyautogui.press("win")
pyautogui.write('Chrome')
pyautogui.press('enter')
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

#2 PASSO: FAZER O LOGIN
pyautogui.press('tab')
pyautogui.write('felipeghensev@gmail.com')
pyautogui.press('tab')
pyautogui.write('senhadomaster1')
pyautogui.press('tab')
pyautogui.press('enter')

#3 PASSO: IMPORTAR A BASE DE DADOS DO PRODUTO
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

#4 PASSO: CADASTRAR 1 PRODUTO E DPS CADASTRAR PARA TODOS
for linha in tabela.index:
    pyautogui.click(x=690, y=257)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca) 
    pyautogui.press("tab")

    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(tipo)
    pyautogui.press("tab")


    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter") 

    



