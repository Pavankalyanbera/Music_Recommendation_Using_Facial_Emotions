from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import*
from keras.models import load_model
from time import sleep
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import webbrowser as wb
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
import tkinter
from tkinter import *
from django.http import JsonResponse
from .gui import *


# Create your views here.

def Home(request):
	return render(request,"Home.html",{})

def Registeration(request):
	if request.method == "POST":
		name = request.POST['fname']
		username = request.POST['username']
		password = request.POST['password']
		age = request.POST['age']
		phone = request.POST['phone']

		obj = userDetails(
							Name=name
							,Username=username
							,Passsword=password
							,age=age
							,phonenumber=phone
			)
		obj.save()
		messages.info(request,name +' Registered')
		return redirect('/User_Login')
	else:
		return render(request,"Registeration.html",{})

def Login(request):
	return render(request,"Login.html",{})

def Demo(request):
	return render(request,"Demo.html",{})

def User_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if userDetails.objects.filter(Username=C_name, Passsword=C_password).exists():
			users = userDetails.objects.all().filter(Username=C_name, Passsword=C_password)
			messages.info(request,C_name +' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'User'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			# request.session['username'] = Username
			return redirect("/")
		else:
			messages.info(request, 'Please Register')
			return redirect("/Registeration")
	else:
		return render(request,'User_Login.html',{})

def Admin_Login(request):
	if request.method == "POST":
		A_username = request.POST['username']
		A_password = request.POST['password']
		if admin_details.objects.filter(aname=A_username,apass=A_password ).exists():
			ad = admin_details.objects.get(aname=A_username,apass=A_password )
			messages.info(request,A_username+ ' login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
			return render(request, "Admin_Login.html", {})
	else:
		return render(request, "Admin_Login.html", {})


def Detection(request):
	return render(request,"Detection.html",{})

def Detect(request):
	face_classifier = cv2.CascadeClassifier('C:/WORKSPACE/Project/Final/Music_Recommendation_System/Music_Recommendation_System/Music_App/haarcascade_frontalface_default.xml')
	classifier =load_model('C:/WORKSPACE/Project/Final/Music_Recommendation_System/Music_Recommendation_System/Music_App/Emotion_Detection.h5')

	class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

	cap = cv2.VideoCapture(0)
	while True:
	    # Grab a single frame of video
	    ret, frame = cap.read()
	    labels = []
	    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	    faces = face_classifier.detectMultiScale(gray,1.3,5)

	    for (x,y,w,h) in faces:
	        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	        roi_gray = gray[y:y+h,x:x+w]
	        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)


	        if np.sum([roi_gray])!=0:
	            roi = roi_gray.astype('float')/255.0
	            roi = img_to_array(roi)
	            roi = np.expand_dims(roi,axis=0)

	        # make a prediction on the ROI, then lookup the class

	            preds = classifier.predict(roi)[0]
	            print("\nprediction = ",preds)
	            label=class_labels[preds.argmax()]
	            print("\nprediction max = ",preds.argmax())
	            print("\nlabel = ",label)
	            label_position = (x,y)
	            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)

	        else:
	            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
	        print("\n\n")
	    cv2.imshow('Emotion Detector',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	wb.open(f"https://www.youtube.com/results?search_query=song+{label}")
	cap.release()
	cv2.destroyAllWindows()
	return render(request,"Home.html",{})





class Message(View):

	def post(self, request):
		msg = request.POST.get('text')
		response = chatbot_response(msg)
		print(response)
		valid=validators.url(response)
		if valid==True:
			data1 = 'True'
			data = {
			'respond': response,'respond1':data1
			}
			return JsonResponse(data)
		else:
			data1 = 'False'
			data = {
			'respond': response,'respond1':data1
			}
			return JsonResponse(data)
		

		#return HttpResponse('data')


	def clean_up_sentence(sentence):
		sentence_words = nltk.word_tokenize(sentence)
		sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
		return sentence_words

	def bow(sentence, words, show_details=True):
		sentence_words = clean_up_sentence(sentence)
		bag = [0] * len(words)
		for s in sentence_words:
			for i, w in enumerate(words):
				if w == s:
					bag[i] = 1
					if show_details:
						print("found in bag: %s" % w)
		return (np.array(bag))


	def predict_class(sentence, model):
		p = bow(sentence, words, show_details=False)
		print(p)
		res = model.predict(np.array([p]))[0]
		print(res)
		ERROR_THRESHOLD = 0.25
		results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
		results.sort(key=lambda x: x[1], reverse=True)
		return_list = []
		for r in results:
			return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
		return return_list

	def getResponse(ints, intents_json):
		tag = ints[0]['intent']
		list_of_intents = intents_json['intents']
		for i in list_of_intents:
			if (i['tag'] == tag):
				result = random.choice(i['responses'])
				print(result)
				break
		return result

	def chatbot_response(msg):
		ints = predict_class(msg, model)
		res = getResponse(ints, intents)
		print(res)
		return res

		
	   
	 
def ChatWindow(request):
	return render(request,'ChatWindow.html',{})

def View_User(request):
	details = userDetails.objects.all()
	return render(request,"View_User.html",{'details':details})

def Logout(request):
	Session.objects.all().delete()
	return redirect('/')

	





	



