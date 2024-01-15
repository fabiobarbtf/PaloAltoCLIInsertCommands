# PaloAlto CLI Show Script

> The script consists of copying and pasting the objects entered by the user into the PaloAlto SSH CLI.

## 💻 Prerequisites

Before you begin, make sure you have met the following requirements:

* You have installed the Pandas library `<pip install pyautogui>`
* You have installed the Requests library `<pip install pyperclip>`
* You have installed the Requests library `<pip install time>`

## 🚀 Using the PaloAlto CLI Show Script

To use the PaloAlto CLI Show Script, follow these steps:

First! Configure the PaltoAlto CLI by disabling paging and entering configuration mode.
```
set cli pager off
```

```
configure
```

1. Enter line by line the objects you want to show within the CLI in the "ObjectBase.txt" file.
    Remember! The script is only configured for Applications, Application-Groups, Services, Service-Groups, Addresses, Address-Group and Policies.
2. Start the script!
3. Inform the device-group!
4. Inform what type of object are those passed in the "ObjectBase.txt" file.
5. Position the mouse cursor in the PaloAlto CLI Terminal, preferably at the end of the CLI.
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