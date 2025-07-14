from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

class IntentExtractor:
    with open("audio/transcripts/D_14-07-2025_T_12-28-16.txt", "r", encoding="utf-8") as file:
        text = file.read()
    def __init__(self, text: str):
        self.text = text
    def extract_intent(self)->str:
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction='''
                                    You are an intent and entity extraction assistant designed to help a hospital appointment booking voice bot. 
                                    The bot receives transcribed user speech (in Hindi-English mix), and your job is to extract useful structured data.

                                    Use the transcription provided below to fill in the required fields. Return only a valid JSON object with keys exactly as shown, and `null` if data is missing.

                                    ---

                                    🎯 Your goal: 
                                    From the given transcription, extract:

                                    {
                                    "intent": "book_appointment / cancel_appointment / inquire_availability / get_doctor_info / greet / other",
                                    "hospital": "Name of the hospital if mentioned, else null",
                                    "department": "Relevant department (e.g., cardiology, neurology), else null",
                                    "doctor": "Full name of doctor if mentioned, else null",
                                    "day": "Name of the day (e.g., Monday), resolved from words like kal (tomorrow), aaj (today), etc.",
                                    "date": "Exact date in YYYY-MM-DD format, resolved from terms like 'tomorrow', 'next Friday' or any specific date",
                                    "time": "Appointment time or time window if mentioned (e.g., 3 PM, morning, afternoon), else null",
                                    "patient_name": "Name of the patient, if user says 'mera naam Ravi hai' or 'for my father', else null",
                                    "self_diagnosis": "What problem user is facing or what they mention they need help with (e.g., fever, chest pain), else null"
                                    }

                                    ---

                                    🧠 Instructions:
                                    - Keep values in **plain text** or `null` (not "none", not "missing", not empty string).
                                    - Do **not add extra keys** outside the ones listed above.
                                    - If the transcription contains unrelated chit-chat, still return the JSON, but with `"intent": "other"` and all other values as null.

                                    ---
                                    '''),
            contents=self.text
        )

        print(response.text)
