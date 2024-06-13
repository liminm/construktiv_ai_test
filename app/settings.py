import os
from os.path import join, dirname
from dotenv import load_dotenv


api_key_path = join(dirname(dirname(__file__)), '.env')
system_prompt_path = join(dirname(dirname(__file__)), 'prompts.env')
load_dotenv(api_key_path)
load_dotenv(system_prompt_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
print(OPENAI_API_KEY)
MAX_TOTAL_TOKENS = int(os.environ.get("MAX_TOTAL_TOKENS"))
SYSTEM_PROMPT = os.environ.get("SYSTEM_PROMPT")
