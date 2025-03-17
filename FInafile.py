import requests

# ✅ Replace with your Together.AI API key
api_token = "7506956744a893835fdbee84f30bb286fe52b9aabf987fd5666fca9be91b56e4"

# ✅ Together.AI API endpoint
API_URL = "https://api.together.xyz/v1/chat/completions"  # ✅ Correct


# ✅ Headers for API authentication
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# ✅ Teacher's Correct Answer
correct_answer = """
Delhi is Capital Of India 
"""

# ✅ Student's Answer
student_answer = """
Pune is Capital of India
"""

# ✅ Message Structure for LLaMA
messages = [
    {
        "role": "system",
        "content": "You are an AI-powered Grading Assistant. Compare the student's answer with the correct answer logically and semantically."
    },
    {
        "role": "user",
        "content": f"""
        Compare the student's answer with the correct answer.

        📌 **Teacher's Answer:** {correct_answer}  
        📌 **Student's Answer:** {student_answer}  

        1️⃣ Give a **similarity percentage** (how much the student's answer matches the correct answer).  
        2️⃣ Assign a **grade out of 10** based on similarity.  
        3️⃣ Provide **feedback** on what was correct and what needs improvement.  
        4️⃣ List any **key points the student missed**.  

        Return your response in **JSON format**:
        {{"similarity_percentage": "XX%", "grade": "X/10", "feedback": "Your detailed feedback here...", "missing_points": "List of key points..."}}
        """
    }
]

# ✅ Payload for LLaMA API
payload = {
    "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    "messages": messages,
    "temperature": 0.7,
    "max_tokens": 300,
}

# ✅ Send request
response = requests.post(API_URL, headers=headers, json=payload)

# ✅ Handle response
if response.status_code == 200:
    result = response.json()
    ai_response = result["choices"][0]["message"]["content"]
    
    print("\n🔹 AI Grading Response:")
    print(ai_response)

else:
    print("❌ API Error:", response.text)