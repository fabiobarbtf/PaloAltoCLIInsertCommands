##### Imports #####
import time
import pyautogui
import pyperclip

def promptCommand(device_group, sub_command, objects):
    command = f"show device-group {device_group} {sub_command} "

    for values in objects:
            aux = (f'"{values}"')
            shows = (f'{command}{aux}')
            cli_inserts.append(shows)

if __name__ == "__main__":
    ##### Objects Imports #####
    with open('ObjectBase.txt', 'r') as file:
        objects =  file.readlines()
    objects = [file.strip('\n') for file in objects]

    ##### Objetive Definition #####
    print("""\
        ____       _         _    _ _           ____ _     ___   ____  _                     ____            _       
    |  _ \ __ _| | ___   / \  | | |_ ___    / ___| |   |_ _| / ___|| |__   _____      __ / ___|  ___ _ __(_)_ __  
    | |_) / _` | |/ _ \ / _ \ | | __/ _ \  | |   | |    | |  \___ \| '_ \ / _ \ \ /\ / / \___ \ / __| '__| | '_ \ 
    |  __/ (_| | | (_) / ___ \| | || (_) | | |___| |___ | |   ___) | | | | (_) \ V  V /   ___) | (__| |  | | |_) |
    |_|   \__,_|_|\___/_/   \_\_|\__\___/   \____|_____|___| |____/|_| |_|\___/ \_/\_/   |____/ \___|_|  |_| .__/ 
                                                                                                        |_|    
        """)
    device_group = input("\033[1;32;40m Enter the Device_Group: ")
    print("\033[1;33;40m Apps(1)     Apps-Group(2)     Serv(3)     Serv-Group(4)     Addr(5)     Addr-Groups(6)     Rules(7)")
    option = int(input("\033[1;32;40m Enter one of the options: "))
    print('')

    cli_inserts = []

    ##### Applications/Application-Groups #####
    if option == 1:
        promptCommand(device_group, "application", objects)
    elif option == 2:
        promptCommand(device_group, "application-group", objects)
    elif option == 3:
        promptCommand(device_group, "service", objects)
    elif option == 4:
        promptCommand(device_group, "service-group", objects)
    elif option == 5:
        promptCommand(device_group, "address", objects)
    elif option == 6:
        promptCommand(device_group, "address-group", objects)
    elif option == 7:
        promptCommand(device_group, "pre-rulebase security rules", objects)
    else:
        print(f'\033[1;33;40m Option {option} Not Configured! Try again.')

    ##### Informs #####
    print("\033[1;31;40m 15 Seconds to Start the Script !!!!!")
    print("\033[1;31;40m Position the Cursor in the Terminal (Preferably at the End!)")
    time.sleep(15)

    ##### CLI Objects Inserts #####
    for executions in cli_inserts:
        pyautogui.click(button='left')
        pyperclip.copy(executions)
        pyautogui.click(button='right')
        pyautogui.press('enter')
        print(f"\033[1;31;40m {executions} Inserted in the Terminal!")
        time.sleep(0.50)

    print("\033[1;33;40m All Objects Have Been Inserted into the Terminal! Script Closed.")
