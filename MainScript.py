##### Imports #####
import time
import pyautogui
import pyperclip

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
input = input("\033[1;32;40m Enter one of the options: ")
print('')

##### DeviceGroup Configuration #####
show_application = (f'show device-group {device_group} application ')
show_application_group = (f'show device-group {device_group} application-group ')

show_service = (f'show device-group {device_group} service ')
show_service_group = (f'show device-group {device_group} service-group ')

show_address = (f'show device-group {device_group} address ')
show_address_group = (f'show device-group {device_group} address-group ')

rules = (f'show device-group {device_group} pre-rulebase security rules ')

cli_inserts =[]
##### Applications/Application-Groups #####
if input == "1":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_application}{varivel}')
        cli_inserts.append(shows)
elif input == "2":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_application_group}{varivel}')
        cli_inserts.append(shows)

##### Services/Service-Groups #####
elif input == "3":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_service}{varivel}')
        cli_inserts.append(shows)
elif input == "4":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_service_group}{varivel}')
        cli_inserts.append(shows)

##### Address/Address-Groups #####
elif input == "5":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_address}{varivel}')
        cli_inserts.append(shows)
elif input == "6":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{show_address_group}{varivel}')
        cli_inserts.append(shows)

##### Rules #####
elif input == "7":
    for valores in objects:
        varivel = (f'"{valores}"')
        shows = (f'{rules}{varivel}')
        cli_inserts.append(shows)

##### Incorrect Selection #####
else:
    print(f'\033[1;33;40m Option {input} Not Configured! Try again.')

##### Informs #####
print("\033[1;31;40m 15 Seconds to Start the Script !!!!!")
print("\033[1;31;40m Position the Cursor in the Terminal (Preferably at the End!)")
time.sleep(15)

##### CLI Objects Inserts #####
for executes in cli_inserts:
    pyautogui.click(button='left')
    pyperclip.copy(executes)
    pyautogui.click(button='right')
    pyautogui.press('enter')
    print(f"\033[1;31;40m {executes} Inserted in the Terminal!")
    time.sleep(0.50)
print("\033[1;33;40m All Objects Have Been Inserted into the Terminal! Script Closed.")