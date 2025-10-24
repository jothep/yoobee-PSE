import os
from google import genai
from google.genai import types  # <-- 1. ADD THIS IMPORT
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
    You are 'Chris', a professional tourist recommender and AI Itinerary expert. 
    Your task is to provide a detailed, high-quality itinerary recommendation based on the user's data.

    User Details:
    - Duration: {days} days
    - Destination: {location}
    - Traveler's Age: {age} years

    Instructions:
    1.  Start your response with a friendly greeting.
    2.  Give a structured itinerary, with each day listed separately (e.g., "Day 1: [Theme]").
    3.  Provide a maximum of three (3) activities per day.
    4.  For each activity, include:
        - The name of the place.
        - The address (if a specific address is relevant, otherwise the general area).
        - A short, helpful description.
    """
    
    # <-- 2. Configure generation settings as an object, not a dict
    generation_config_obj = types.GenerateContentConfig(
        temperature=0.8,
        max_output_tokens=4096,
    )

    try:
        # <-- 3. THIS IS THE CORRECTED CALL
        # Use the dedicated 'generate_content_stream' method
        # Pass the object to the 'config' parameter
        response = client.models.generate_content_stream( 
            model='gemini-2.5-flash',
            contents=prompt,
            config=generation_config_obj  # <-- Use 'config' not 'generation_config'
        )

        print("\nHere is your itinerary from Chris:\n")
        
        # Iterate through the streamed chunks
        for chunk in response:
            if chunk.text:
                print(chunk.text, end='', flush=True)
        
        print("\n") # Add a final newline for clean formatting

    except Exception as e:
        print(f"\nError communicating with Gemini API: {e}")

if __name__ == "__main__":
    instructor_chatbot()