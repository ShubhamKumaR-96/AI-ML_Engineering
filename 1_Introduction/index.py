from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv("OPEN_AI_KEY")

client = genai.Client(api_key=OPENAI_KEY)

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
