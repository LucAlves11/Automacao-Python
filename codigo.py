import pyautogui
import time

#DELAY 
pyautogui.PAUSE = 0.5

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
time.sleep(1)


# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
pyautogui.click(x=1116, y=275)
# Passo 5: Repetir para todos os produtos 

# pyautogui = fazer automações com python