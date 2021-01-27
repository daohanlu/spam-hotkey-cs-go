# spam-hotkey-cs-go
A simple keyboard manipulation tool for spamming Señorita in CS:GO in-game chat

## Setup
First, make sure you have python3 by typing `python` or `python3` in terminal/windows command line. Then you need to install pynput and upsidedown for typing stylized text in CS:GO. You can do this by typing `python -m pip install -r requirements.txt' after you cd into the project directory. On Windows you may need to launch powershell as an admin to use pip, which you can do by hitting Windows+X -> A -> (click yes) and then use the command above. 

## Usage
By default, the code types in a line from one of the txt files from the 'text' folder in game with random stylizations. You can change the keybind inside the function 'listen_keyboard_on_press'. Note that typing only works after you have opened the chatbox in-game, so you have to set the activation key for this script to the same key as the one that opens chatbox. 

Once you want to stop, or when your teammates finnally yells at you to stop, you can hit Alt+q to quit the script. 