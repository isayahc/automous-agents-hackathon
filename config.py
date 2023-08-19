import os
import elevenlabs
import dotenv

dotenv.load_dotenv()

ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


elevenlabs.set_api_key(ELEVENLABS_API_KEY)




