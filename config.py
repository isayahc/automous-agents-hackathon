import os
import elevenlabs
import dotenv
import openai

dotenv.load_dotenv()

ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


elevenlabs.set_api_key(ELEVENLABS_API_KEY)
openai.api_key = OPENAI_API_KEY




