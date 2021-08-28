#!/usr/bin/env python3
from discord_bot import send_alert
from recognition import recognize_audio_forever
from project_variables import *


if __name__ == '__main__':
    print(f'SPEECH ALERT!\n\nThe current detection variables are:'
          f'\n\tCALIBRATE={CALIBRATE}\n\tUSE_GOOGLE={USE_GOOGLE}\n\tLANGUAGE_CODE={LANGUAGE_CODE}.\n\tALERT_MESSAGE={ALERT_MESSAGE}'
          f'\n\nIf you want to change them, modify the file project_variables.py and execute this script again.'
          f'\nRemember to set your Discord bot token and user ID.')
    input('ENTER to continue:')

    print(f'\nNow you need to input the set of words that will trigger a discord notification.'
          f'\nMake sure that each input consists of single, lowercase words.'
          f'\nA minimum of 5 keywords is recommended. After inserting, submit an empty word to proceed.')
    alert_keywords = []
    new_keyword = input('Insert new keyword (enter to stop): ')

    while len(new_keyword):
        alert_keywords .append(new_keyword)
        new_keyword = input('Insert new keyword (enter to stop): ')

    recognize_audio_forever(async_callback=send_alert, keywords=alert_keywords, calibrate=CALIBRATE)
