from django.shortcuts import render
from django.http import JsonResponse
from .ai_modules import education_ai, medical_ai, games_ai, personal_ai,tech_ai,finance_ai,cooking_ai,legal_ai,fitness_ai,travel_ai
 

def home(request):
    return render(request, 'ai/home.html')

def education_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Education AI', 'endpoint': 'education/chat'})  

def medical_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Medical AI', 'endpoint': 'medical/chat'})   

def games_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Games AI', 'endpoint': 'games/chat'})   

def personal_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Personal AI', 'endpoint': 'personal/chat'})   

def tech_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Tech AI', 'endpoint': 'tech/chat'})  

def finance_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Finace AI', 'endpoint': 'finance/chat'})\

def cooking_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Cooking AI', 'endpoint': 'cooking/chat'})

def legal_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Legal AI', 'endpoint': 'legal/chat'})    

def fitness_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Fitness AI', 'endpoint': 'fitness/chat'})

def travel_ai_view(request):
    return render(request, 'ai/chat.html', {'ai_type': 'Travel AI', 'endpoint': 'travel/chat'})    


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

def tech_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = tech_ai.process(user_message)
    return JsonResponse({'response': response})

def finance_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = finance_ai.process(user_message)
    return JsonResponse({'response': response})

def cooking_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = cooking_ai.process(user_message)
    return JsonResponse({'response': response})

def legal_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = legal_ai.process(user_message)
    return JsonResponse({'response': response})

def fitness_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = fitness_ai.process(user_message)
    return JsonResponse({'response': response})

def travel_ai_chat(request):
    user_message = request.GET.get('message', '')
    response = travel_ai.process(user_message)
    return JsonResponse({'response': response})