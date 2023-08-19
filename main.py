from  util_elevenlabs import speak, speak_bytes, speak_to_file
from elevenlabs import set_api_key
import elevenlabs
import os
import dotenv

dotenv.load_dotenv()


ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

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