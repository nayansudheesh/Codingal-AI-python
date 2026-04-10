import config
from huggingface_hub import InferenceClient


MODELS = getattr(config, "HF_MODELS" , ["meta-llama/Llama-3.1-8B-instruct"])

def generate_response(prompt: str , temperature: float = 0.3, max_tokens : int = 512) -> str:    
    key = getattr(config, "HF_API_KEY", None)
    if not key:
        return "Error: HF_API_KEY missing in config.py"
    c = InferenceClient(token=key)
    last_err = None
    for m in MODELS:
        try:
            r = c.chat_completion(messages=[{"role" : "user" , "content" : prompt}] , model = m , temperature = temperature , max_tokens = max_tokens)\
            
            return r.choices[0].message.content
        
        except Exception as e:
            last_err = e
    return (
        "HF model failed"
        f"Tried models: {MODELS}"
    )