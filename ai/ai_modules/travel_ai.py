import requests

GROQ_API_KEY = "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"

def process(query):
    prompt = f"""
    You are Travel AI. You suggest destinations, itineraries, and travel tips. 
    If a question is not about travel, respond with: 'I can only help with travel-related questions.'
    
    User: {query}
    AI: 
    """

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "llama3-8b-8192",  
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "AI did not respond.")
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"

