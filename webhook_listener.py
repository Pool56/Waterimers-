from flask import Flask, request
from agents.lead_classifier import classify_lead
from integrations.perplexity_lookup import research_company

app = Flask(__name__)

@app.route("/lead",methods=["POST"])
def lead():

    data = request.json

    company = data["company"]

    research = research_company(company)

    score = classify_lead(data,research)

    return {"lead_score":score}

if __name__ == "__main__":
    app.run(port=5000)
