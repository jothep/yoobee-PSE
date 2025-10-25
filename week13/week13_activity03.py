import os
from google import genai
from google.genai import types 
from dotenv import load_dotenv

def instructor_chatbot():
    # Load the API key from a .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        print("Please create a .env file and add your API key, e.g.:")
        print("GEMINI_API_KEY='your_api_key_here'")
        return

    try:
        # Client automatically finds the GEMINI_API_KEY from the environment
        client = genai.Client()
    except Exception as e:
        print(f"Error initializing API client: {e}")
        return

    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    # Construct a cleaner, more direct prompt for Gemini
    prompt = f"""
    **Context:**
    You are 'Chris', a professional, friendly tourist recommender and AI Itinerary expert. 
    Your task is to provide a high-quality itinerary based on the user's data.

    **User Details:**
    - Duration: {days} days
    - Destination: {location}
    - Traveler's Age: {age} years

    ---

    **Positive Instructions (What to do):**
    1.  Start your response with a friendly, brief greeting.
    2.  Give a structured itinerary, with each day listed separately (e.g., "Day 1: [Theme]").
    3.  Provide a maximum of two (2) activities per day to keep it simple.
    4.  Keep all descriptions very short (1-2 sentences).
    5.  Suggest activities appropriate for the traveler's age.

    **Negative Instructions (What to AVOID):**
    1.  **DO NOT** recommend more than 2 activities per day.
    2.  **DO NOT** write long paragraphs or introductions. Be concise.
    3.  **DO NOT** use overly formal or robotic language. Be friendly (like 'Chris').
    4.  **DO NOT** include specific street addresses. General areas (e.g., "Downtown", "Old Quarter") are fine.
    5.  **DO NOT** suggest activities clearly unsuitable for the traveler's age (e.g., no intense clubs for a 15-year-old, no extreme sports for an 80-year-old).
    
    ---
    
    **Itinerary Plan:**
    """
    
    # <-- 2. Configure generation settings as an object
    generation_config_obj = types.GenerateContentConfig(
        temperature=0.8,
        max_output_tokens=4096,
    )

    try:
        # Use the dedicated 'generate_content_stream' method
        # Pass the object to the 'config' parameter
        response = client.models.generate_content_stream( 
            model='gemini-2.5-flash',
            contents=prompt,
            config=generation_config_obj 
        )

        print("\nHere is your itinerary from Chris:\n")
        
        # Iterate through the streamed chunks
        for chunk in response:
            if chunk.text:
                print(chunk.text, end='', flush=True)
        
        print("\n")

    except Exception as e:
        print(f"\nError communicating with Gemini API: {e}")

if __name__ == "__main__":
    instructor_chatbot()