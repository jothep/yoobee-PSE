from google import genai
import docx
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
client = genai.Client()
cv_text = ""

DOCX_FILE_PATH = r"/Users/zhuxiang/Documents/Xiang-Zhu-CV-11:Sep:2025.docx"

try:
    if not os.path.exists(DOCX_FILE_PATH):
        raise FileNotFoundError(f"Error: The file '{DOCX_FILE_PATH}' was not found.")

    doc = docx.Document(DOCX_FILE_PATH)
    all_paras = [para.text for para in doc.paragraphs] # Get text from each paragraph
    cv_text = "\n".join(all_paras) # Join all paragraphs into one string

    if not cv_text.strip():
        print("Error: The .docx file is empty or contains no readable text.")
        exit()

    # Prompt
    prompt = prompt = f"""
You are an expert HR Co-Pilot. Your task is to analyze the following CV and provide a comprehensive summary for a busy hiring manager.

**CV Text:**
{cv_text}

---
**Analysis Report:**

**1. Candidate Profile:**
* **Name:** [Extract Name]
* **Contact:** [Extract Email and Phone]
* **Executive Summary:** [Write a 3-sentence summary of the candidate's entire professional profile and apparent seniority level (e.g., Junior, Mid-Level, Senior).]

**2. Experience Analysis:**
* **Total Years of Experience:** [Calculate the total years of relevant experience, e.g., "Approximately 7.5 years"]
* **Recent Role:** [Extract the most recent Job Title and Company]

**3. Skills Matrix:**
* **Technical Skills:** [List 5-7 key programming languages, software, or technical frameworks.]
* **Soft Skills:** [List 3-5 key soft skills (e.g., "Team Leadership", "Agile Methodologies", "Client Communication").]

**4. Red Flags (If Any):**
* [List any potential red flags, such as significant employment gaps, job hopping, or lack of clear achievements. If none, state "No significant red flags detected."]
"""

    # Call API and Print
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    print("--- CV Summary ---")
    print(response.text)
    print("------------------")

except Exception as e:
    print(f"An error occurred: {e}")