import requests

# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = 'API_KEY'
endpoint = "https://api.openai.com/v1/moderations"

# The data you want to check for moderation
data = {
    "input": "The text you want to analyze for potentially unsafe content."
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(endpoint, json=data, headers=headers)

if response.status_code == 200:
    print("Moderation API call was successful.")
    print("Response:", response.json())
else:
    print(f"Failed to call Moderation API. Status code: {response.status_code}")
    print("Response:", response.json())
