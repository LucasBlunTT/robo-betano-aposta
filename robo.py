from time import sleep
import pyperclip
import pyautogui
import re

entrada = 'Entrada'
green = 'GREEN'
red = 'Red'

pyautogui.mouseInfo()


def jogar():
    #pyautogui.moveTo(3038,840) # entrada betano
    pyautogui.moveTo(3105,654)
    pyautogui.click()
    print('...::: ENTROU COM A APOSTA :::...')
    verificarGreen()
    
def verificarGreen():
     while(True):
        pyautogui.moveTo(4101,1094)
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl','c')
        variavelGreen = pyperclip.paste() 
        if(variavelGreen != green or variavelGreen != red):
            print('VERIFICANDO GREEN PARA CONTINUAR')
        else:
            break
       
#def verificarOddFazerG2(variavelEntradaApos):
    #pyautogui.moveTo(574,351)
    #pyautogui.click()
    #sleep(1)
    #pyautogui.moveTo(598,335)
    #pyautogui.doubleClick()   
    #pyautogui.hotkey('ctrl','c')
    #sleep(1)
    #ultimaOdd = pyperclip.paste()
    #ultimaOdd = re.findall(r'\d+\.\d+', ultimaOdd)    
    #ultimaOdd = float(ultimaOdd[0])
    #print(ultimaOdd)
        
    #Fechando o modal da ODD
    #pyautogui.moveTo(1384,336)
    #pyautogui.click()
      
    #if(ultimaOdd < 2.00 and ultimaOdd != variavelEntradaApos):
        #print(ultimaOdd) 
        #print(variavelEntradaApos) 
        #print("Fazendo Gale")
        #jogar()          
    #else:
        #print ("cai no else")  
        #verificarOddFazerG2(variavelEntradaApos)         
      
while (True):
        
    # Mover até a palavra ENTRADA
    pyautogui.moveTo(4120,1039, duration=0.1)

    # Clicar 2 vezes
    pyautogui.doubleClick()

    # Esperar 1 segundo
    sleep(0.500)

    # Copiar conteudo 
    pyautogui.hotkey('ctrl','c')

    # Colar conteudo
    variavelEntrada = pyperclip.paste()
    
    if(variavelEntrada == entrada):      
        
        #--- Pegado o valor da entrada ---
        #pyautogui.moveTo(4269,1041)
        #pyautogui.tripleClick()   
        #pyautogui.hotkey('ctrl','c')
        #variavelEntradaApos = pyperclip.paste()
        #variavelEntradaApos = re.findall(r'\d+\.\d+', variavelEntradaApos)    
        #variavelEntradaApos = float(variavelEntradaApos[0])  
        
        #Chamando a funcao jogar
        jogar()  
              
        #sleep(8)
        
        #Chamando a funcao verificar e fazer G2
        #verificarOddFazerG2(variavelEntradaApos) 
        
        #Verificando se deu GREEN        
        #pyautogui.moveTo(4104,818)      
        ##pyautogui.doubleClick() 
        #pyautogui.hotkey('ctrl','c') 
        #variavelGreen1 = pyperclip.paste()
        #sleep(1)
        
        #Verificando se deu GREEN        
        #pyautogui.moveTo(4104,1070)     
        #pyautogui.doubleClick() 
        #pyautogui.hotkey('ctrl','c') 
        #variavelGreen2 = pyperclip.paste()
        #sleep(1)
        
        #if(variavelGreen1 == green or variavelGreen2 == green):
         #   return True    
                       
    else:    
        print('Esperando ENTRADA ')