## SPEECH ALERT

An idea proposed by @gpizzigh, this script enables your microphone and notifies you on Discord when a keyword is identified.


#### Windows Users
 - Go to the "Releases" section on the right and download the most recent zip file
 - Ignore the "Environment Setup" section
 - To hear audio **coming from your PC** instead of a microphone, enable [Stereo Mix](https://thegeekpage.com/stereo-mix/)
 - Run the executable file. If any instruction there confuses you, check the Troubleshooting section on the bottom of this page

---

#### Environment Setup
 - Clone this repository, and make sure you have [Python 3](https://www.python.org/) installed
 - Run `pip install -r requirements.txt`
     - On Windows, if an error occurs when trying to install PyAudio, [download the wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) compatible with your system and run `pip install [file_name.whl]`
     - Another solution:
        ```
        pip install pipwin 
        pipwin install pyaudio
        ```

---

#### Troubleshooting
 - **Bot Token**
    - If you are using someone else's bot, ask them for the Bot Token. If you are on your own, then you have to create your own bot (follow the steps below):
    - On [Discord developer portal](https://discord.com/developers/) Go to "Applications" and select/create your bot
    - Then, go to Bot, scroll to 'Privileged Gateway Intents' and enable 'SERVER MEMBERS INTENT' (toggle switch)
    - On the same page, next to the ICON section, copy the application token

 - **User ID**
    - To get notified, you need to know you Discord user ID
    - On the Discord desktop/mobile application, go to **User Settings -> Advanced** and enable Developer Mode
    - Now, in **User Settings**, go to My Account and click on the three dots next to you username. Now you can copy you User ID

After setting the Bot Token and your User ID properly, when you run the program you should receive a direct message on Discord from the bot telling you that it is online.

 - **Language Code**: input the ISO 639-1 codes for your language (en-US, pt-BR, es-MX)
 
 - **Alert Message**: what the bot will send you when any keyword is detected from the live input audio
 
 - **Calibration**: to adjust the detection noise threshold for your microphone, enable this option and don't speak while calibrating. It should take less than 5 seconds

 - **Maximum Phrase Duration**: each phrase being said is processed when the speaker stops talking for a brief moment or the maximum phrase duration is reached

 - **Audio Devices**:
    - The program asks you to select an audio device. If the audio you want to capture comes from your microphone, select the first option (uses the default) by entering the number `0`.
    But you probably want to detect audio that you can hear **coming out of your PC** (Zoom, YouTube, Google Meet, etc). In that case, enable [Stereo Mix](https://thegeekpage.com/stereo-mix/)
    and run the program again. Now enter the number corresponding to the first listed option that contains "Stereo Mix".

 - **Keywords**: you can insert any number of words that trigger the Discord notification. Make sure that each insertion consists of single, lowercase words. When you are done, press enter (as if you were entering an empty word).
