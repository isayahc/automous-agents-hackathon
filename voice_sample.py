from elevenlabs import voices, generate, set_api_key
import os


ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
set_api_key(ELEVENLABS_API_KEY)
voices = voices()
audio = generate(text="Hello there!", voice=voices[0])

print(voices)