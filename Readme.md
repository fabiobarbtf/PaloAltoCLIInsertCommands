# PaloAlto CLI Insert Commands

> The script consists of copying and pasting the objects entered by the user into the PaloAlto SSH CLI.

## 💻 Prerequisites

Before you begin, make sure you have met the following requirements:

* You have installed the Pandas library `<pip install pyautogui>`
* You have installed the Pyperclip library `<pip install pyperclip>`
* You have installed the Keyboard library `<pip install keyboard`
* You have installed the Time library `<pip install time>`

## 🚀 Using the PaloAlto CLI Show Script

To use the PaloAlto CLI Show Script, follow these steps:

First! Configure the PaltoAlto CLI by disabling paging and entering configuration mode.

1. Enter all the commands line by line that you want to execute in the "ObjectBase.txt" file.
      Remeber! The Script and the "ObjectBase.txt" file must be in the same directory.
2. Start the script!
3. If you have not configured the Palo Alto CLI for SET mode and entered configuration mode, enter "Y" for the script to perform the configuration, otherwise enter "N".
      The commands executed are:
          set cli config-output-format set
          set cli pager off
          configure
4. The Script can pause after a certain number of lines are inserted into the CLI. If you want this option, type "Y", otherwise type "N"
      Enter the number of lines that must be inserted until the script pauses.
      After the number of lines entered are inserted, the Script will ask if everything is ok. To exit the script pause, simply press Ctrl+Shift.
      When the script is paused, you can perform any activity!
      Remember! Before pressing Ctrl+Shift, move the mouse cursor over the CLI Terminal.
5. After completing the steps above, the Script will start after 10 seconds, position the mouse cursor above the Terminal (Putty, Royal, etc.).
6. Just wait!! 🚀

## 🤝 Creator

To people who contributed and created this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/144133682" width="100px;" alt="Photo by Fábio Barbosa on GitHub"/><br>
        <sub>
          <b>Fábio Barbosa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>