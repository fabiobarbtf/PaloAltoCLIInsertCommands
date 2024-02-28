##### Imports #####
import time
import pyautogui
import pyperclip
import keyboard

##### Object Import #####
with open("ObjectBase.txt", "r") as arquivo:
    objects = arquivo.readlines()
objects = [arquivo.strip('\n') for arquivo in objects]

##### Goal Definition #####
print("""\
\033[1;34;40m   ____ _                              _____                     _            
\033[1;34;40m  / ___| |__   __ _ _ __   __ _  ___  | ____|_  _____  ___ _   _| |_ ___ _ __ 
\033[1;34;40m | |   | '_ \ / _` | '_ \ / _` |/ _ \ |  _| \ \/ / _ \/ __| | | | __/ _ \ '__|
\033[1;34;40m | |___| | | | (_| | | | | (_| |  __/ | |___ >  <  __/ (__| |_| | ||  __/ |   
\033[1;34;40m  \____|_| |_|\__,_|_| |_|\__, |\___| |_____/_/\_\___|\___|\__,_|\__\___|_|   
\033[1;34;40m                          |___/                                               
""")
##### Choosing CLI Configuration #####
cli_configuration = input("""\
\033[1;31;40m CLI SETUP!
        \033[1;33;40m Do you want the script to run configuration commands in the CLI?
            \033[1;34;40m set cli config-output-format set
            \033[1;34;40m set cli pager off
            \033[1;34;40m configure
\033[1;32;40m  Type Y/N:""")
if cli_configuration.lower() == "n":
    print("\033[1;37;40m  CLI settings will not be executed!")
    print('')
elif cli_configuration.lower() != "y":
    print("\033[1;37;40m  Option not configured, restart the script!")
    print('')
    input()
    exit()
elif cli_configuration.lower() == "y":
    print("\033[1;37;40m  CLI settings will be executed!")
    print('')
time.sleep(0.50)

##### Choosing Row Count #####
pause_configuration = input("""\
\033[1;31;40m EXECUTION PAUSE!
        \033[1;33;40m Do you want the script to pause after a certain number of lines entered?
\033[1;32;40m  Digite Y/N:""")
if pause_configuration.lower() == "n":
    print("\033[1;37;40m  Script pauses will not be executed!")
    print('')
elif pause_configuration.lower() != "y":
    print("\033[1;37;40m  Option not configured, restart the script!")
    print('')
    input()
    exit()
elif pause_configuration.lower() == "y":
    time.sleep(0.25)
    try:
        pause_count = int(input("""\
        \033[1;33;40m Enter the number of lines inserted per pause!
\033[1;32;40m  Enter an integer:"""))
        print(f"\033[1;37;40m  Script Pauses will run every {pause_count} lines!")
        print('')
    except:
        print(f"\033[1;37;40m  The Value entered is not an integer, restart the script!")
        print('')
        input()
        exit()
    
##### Script Execution Configuration #####
cli_inserts = []
for valores in objects:
    cli_inserts.append(valores)

##### Script Start Information #####
print("\033[1;31;40m 10 Seconds to Start the Script !!!")
print("\033[1;31;40m Place Mouse Cursor in Terminal (Preference at the End!)")
print('')
print("\033[1;33;40m To cancel the script, simply enter the VSCode Terminal and press Ctrl+C")
print('')
time.sleep(10)

##### CLI Configuration #####
cli_set = "set cli config-output-format set"
cli_pager = "set cli pager off"
cli_config = "configure"
if cli_configuration.lower() == 'y':
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
    print("\033[1;31;40m Configured CLI, starting script!!!")
    time.sleep(0.50)

##### Main Repeat Loop - With Pause #####
if pause_configuration.lower() == "y":
    pyautogui.click(button='left')
    const = 0
    while True:
        for executes in cli_inserts:
            ##### Option to Stop the Script #####
            const = const + 1
            if const == pause_count:
                print('')
                print("\033[1;31;40m Pause to validate executions! Validate in CLI.")
                print("\033[1;34;40m Ctrl+Shift to Continue the script!")
                print('')
                keyboard.wait('Ctrl+Shift')
                print("\033[1;34;40m Continuing Script!")
                const = const - pause_count
                time.sleep(0.20)
            ##### Inserting Code in the Terminal #####
            pyperclip.copy(executes)
            time.sleep(0.10)
            pyautogui.click(button='right')
            time.sleep(0.20)
            pyautogui.press('enter')
            print(f'\033[0;37;40m Command Entered in Terminal: {executes}')
            time.sleep(0.30)
        print('')
        print('\033[92m Script Closed.')
        print('')
        input()
        exit()
##### Main Repeat Loop - No Pause #####
elif pause_configuration.lower() == "n":
    pyautogui.click(button='left')
    const = 0
    while True:
        for executes in cli_inserts:
            ##### Inserting Code in the Terminal #####
            pyperclip.copy(executes)
            time.sleep(0.10)
            pyautogui.click(button='right')
            time.sleep(0.20)
            pyautogui.press('enter')
            print(f'\033[0;37;40m Command Entered in Terminal: {executes}')
            time.sleep(0.30)
        print('')
        print('\033[92m Script Closed.')
        print('')
        input()
        exit()