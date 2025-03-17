
# import requests

# def check_similarity(student_answer, teacher_answer):
#     API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
#     headers = {"Authorization": "Bearer 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"}

#     data = {
#         "inputs": {
#             "source_sentence": student_answer,
#             "sentences": [teacher_answer]
#         }
#     }

#     response = requests.post(API_URL, headers=headers, json=data)
#     if 'error' in response.json():
#         print("Error:", response.json()['error'])
#         return None
#     return response.json()[0]


# # Example Usage
# student_answer = "The earth revolves around the sun."
# teacher_answer = "The planet orbits the sun."

# score = check_similarity(student_answer, teacher_answer)

# if score > 0.8:
#     print("✅ Fully Correct Answer")
# elif score > 0.5:
#     print("⚡ Partially Correct Answer")
# else:
#     print("❌ Wrong Answer")


# from sentence_transformers import SentenceTransformer, util

# # Load the model locally (No need for API)
# model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# def check_similarity(student_answer, teacher_answer):
#     embeddings = model.encode([student_answer, teacher_answer])
#     similarity_score = util.cos_sim(embeddings[0], embeddings[1])
#     return similarity_score.item()

# # Example Usage
# student_answer = "The earth revolves around the sun."
# teacher_answer = "The planet orbits the sun."

# score = check_similarity(student_answer, teacher_answer)

# if score > 0.8:
#     print("✅ Fully Correct Answer")
# elif score > 0.5:
#     print("⚡ Partially Correct Answer")
# else:
#     print("❌ Wrong Answer")


import requests
import json
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}

def check_similarity(student_answer, teacher_answer):
    data = {
        "inputs": {
            "source_sentence": student_answer,
            "sentences": [teacher_answer]
        }
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()[0]  # Returns similarity score
    else:
        print("Error:", response.json())
        return None

# Example Usage
student_answer = "The earth revolves around the sun."
teacher_answer = "The planet orbits the sun."

score = check_similarity(student_answer, teacher_answer)

if score:
    if score > 0.8:
        print("✅ Fully Correct Answer")
    elif score > 0.5:
        print("⚡ Partially Correct Answer")
    else:
        print("❌ Wrong Answer")
