import pyautogui
import time

pyautogui.PAUSE = 0.6
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1.5)

pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(3)

botao_escrever = pyautogui.locateCenterOnScreen("imagens/escrever.png")
pyautogui.click(botao_escrever)
pyautogui.write("kilton.araujo@gmail.com")
pyautogui.press("enter")

assunto = pyautogui.locateCenterOnScreen("imagens/assunto.png")
pyautogui.click(assunto)
pyautogui.write("Codigo.py")

pyautogui.click(x=1262, y=577)
pyautogui.write("Codigo de automação bem sucedido!")

enviar = pyautogui.locateCenterOnScreen("imagens/enviar.png")
pyautogui.click(enviar)