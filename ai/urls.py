from django.urls import path
from . import views

 
urlpatterns = [
    path('', views.home, name='home'),
    path('medical/', views.medical_ai_view, name='medical_ai'),
    path('education/', views.education_ai_view, name='education_ai'),
    path('games/', views.games_ai_view, name='games_ai'),
    path('personal/', views.personal_ai_view, name='personal_ai'),
    path('education/chat/', views.education_ai_chat, name='education_ai_chat'),
    path('medical/chat/', views.medical_ai_chat, name='medical_ai_chat'),
    path('games/chat/', views.games_ai_chat, name='games_ai_chat'),
    path('personal/chat/', views.personal_ai_chat, name='personal_ai_chat'),
]
 