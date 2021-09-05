#!/usr/bin/env python3
import os
import pyaudio
from src.discord_bot import start_bot
from src.recognition import recognize_audio_forever


if __name__ == '__main__':
    print(f'SPEECH ALERT!\n\nThis program listens to live audio and notifies you on Discord when any keyword is identified. More on that later.')

    # Set Discord credentials
    discord_bot_token = ''
    discord_user_id = 0
    discord_secret_file_path = 'discord_secret.txt'
    if os.path.isfile(discord_secret_file_path):
        with open(discord_secret_file_path, 'r', encoding='utf-8') as discord_secret_file:
            try:
                discord_bot_token = next(discord_secret_file).strip()
                discord_user_id = int(next(discord_secret_file).strip())
            except Exception as e:
                input(f'{e}\nError while reading file. Restart the program.')
                exit()
    else:
        print('\nFirst, you need to configure your Discord credentials. If you are confused, read the instructions on GitHub.')
        with open(discord_secret_file_path, 'w', encoding='utf-8') as discord_secret_file:
            try:
                discord_bot_token = input('\tBOT TOKEN: ')
                discord_user_id = input('\tYOUR USER ID: ')
                discord_secret_file.writelines([discord_bot_token, '\n', discord_user_id])
            except Exception as e:
                input(f'{e}\nError while writing credentials file. Restart the program.')
                exit()

    # Initialize Bot
    bot = start_bot(bot_token=discord_bot_token, user_id=discord_user_id)

    # Set Recognition variables
    language_code = input('\nAudio Language (e.g. en-US, pt-PT) [Defaults to en-US]: ').strip()
    alert_message = input('What message should be sent to you? [Defaults to "ALERT!"]: ').strip()
    calibrate = input('Do you want to calibrate before listening (you should be silent while calibrating) [y/N]: ') in 'yY'
    max_phrase_duration = input('Maximum duration (in seconds) of each phrase [Defaults to 10]: ')

    if len(language_code) < 1:
        language_code = 'en-US'
    if len(alert_message) < 1:
        alert_message = 'ALERT!'
    if len(max_phrase_duration) < 1:
        max_phrase_duration = 10
    else:
        max_phrase_duration = int(max_phrase_duration)
    # if 'en-us' in language_code.lower():
    #     use_google = input('Do you want to use Google Speech Recognition API [Y/n]: ') not in 'nN'
    input('Press ENTER to proceed:')

    # Set Audio device
    audio_module = pyaudio.PyAudio()
    print('\nNow you need to choose which audio device to listen. If you are confused, read the instructions on Github.')
    for i in range(audio_module.get_device_count()):
        print(f'\t{audio_module.get_device_info_by_index(i)["index"]}: {audio_module.get_device_info_by_index(i)["name"]}')
    audio_device_index = int(input('Selected audio device [press ENTER to use default]: '))

    # Set keywords
    print(f'\nNow you need to input the set of words that will trigger a discord notification.'
          f'\nMake sure that each input consists of single, lowercase words.'
          f'\nA minimum of 5 keywords is recommended to prevent detection errors. After inserting, submit an empty word to proceed.')
    alert_keywords = []
    new_keyword = input('Insert new keyword (press ENTER to stop): ')

    while len(new_keyword):
        alert_keywords.append(new_keyword)
        new_keyword = input('Insert new keyword (press ENTER to stop): ')

    try:
        recognize_audio_forever(
            async_callback=bot.client.send_alert,
            callback_message=alert_message,
            keywords=alert_keywords,
            calibrate=calibrate,
            language_code=language_code,
            audio_device_index=audio_device_index,
            max_phrase_duration=max_phrase_duration
        )
    except Exception as e:
        input(f'{e}\nPress ENTER to exit: ')
