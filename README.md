# Music_Recommendation_Using_Facial_Emotions
CPSC 597 Project

# About :

The project focuses on developing a system that recommends music based on the user's facial expressions detected in real-time. The system uses Convolutional Neural Networks (CNN) to identify emotions such as happiness, sadness, anger, surprise, and neutrality, and then suggests a playlist of songs that align with the detected emotion.

# Installation Instruction:


1.	Environment Setup Install Python and Django: pip install django 	
3.	Set Up Django Project Create a new Django project if not already done: django-admin start project _project name Navigate into project directory: cd project_name
4.	 Django Application Setup Create a new Django app for handling the video violence detection: bash Copy code python manage.py startapp 
5.	Configure Django to Use the Model Ensure views.py in the facial_emotion_detection app is set up to handle connections between the frontend and the model predictions. 
6.	Database Setup Install MySQL and phpMyAdmin: Depending on your OS, use the appropriate package manager or download from the website Configure Django to use MySQL by updating DATABASES in settings.py. 
7.	Model Training Run the Jupyter notebook to train the model using the dataset. Adjust the path to the dataset in your notebook accordingly. Save the trained model locally to integrate with Django.
8.	Running the Server Start the Django development server: bash Copy code python manage.py runserver. 
9.	Test the Application Access the application through the browser at http://127.0.0.1:8000/ to test video processing and facial emotion functionalities. 
These steps will get your Django-based application running with a trained machine learning model and database integration.
