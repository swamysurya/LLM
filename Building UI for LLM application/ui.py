import gradio as gr

import os
# import necessary libraries and modules
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
  return response.text


demo = gr.Interface(
    fn = study_assistance,
    # inputs order should be mached with function arguments
    inputs = [
        gr.Textbox(label="Enter your question", lines=4, placeholder="Ask me anything about your studies!"),
        gr.Radio(choices = list(personalities.keys()), label = "Select a persona", value = "Friendly")
    ],
    outputs=gr.Textbox(label="Study Assistant's Response", lines = 10),
    title = "smart Study Assistant",
    description = "Ask any study-related question and get a helpful response from our AI-powered Study Assistant. Select a persona to customize the style of the response!"
)
# to get public url use share=True in lauch method
demo.launch(debug=True, share=True)

"""
gradio => is an open-source Python library that allows you to quickly create
and share web-based interfaces for machine learning models. 
It provides a simple and intuitive way to build interactive applications without needing extensive web development knowledge.
With Gradio, you can create user-friendly interfaces for your models, making it easier for users to interact with them and visualize the results.

gradio provide a special class called interface which is used to 
quicky create a demo for your function.


"""
