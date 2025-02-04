# mini_chat_bot
# Personal Assistant

This is a simple personal assistant application built using Python. It uses `speech_recognition` for listening to the user's commands, `pyttsx3` for text-to-speech functionality, and `wikipedia` and `webbrowser` to fetch information and open websites based on the user's input.

## Features

- **Voice Commands:**
  - Greet the user with "hello".
  - Search Wikipedia for a specific topic.
  - Open websites based on user input.
  - Provide the current time and date.
  - Exit the assistant with a "goodbye" or "exit" command.

## Requirements

Before running the assistant, make sure you have the following Python packages installed:

- `speech_recognition`
- `pyttsx3`
- `wikipedia`
- `webbrowser` (part of Python standard library)
- `datetime` (part of Python standard library)

You can install the necessary packages using `pip`:

```bash
pip install speechrecognition pyttsx3 wikipedia
