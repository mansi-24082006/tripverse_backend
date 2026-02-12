import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Warning: GEMINI_API_KEY not found in environment variables.")

def generate_itinerary(source, destination, days, vibe, budget, people):
    """
    Generates a travel itinerary using Google Gemini.
    """
    if not GEMINI_API_KEY:
        return "Travel itinerary generation is currently unavailable. Please check API configuration."

    prompt = f"""
    Create a detailed travel itinerary for a trip:
    - From: {source}
    - To: {destination}
    - Duration: {days} days
    - Vibe: {vibe}
    - Budget: {budget}
    - Number of People: {people}

    Please provide a day-by-day plan including:
    - Sightseeing locations
    - Suggested activities
    - Local food recommendations
    - Travel tips for this specific destination

    Format the response clearly with headings for each day.
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating itinerary: {e}")
        return f"Sorry, I couldn't generate your itinerary at this moment. Error: {str(e)}"
