from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
import os


import traceback
from openai import OpenAI
client = OpenAI(
  api_key="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"
)

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # change this if GPT-4 is not accessible
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
        )
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ OpenAI Exception:", str(e))
        return "Sorry, I'm having trouble reaching OpenAI right now."

def chatbot(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(user=request.user)
    else:
        chats = []

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        message = request.POST.get('message', '').strip()
        if not message:
            return JsonResponse({'error': 'Empty message'}, status=400)

        response = ask_openai(message)

        Chat.objects.create(
            user=request.user,
            message=message,
            response=response,
            created_at=timezone.now()
        )
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            auth.login(request, user)
            return redirect('chatbot')
        except:
            return render(request, 'register.html', {'error_message': 'Error creating account'})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
