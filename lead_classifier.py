import requests
import os

ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

def classify_lead(lead,research):

    prompt = f"""
Classify this lead as HOT, WARM, or COLD.

Lead:
{lead}

Company research:
{research}
"""

    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": ANTHROPIC_KEY,
        "anthropic-version": "2023-06-01",
        "content-type":"application/json"
    }

    data = {
        "model":"claude-3-sonnet-20240229",
        "max_tokens":500,
        "messages":[{"role":"user","content":prompt}]
    }

    r = requests.post(url,json=data,headers=headers)

    return r.json()
