# Text-To-Speech-in-Indian-Languages
Implementation of Text to Speech in English, along with 5 frequently used Indian Languages (Bengali, Gujarati, Hindi, Kannada, Tamil) in a webpage (using Django Rest Framework).

The whole world is going digital. Money transfers from one bank account to another, creating a bank account, online shopping, online tutorial classes are only few of the numerous services that a common man can use it to their fullest advantage. But of what purpose is it, if the end user is not able to read the text written in English on the webpage, simply because the person doesn't know to read or understand English. This project aims to tackle this very issue, by translating the contents of the page in the selected language. It also has a text to speech feature, where the browser speaks in the selected language.

## Setup instructions:

1. Download repository
2. Open terminal, move to multilang_TTS/ and run the command
   #### pip install -r requirements.txt
   to install the following packages:
   
   gtts  
   playsound  
   django  
   djangorestframework  
   django-cors-headers  
   
3. Then run this command:
   #### python manage.py runserver
   
4. Once the server is active, run http:127.0.0.1/8000/tts to see the magic.

## Demo Video
[![SC2 Video](https://img.youtube.com/vi/5wniPnHfq-U/0.jpg)](http://www.youtube.com/watch?v=5wniPnHfq-U)
