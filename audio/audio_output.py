
from groq import Groq
from pathlib import Path
import os
import subprocess

client = Groq()
def speak(text:str):
    speech_file_path = Path(__file__).parent / "speech.wav"
    response = client.audio.speech.create(
    model="playai-tts",
    voice="Fritz-PlayAI",
    response_format="wav",
    input=text,
)
    response.write_to_file(speech_file_path)
    subprocess.run(["aplay", str(speech_file_path)])