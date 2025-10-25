from google import genai
import docx
import os
from dotenv import load_dotenv

def instructor_chatbot():
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
        prompt = f"""
        **Context:**
        You are an expert HR Co-Pilot. Your task is to analyze the following CV and provide a comprehensive, factual summary for a busy hiring manager.

        **CV Text:**
        {cv_text}

        ---

    **Positive Instructions (What to do):**
    1.  Analyze the provided CV Text.
    2.  Structure your output *exactly* according to the "Analysis Report" template below.
    3.  Be concise, factual, and professional.
    4.  Extract information *only* from the text.
    5.  Calculate total *relevant* experience based on the roles listed.
    6.  Identify key *technical* skills (like languages, frameworks, software) and *soft* skills (like leadership, communication) that are *explicitly mentioned* or *strongly implied* by job descriptions.
    7.  Identify potential red flags, such as significant employment gaps (over 6 months) or frequent job changes (e.g., multiple roles under 1 year).

    **Negative Instructions (What to AVOID):**
    1.  **DO NOT** use subjective or overly enthusiastic language (e.g., "amazing candidate," "perfect fit," "highly recommend"). Stick to factual analysis.
    2.  **DO NOT** invent or infer skills, experiences, or qualifications that are not present in the CV.
    3.  **DO NOT** include personal, non-professional information (e.g., hobbies, marital status, home address) even if it's in the CV. Only extract Name, Email, and Phone.
    4.  **DO NOT** provide a summary or opinion *outside* of the requested structure.
    5.  **DO NOT** write long narrative paragraphs. Use bullet points as shown in the template.

    ---

    **Analysis Report Template (Follow this structure exactly):**

    **1. Candidate Profile:**
    * **Name:** [Extract Name]
    * **Contact:** [Extract Email and Phone]
    * **Executive Summary:** [Write a 2-3 sentence summary of the candidate's professional profile and apparent seniority level (e.g., Junior, Mid-Level, Senior).]

    **2. Experience Analysis:**
    * **Total Years of Experience:** [Calculate total years of relevant experience, e.g., "Approximately 7.5 years"]
    * **Recent Role:** [Extract the most recent Job Title and Company]

    **3. Skills Matrix:**
    * **Technical Skills:** [List 5-7 key programming languages, software, or technical frameworks.]
    * **Soft Skills:** [List 3-5 key soft skills (e.g., "Team Leadership", "Agile Methodologies", "Client Communication").]

    **4. Red Flags (If Any):**
    * [List any potential red flags. If none, state "No significant red flags detected."]
    """

        print("===================================")
        print("=== PROMPT SENT TO API ===")
        print("===================================")
        print(prompt) 
        print("===================================")
        print("=== WAITING FOR RESPONSE... ===")
        print("===================================")

    # Call API and Print
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
    
        print("\n===================================")
        print("=== RESULTING ANALYSIS ===")
        print("===================================")
        print(response.text)
        print("===================================")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instructor_chatbot()