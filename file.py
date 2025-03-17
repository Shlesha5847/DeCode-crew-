import easyocr
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Step 1: Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Load English OCR model

# Step 2: Read text from image
results = reader.readtext('imp2.jpg')  # Replace with your image path

# Extract text from OCR results
extracted_text = " ".join([res[1] for res in results])

print("OCR Extracted Text:", extracted_text)

# Step 3: Load Transformer Model for Post-Processing
tokenizer = T5Tokenizer.from_pretrained("t5-small")  # Using T5-small for text correction
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Prepare input for T5 model
input_text = "fix spelling: " + extracted_text
tokens = tokenizer(input_text, return_tensors="pt")

# Generate corrected text
output = model.generate(**tokens)
corrected_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Corrected Text:", corrected_text)


