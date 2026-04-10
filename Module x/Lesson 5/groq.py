import config
from openai import OpenAI

GROQ__URL = "https://api.groq.com/openai/v1/"

MODELS = getattr(config, "GROQ_MODELS" , ["llama-3.1-8b-instant" , "mixtral-8x7b32768"])

def generate_response(prompt: str , temperature: float = 0.3, max_tokens : int = 512) -> str:

    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_KEY missing in config.py"
    c = OpenAI(api_key=key , base_url=GROQ__URL)

    last_err = None

    for m in MODELS:
        try:
            r = c.chat.completions.create(
                model  = m
                messages= [{"role" : "user" , "content" : prompt}]
                temperature = temperature,
                max_tokens=max_tokens
            )
        except Exception as e:
            last_err = e
        
    return (
            "GROQ model failed"
            f"Tried models: {MODELS}"
        )