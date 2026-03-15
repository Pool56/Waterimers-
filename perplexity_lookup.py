import requests
import os

API = os.getenv("PERPLEXITY_API")

def research_company(company):

    payload = {
        "model":"pplx-70b-online",
        "messages":[
            {"role":"user","content":f"Tell me about the company {company}"}
        ]
    }

    headers = {
        "Authorization":f"Bearer {API}",
        "Content-Type":"application/json"
    }

    r = requests.post(
        "https://api.perplexity.ai/chat/completions",
        json=payload,
        headers=headers
    )

    return r.json()
