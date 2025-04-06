# AI-Powered Grading Assistant

This project is an AI-powered grading assistant that evaluates students' answers by extracting text from images using Optical Character Recognition (OCR), performing spell correction, and comparing the extracted text to a model answer using the Google Gemini API.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Configuration](#api-configuration)
- [Contributing](#contributing)


## Project Overview

The AI-Powered Grading Assistant automates the evaluation of handwritten or printed student responses. It processes an image of the student's answer, extracts the text using OCR, corrects any spelling errors, and then assesses the content by comparing it to a predefined correct answer. The evaluation provides a similarity percentage, a grade out of 10, detailed feedback, and highlights any key points that were missed.

## Features

- **OCR Processing**: Extracts text from images using EasyOCR.
- **Spell Correction**: Corrects spelling errors in the extracted text.
- **Answer Evaluation**: Compares the student's answer to the correct answer using the Google Gemini API.
- **Detailed Feedback**: Provides similarity percentage, grade, feedback, and lists missing key points.

## Technologies Used

- Python
- EasyOCR
- SpellChecker
- Google Gemini API
- Requests library

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ai-grading-assistant.git
   cd ai-grading-assistant
2. Create a Virtual Environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
3. Install Required Packages:
pip install -r requirements.txt
Ensure your requirements.txt includes:

easyocr
requests
pyspellchecker

4. Obtain Google Gemini API Key:

Visit the Google Cloud Console.
Create a new project or select an existing one.
Navigate to the API & Services > Credentials.
Generate a new API key.
Enable the Google Gemini API for your project.
 
4. Usage
    1. Place the Student's Answer Image:

            Save the image of the student's answer in the project directory. Update the image_path variable in the script to point to this image.

    2. Run the Script:

            python Project.py
            The script will process the image, perform OCR, correct spelling errors, and evaluate the answer. The results will be displayed in the console.

5. API Configuration
In the script, set your Google Gemini API key:

GEMINI_API_KEY = "your_api_key_here"
Replace "your_api_key_here" with the API key obtained from the Google Cloud Console.

5. Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.