# Create a simple bot with gemini model

from dotenv import load_dotenv
load_dotenv()
import os
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

from google import genai
client= genai.Client()
#prompt = 'who are you?'

while(True):
   prompt = input('user: ')
   if prompt == 'exit':
        break
   response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[prompt]
    )
#while(True):
#    prompt = input('user: ')
##    if prompt == 'exit':
##        break
#    response = client.models.generate_content(
#        model='gemini-2.5-flash',
#        contents=[prompt]
#    )
   print(response.text)
 


