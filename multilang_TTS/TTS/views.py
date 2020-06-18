from django.shortcuts import render
from rest_framework.decorators import api_view 
from TTS.speak import speech

# Create your views here. 
@api_view(["GET"])
def tts(request):
	print(request.__class__)
	
	if request.is_ajax:
		print("AJAX request")
	else:
		print("Not AJAX request")
	print(request.query_params)
	text_list = request.query_params.getlist('text_list[]')
	print("Text list: ",text_list)

	sentence = ' '.join(text_list)
	print("Full text: ", sentence)
	lang = request.query_params.get('lang')
	print("lang: ",lang)
	if lang is not None and sentence!='':
		speech(sentence,lang)
	return render(request, "translate_speech_to_text.html")

