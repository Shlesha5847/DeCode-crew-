# import requests
# import warnings
# warnings.filterwarnings("ignore")  # Suppress warnings

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logs

# from spellchecker import SpellChecker 

# import re 
# import easyocr
# from transformers import T5ForConditionalGeneration, T5Tokenizer

# # Step 1: Initialize EasyOCR reader
# reader = easyocr.Reader(['en'])  # Load English OCR model

# # Step 2: Read text from image
# results = reader.readtext('Testing2.jpg')  # Replace with your image path

# # Extract text from OCR results
# extracted_text = " ".join([res[1] for res in results])

# print("OCR Extracted Text:", extracted_text)


# spell = SpellChecker()

# words = extracted_text.split()

# # Correct each word
# corrected_text = " ".join([spell.correction(word) or word for word in words])


# print("Corrected Text:", corrected_text)




# # ✅ Replace with your Together.AI API key
# api_token = "7506956744a893835fdbee84f30bb286fe52b9aabf987fd5666fca9be91b56e4"

# # ✅ Together.AI API endpoint
# API_URL = "https://api.together.xyz/v1/chat/completions"  # ✅ Correct


# # ✅ Headers for API authentication
# headers = {
#     "Authorization": f"Bearer {api_token}",
#     "Content-Type": "application/json"
# }

# # ✅ Teacher's Correct Answer
# correct_answer = """
# Stack is a data structure works on FIFO (First in First Out). Stack is used in paranthesis checking.
# """

# # ✅ Student's Answer
# student_answer = corrected_text

# # ✅ Message Structure for LLaMA
# messages = [
#     {
#         "role": "system",
#         "content": "You are an AI-powered Grading Assistant. Compare the student's answer with the correct answer logically and semantically."
#     },
#     {
#         #  users prompt to ai
#         "role": "user",
#         "content": f"""
#         Compare the student's answer with the correct answer.

#         📌 *Teacher's Answer:* {correct_answer}  
#         📌 *Student's Answer:* {student_answer}  
#         Your prompt should only contain : 
#         1️⃣ Give a *similarity percentage* (how much the student's answer matches the correct answer).  
#         2️⃣ Assign a *grade out of 10* based on similarity.  
#         3️⃣ Provide *feedback* on what was correct and what needs improvement.  
#         4️⃣ List any *key points the student missed*.   
#         Return your response in *JSON format*:
#         {{"similarity_percentage": "XX%", "grade": "X/10", "feedback": "Your detailed feedback here...", "missing_points": "List of key points..."}}
#         """
#     }
# ]

# # ✅ Payload for LLaMA API
# payload = {
#     "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
#     "messages": messages,
#     "temperature": 0.7,
#     "max_tokens": 1000,
# }

# # ✅ Send request
# response = requests.post(API_URL, headers=headers, json=payload)

# # ✅ Handle response
# # ✅ Handle response
# if response.status_code == 200:
#     result = response.json()
#     ai_response = result["choices"][0]["message"]["content"]
    
#     # ✅ Remove <think>...</think> block and extra spaces
#     ai_response = re.sub(r"<think>.*?</think>", "", ai_response, flags=re.DOTALL).strip()
#     ai_response = ai_response.replace("\n\n", "\n").strip()  # Remove extra newlines

#     print("\n🔹 AI Grading Response:")
#     print(ai_response)

# else:
#     print("❌ API Error:", response.text)







# if response.status_code == 200:
#     result = response.json()
#     ai_response = result["choices"][0]["message"]["content"]
    
#     # ✅ Remove <think>...</think> block and extra spaces
#     ai_response = re.sub(r"<think>.*?</think>", "", ai_response, flags=re.DOTALL).strip()
#     ai_response = ai_response.replace("\n\n", "\n").strip()  # Remove extra newlines

#     # ✅ Convert JSON string to dictionary
#     import json
#     try:
#         json_start = ai_response.find("{")
#         json_end = ai_response.rfind("}") + 1
#         ai_json_str = ai_response[json_start:json_end]  # Extract JSON part
#         ai_response_json = json.loads(ai_json_str)  # Parse JSON

#         # ✅ Pretty-print JSON output
#         print("\n🔹 AI Grading Report:")
#         print(f"📊 *Similarity Percentage:* {ai_response_json['similarity_percentage']}")
#         print(f"🎯 *Grade:* {ai_response_json['grade']}")
#         print(f"💡 *Feedback:* {ai_response_json['feedback']}")
#         print(f"❗ *Missing Points:* {ai_response_json['missing_points']}")

#     except Exception as e:
#         print("❌ Error parsing AI response:", e)
#         print("🔹 Raw AI Response:\n", ai_response)
# else:
#     print("❌ API Error:", response.text)




import requests
import warnings
import re
import easyocr
from spellchecker import SpellChecker

warnings.filterwarnings("ignore")  # Suppress warnings

# ✅ Step 1: Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Load English OCR model

# ✅ Step 2: Read text from image
image_path = 'Testing2.jpg'  # Replace with your image path
results = reader.readtext(image_path)

# ✅ Extract text from OCR results
extracted_text = " ".join([res[1] for res in results])
print("OCR Extracted Text:", extracted_text)

# ✅ Step 3: Spell Correction
spell = SpellChecker()
words = extracted_text.split()
corrected_text = " ".join([spell.correction(word) or word for word in words])
print("Corrected Text:", corrected_text)

# ✅ Step 4: Configure Google Gemini API
GEMINI_API_KEY = "AIzaSyBO7EU1gsy7kGKSeTyfBEKZPlvdRDCAIT0"  # Replace with your API key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# ✅ Teacher's Correct Answer
correct_answer = """
Stack is a data structure that works on LIFO (Last In First Out). Stack is used in parenthesis checking.
"""

# ✅ Student's Answer (from OCR and spell correction)
student_answer = corrected_text

# ✅ Gemini Prompt for Evaluation
payload = {
    "contents": [{
        "parts": [{
            "text": f"""
            You are an AI-powered Grading Assistant. Compare the student's answer with the correct answer logically and semantically.

            📌 *Teacher's Answer:* {correct_answer}  
            📌 *Student's Answer:* {student_answer}  

            Your response should include:
            1️⃣ Give a *similarity percentage* (how much the student's answer matches the correct answer).  
            2️⃣ Assign a *grade out of 10* based on similarity.  
            3️⃣ Provide *feedback* on what was correct and what needs improvement.  
            4️⃣ List any *key points the student missed*.   

            Return your response in *JSON format*:
            {{
              "similarity_percentage": "XX%", 
              "grade": "X/10", 
              "feedback": "Your detailed feedback here...", 
              "missing_points": "List of key points..."
            }}
            """
        }]
    }]
}

# ✅ Headers for API request
headers = {
    "Content-Type": "application/json"
}

# ✅ Send the request to Gemini API
response = requests.post(API_URL, headers=headers, json=payload)

# ✅ Process API Response
if response.status_code == 200:
    result = response.json()
    
    if "candidates" in result and result["candidates"]:
        ai_response = result["candidates"][0]["content"]["parts"][0]["text"]
        ai_response = re.sub(r"<think>.*?</think>", "", ai_response, flags=re.DOTALL).strip()
        print("\n🔹 AI Grading Response:")
        print(ai_response)
    else:
        print("❌ API Error: No valid response received.")

else:
    print("❌ API Error:", response.text)

