import pyautogui
import time

#DELAY 
pyautogui.PAUSE = 0.5

# pyautogui = fazer automações com python
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> aperta 1 tecla do teclado
# pyautogui.write -> escreve um texto
# pyautogui.hotkey -> apertar uma combinação de teclas, separado por virgula

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")


#digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
#esperar X segundos com a biblioteca "time"
time.sleep(1) 


# Passo 2: Fazer login
# email
pyautogui.click(x=774, y=380)
pyautogui.write("lucca1969@gmail.com")
# senha
pyautogui.press("tab")
pyautogui.write("123456")
# botao logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv") #criei o pandas e armazenei dentro da variavel tabela


# Passo 4: Cadastrar 1 produto 
for linha in tabela.index: # para cada linha da minha tabela
    pyautogui.click(x=1116, y=275)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"]) #string = texto no python -> str() agora ele vai pegar o numero entre aspas e n vai dar erro
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(obs) 
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(3000)


# Passo 5: Repetir para todos os produtos