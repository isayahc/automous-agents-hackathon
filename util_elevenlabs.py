import os
import wave
from elevenlabs import generate, play, set_api_key, voices
import dotenv

dotenv.load_dotenv()
ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
set_api_key(ELEVENLABS_API_KEY)
voices() # must be called in order to activate custom trained voices


def play_audio(audio):
    play(audio)

def save_as_wav(audio, filename):
    with wave.open(filename, "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes (16 bits)
        wav_file.setframerate(44100)  # 44.1 kHz
        wav_file.writeframes(audio)

def speak(text, voice="Doctor G"):
    # print(voices())
    set_api_key(ELEVENLABS_API_KEY)
    audio = generate(text=text, voice=voice)
    play_audio(audio)

def speak_bytes(text, voice="Doctor G"):
    audio = generate(text=text, voice=voice)
    return audio

def speak_to_file(text, filename, voice="Doctor G"):
    audio = generate(text=text, voice=voice)
    save_as_wav(audio, filename)

def main():
    text = "Hello world!"
    filename = "./assets/output.wav"
    voice = "Doctor G"
    set_api_key(ELEVENLABS_API_KEY)

    # Example 1: Using speak
    print("Example 1: Using speak")
    speak(text, voice)

    # Example 2: Using speak_bytes
    print("Example 2: Using speak_bytes")
    audio = speak_bytes(text, voice)
    print(f"Generated audio: {audio}")

    # Example 3: Using speak_to_file
    print("Example 3: Using speak_to_file")
    speak_to_file(text, filename, voice)
    print(f'Audio saved to "{filename}"')

if __name__ == "__main__":
    main()
