import requests
import warnings
import re
import easyocr
from spellchecker import SpellChecker

warnings.filterwarnings("ignore")  # Suppress warnings

# ✅ Step 1: Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Load English OCR model

# ✅ Step 2: Read text from image
image_path = 'Numbersimg.jpg'  # Replace with your image path
results = reader.readtext(image_path)

# ✅ Extract text from OCR results
extracted_text = " ".join([res[1] for res in results])
print("OCR Extracted Text:", extracted_text)

# ✅ Step 3: Spell Correction
spell = SpellChecker()
def correct_word(word):
    """Correct only words containing only alphabets, keep numbers and symbols unchanged."""
    return spell.correction(word) if re.match(r'^[a-zA-Z]+$', word) else word
words = extracted_text.split()
corrected_text = " ".join([correct_word(word) for word in words])
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

