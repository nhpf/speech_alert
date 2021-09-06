#!/usr/bin/env python3
import asyncio
from typing import List, Callable
import speech_recognition as sr


# Call google speech recognition API
def recognize_audio_segment(recognizer: sr.Recognizer, audio: sr.AudioData, language_code: str) -> str:
    try:  # To use anther api key, add parameter key="API_KEY"
        return recognizer.recognize_google(audio, language=language_code)
    except sr.UnknownValueError:
        print('Could not recognize any word')
    except sr.RequestError as e:
        print(f'Request Error: {e}')
    return ''


# Briefly test if everything is working
def brief_test(calibrate: bool = False, language_code: str = 'en-US', audio_device_index: int = 0) -> None:
    mic = sr.Recognizer()
    # Calibrate if asked to
    with sr.Microphone(audio_device_index) as audio_source:
        if calibrate:
            mic.adjust_for_ambient_noise(audio_source)
            print("Calibration Done")
        print("Start Speaking:\n")
        # Capture phrase and recognize it
        captured_phrase = mic.listen(audio_source)
        recognize_audio_segment(mic, captured_phrase, language_code)


# Listen and process microphone audio until users asks to stop
def recognize_audio_forever(
        async_callback: Callable,
        callback_message: str,
        keywords: List[str],
        calibrate: bool,
        language_code: str,
        audio_device_index: int,
        max_phrase_duration: int) -> None:
    # Set up speech recognition components
    speech_recognizer = sr.Recognizer()
    microphone = sr.Microphone(audio_device_index)
    with microphone as source:
        if calibrate:
            input("\nStarting calibration. Remain silent and, when you are ready, press ENTER and wait: ")
            speech_recognizer.adjust_for_ambient_noise(source)
            print("\tCalibration Done.")
        print("\nNow you can start speaking. Recognized phrases will be shown below:\n")

        # Forever
        while True:
            # Capture phrase and recognize it
            captured_phrase = speech_recognizer.listen(microphone, phrase_time_limit=max_phrase_duration)
            identified_phrase = recognize_audio_segment(speech_recognizer, captured_phrase, language_code)

            print('\t->' + identified_phrase)

            # If any word identified is a keyword, call callback function
            if any(keyword in identified_phrase.lower() for keyword in keywords):
                asyncio.get_event_loop().create_task(async_callback(callback_message))
