##### Importações #####
import time
import pyautogui
import pyperclip
import keyboard

##### Import de Objetos #####
with open("ObjectBase.txt", "r") as arquivo:
    objects = arquivo.readlines()
objects = [arquivo.strip('\n') for arquivo in objects]

##### Definição de Objetivo #####
print("""\
\033[1;31;40m   ____ _______ _____       _____ _                                 ______                     _            
\033[1;31;40m  |  _ \__   __/ ____|     / ____| |                               |  ____|                   | |           
\033[1;31;40m  | |_) | | | | |  __     | |    | |__   __ _ _ __   __ _  ___     | |__  __  _____  ___ _   _| |_ ___ _ __ 
\033[1;31;40m  |  _ <  | | | | |_ |    | |    | '_ \ / _` | '_ \ / _` |/ _ \    |  __| \ \/ / _ \/ __| | | | __/ _ \ '__|
\033[1;31;40m  | |_) | | | | |__| |    | |____| | | | (_| | | | | (_| |  __/    | |____ >  <  __/ (__| |_| | ||  __/ |   
\033[1;31;40m  |____/  |_|  \_____|     \_____|_| |_|\__,_|_| |_|\__, |\___|    |______/_/\_\___|\___|\__,_|\__\___|_|   
\033[1;31;40m                                                     __/ |                                                  
\033[1;31;40m                                                    |___/                                                   
""")
##### Escolha de Configuração de CLI #####
cli_configuration = input("""\
\033[1;31;40m CONFIGURAÇÃO DE CLI!
        \033[1;33;40m Deseja que o script execute os comandos de configuração na CLI?
            \033[1;34;40m set cli config-output-format set
            \033[1;34;40m set cli pager off
            \033[1;34;40m configure
\033[1;32;40m  Digite S/N:""")
if cli_configuration.lower() == "n":
    print("\033[1;37;40m  Configurações de CLI não serão executadas!")
    print('')
elif cli_configuration.lower() != "s":
    print("\033[1;37;40m  Opção não configurada, reinicie o script!")
    print('')
    input()
    exit()
elif cli_configuration.lower() == "s":
    print("\033[1;37;40m  Configurações de CLI serão executadas!")
    print('')
time.sleep(0.50)

##### Escolha de Contagem de Linhas #####
pause_configuration = input("""\
\033[1;31;40m PAUSA DE EXECUÇÃO!
        \033[1;33;40m Deseja que o script pause após uma certa quantidade de linhas inseridas?
\033[1;32;40m  Digite S/N:""")
if pause_configuration.lower() == "n":
    print("\033[1;37;40m  As pausas de script não serão executadas!")
    print('')
elif pause_configuration.lower() != "s":
    print("\033[1;37;40m  Opção não configurada, reinicie o script!")
    print('')
    input()
    exit()
elif pause_configuration.lower() == "s":
    time.sleep(0.25)
    try:
        pause_count = int(input("""\
        \033[1;33;40m Informe o número de linhas inseridas por pausa!
\033[1;32;40m  Informa um número inteiro:"""))
        print(f"\033[1;37;40m  As Pausas de script serão executadas a cada {pause_count} linhas!")
        print('')
    except:
        print(f"\033[1;37;40m  O Valor informado não é um número inteiro, reinicie o script!")
        print('')
        input()
        exit()
    
##### Configuração de Execução de Script #####
cli_inserts = []
for valores in objects:
    cli_inserts.append(valores)

##### Informativo de Inicio de Script #####
print("\033[1;31;40m 10 Segundos Para Inicio do Script !!!")
print("\033[1;31;40m Colocar Cursor do Mouse no Terminal (Preferencia no Final!)")
print('')
print("\033[1;33;40m Para Cancelar o Script, Basta Entrar no Terminal do VSCode e dar Ctrl+C")
print('')
time.sleep(10)

##### Configuração da CLI #####
cli_set = "set cli config-output-format set"
cli_pager = "set cli pager off"
cli_config = "configure"
if cli_configuration.lower() == 's':
    pyautogui.click(button='left')
    time.sleep(0.20)
    pyperclip.copy(cli_set)
    pyautogui.click(button='right')
    pyautogui.press('enter')
    time.sleep(0.50)
    pyperclip.copy(cli_pager)
    pyautogui.click(button='right')
    pyautogui.press('enter')
    time.sleep(0.50)
    pyperclip.copy(cli_config)
    pyautogui.click(button='right')
    pyautogui.press('enter')
    print("\033[1;31;40m CLI Configurada, iniciando script!!!")
    time.sleep(0.50)

##### Laço de Repetição Principal - Com Pause #####
if pause_configuration.lower() == "s":
    pyautogui.click(button='left')
    const = 0
    while True:
        for executes in cli_inserts:
            ##### Opção de Parar o Script #####
            const = const + 1
            if const == pause_count:
                print('')
                print("\033[1;31;40m Pause para validação de execuções! Validar na CLI.")
                print("\033[1;34;40m Ctrl+Shift para Continuar o script!")
                print('')
                keyboard.wait('Ctrl+Shift')
                print("\033[1;34;40m Continuando Script!")
                const = const - pause_count
                time.sleep(0.20)
            ##### Inserção de Código no Terminal #####
            pyperclip.copy(executes)
            time.sleep(0.10)
            pyautogui.click(button='right')
            time.sleep(0.20)
            pyautogui.press('enter')
            print(f'\033[0;37;40m Comando Inserido no Temrinal: {executes}')
            time.sleep(0.30)
        print('')
        print('\033[92m Script Encerrado.')
        print('')
        input()
        exit()
##### Laço de Repetição Principal - Sem Pause #####
elif pause_configuration.lower() == "n":
    pyautogui.click(button='left')
    const = 0
    while True:
        for executes in cli_inserts:
            ##### Inserção de Código no Terminal #####
            pyperclip.copy(executes)
            time.sleep(0.10)
            pyautogui.click(button='right')
            time.sleep(0.20)
            pyautogui.press('enter')
            print(f'\033[0;37;40m Comando Inserido no Temrinal: {executes}')
            time.sleep(0.30)
        print('')
        print('\033[92m Script Encerrado.')
        print('')
        input()
        exit()