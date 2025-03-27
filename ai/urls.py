from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('medical/', views.medical_ai_view, name='medical_ai'),
    path('education/', views.education_ai_view, name='education_ai'),
    path('games/', views.games_ai_view, name='games_ai'),
    path('personal/', views.personal_ai_view, name='personal_ai'),
    path('tech/', views.tech_ai_view, name='tech_ai'),
    path('finance/', views.finance_ai_view, name='finance_ai'),
    path('cooking/', views.cooking_ai_view, name='cooking_ai'),
    path('legal/', views.legal_ai_view, name='legal_ai'),
    path('fitness/', views.fitness_ai_view, name='fitness_ai'),
    path('travel/', views.travel_ai_view, name='travel_ai'),
    path('fitness/chat/', views.fitness_ai_chat, name='fitness_ai_chat'),
    path('travel/chat/', views.travel_ai_chat, name='travel_ai_chat'),
    path('legal/chat/', views.legal_ai_chat, name='legal_ai_chat'),
    path('cooking/chat/', views.cooking_ai_chat, name='cooking_ai_chat'),
    path('finance/chat/', views.finance_ai_chat, name='finance_ai_chat'),
    path('tech/chat/', views.tech_ai_chat, name='tech_ai_chat'),
    path('education/chat/', views.education_ai_chat, name='education_ai_chat'),
    path('medical/chat/', views.medical_ai_chat, name='medical_ai_chat'),
    path('games/chat/', views.games_ai_chat, name='games_ai_chat'),
    path('personal/chat/', views.personal_ai_chat, name='personal_ai_chat'),
]
