# to install the required libraries, run the following command in your terminal:
# pip install flask google-genai
# to insll dotenv, run the following command in your terminal:
# pip install python-dotenv
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

# Define different personalities for the Study Assistant
personalities = {
  "Friendly": "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding.",
  "Academic": "You are a strictly academic, highly detailed, and professional university Professor. Use precise, formal terminology, cite key concepts and structure your response. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding."
}

# Initialize the GenAI client with the API key
client = genai.Client(api_key = apiKey)


# Function to generate a response from the Study Assistant based on the user's question and selected persona    
def study_assistance(question, persona):

  system_prompt = personalities[persona]

  # Generate a response from the model using the system prompt and user question
  response = client.models.generate_content(
      model = "gemini-2.5-flash",
      # Configure the generation settings such as temperature and max output tokens
      config = types.GenerateContentConfig(
          system_instruction = system_prompt,
          temperature = 1.9,
          max_output_tokens = 2000
      ),
        
      contents = question
  )
  return response

question = "explain about LLM"
persona = "Friendly"
output = study_assistance(question, persona)
print(output.text)

""" 
system_prompt => is the instruction that guides the model's behavior and
response style. It sets the context for how the model should generate its
output based on the user's question and the selected persona.

temperature => is a parameter that controls the randomness of the model's output.
ranges from 0 to 2.
- A lower temperature (e.g., 0.2) will make the output more focused and deterministic, often resulting in more conservative responses.
- A higher temperature (e.g., 1.0 or above) will make the output more diverse and creative, allowing for more varied responses.
In the context of a Study Assistant, a higher temperature can encourage the model to provide more engaging and less predictable explanations, which can be beneficial for keeping the user interested and providing a wider range of examples and analogies.
"""


