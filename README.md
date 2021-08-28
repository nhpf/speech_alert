## SPEECH ALERT

An idea proposed by @gpizzigh, this script enables your microphone and notifies you on Discord when a keyword is identified.

Environment Setup
 - Clone this repository, and make sure you have [Python 3](https://www.python.org/) installed
 - Run `pip install -r requirements.txt`
     - On Windows, if an error occurs when trying to install PyAudio, [download the wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) compatible with your system and run `pip install [file_name.whl]`
     - Another solution:
        ```
        pip install pipwin 
        pipwin install pyaudio
        ```

Discord Setup
 - On [Discord developer portal](https://discord.com/developers/) Go to "Applications" and select/create your bot
 - Then, go to Bot, scroll to 'Privileged Gateway Intents' and enable 'SERVER MEMBERS INTENT' (toggle switch)
 - On the same page, next to the ICON section, the application token and paste it in `project_variables.py`
 - Get your user ID in your profile page and paste it in `project_variables.py` as well.

Finally, you can run `python3 main.py` and follow the instructions there. All parameters that you can (should) tweak can be found in the file `project_variables.py`
