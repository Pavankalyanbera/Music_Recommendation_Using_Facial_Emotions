from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from Music_App.views import Message

urlpatterns = [
					path('',views.Home,name="Home"),
					path('Registeration/',views.Registeration,name="Registeration"),
					path('Login/',views.Login,name="Login"),
					path('Demo/',views.Demo,name="Demo"),
					path('User_Login/',views.User_Login,name="User_Login"),
					path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
					path('Detection/',views.Detection,name="Detection"),
					path('Detect/',views.Detect,name="Detect"),
					#path('Chatbot/',views.Chatbot,name="Chatbot"),
					path('Logout/',views.Logout,name="Logout"),
					path('View_User/',views.View_User,name="View_User"),
					path('Message/', Message.as_view(),name='Message'),
					path('ChatWindow/',views.ChatWindow,name="ChatWindow"),
					
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)