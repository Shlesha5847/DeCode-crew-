import requests
import warnings
import re
import easyocr
from spellchecker import SpellChecker

warnings.filterwarnings("ignore")  


reader = easyocr.Reader(['en'])  


image_path = 'Testing2.jpg' 
results = reader.readtext(image_path)


extracted_text = " ".join([res[1] for res in results])
print("OCR Extracted Text:", extracted_text)

spell = SpellChecker()
def correct_word(word):
    """Correct only words containing only alphabets, keep numbers and symbols unchanged."""
    return spell.correction(word) if re.match(r'^[a-zA-Z]+$', word) else word
words = extracted_text.split()
corrected_text = " ".join([correct_word(word) for word in words])
print("Corrected Text:", corrected_text)
GEMINI_API_KEY = "AIzaSyBO7EU1gsy7kGKSeTyfBEKZPlvdRDCAIT0" 
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

correct_answer = """
Stack is a data structure that works on LIFO (Last In First Out). Stack is used in parenthesis checking.
"""
student_answer = corrected_text

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
headers = {
    "Content-Type": "application/json"
}
response = requests.post(API_URL, headers=headers, json=payload)

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

