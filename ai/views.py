from django.shortcuts import render
from django.http import JsonResponse
from .ai_modules import education_ai, medical_ai, games_ai, personal_ai

from django.http import JsonResponse
  # Import the correct AI module
 

def home(request):
    return render(request, 'ai/home.html')

def education_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Education AI', 'endpoint': 'education/chat'})  # ✅ Corrected

def medical_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Medical AI', 'endpoint': 'medical/chat'})  # ✅ Corrected

def games_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Games AI', 'endpoint': 'games/chat'})  # ✅ Corrected

def personal_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Personal AI', 'endpoint': 'personal/chat'})  # ✅ Corrected

# AI API Chat Endpoints
def education_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = education_ai.process(user_message)
    return JsonResponse({'response': response})

def medical_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = medical_ai.process(user_message)
    return JsonResponse({'response': response})

def games_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = games_ai.process(user_message)
    return JsonResponse({'response': response})

def personal_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = personal_ai.process(user_message)
    return JsonResponse({'response': response})
