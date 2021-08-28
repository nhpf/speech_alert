#!/usr/bin/env python3
import asyncio
from typing import List, Callable
from abc import ABC
import speech_recognition as sr
from project_variables import USE_GOOGLE, LANGUAGE_CODE


class ProjectRecognizer(sr.Recognizer, ABC):
    def __init__(self):
        super().__init__()

    def chosen_recognizer(self, *args, **kwargs):
        return super().recognize_google(*args, **kwargs) if USE_GOOGLE else super().recognize_sphinx(*args, **kwargs)


# Call google speech recognition API
def recognize_audio_segment(recognizer: ProjectRecognizer, audio: sr.AudioData) -> str:
    try:  # To use anther api key, add parameter key="API_KEY"
        return recognizer.chosen_recognizer(audio, language=LANGUAGE_CODE)
    except sr.UnknownValueError:
        print('Could not recognize any word')
    except sr.RequestError as e:
        print(f'Request Error: {e}')
    return ''


# Briefly test if everything is working
def brief_test(calibrate: bool = False) -> None:
    mic = ProjectRecognizer()
    # Calibrate if asked to
    with sr.Microphone() as audio_source:
        if calibrate:
            mic.adjust_for_ambient_noise(audio_source)
            print("Calibration Done")
        # Capture phrase and recognize it
        captured_phrase = mic.listen(audio_source)
        recognize_audio_segment(mic, captured_phrase)


# Listen and process microphone audio until users asks to stop
def recognize_audio_forever(async_callback: Callable, keywords: List[str], calibrate: bool = False) -> None:
    # Set up speech recognition components
    speech_recognizer = ProjectRecognizer()
    microphone = sr.Microphone()
    with microphone as source:
        if calibrate:
            speech_recognizer.adjust_for_ambient_noise(source)
            print("Calibration Done.\n")

        # Forever
        while True:
            # Capture phrase and recognize it
            captured_phrase = speech_recognizer.listen(microphone)
            identified_phrase = recognize_audio_segment(speech_recognizer, captured_phrase)

            print('\t->' + identified_phrase)

            # If any word identified is a keyword, call callback function
            if any(keyword in identified_phrase.lower() for keyword in keywords):
                asyncio.get_event_loop().create_task(async_callback())
