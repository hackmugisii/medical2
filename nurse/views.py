from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .tensorflow_bot import generate_bot_response
from django.contrib.auth import login, authenticate

def chat_view(request):
    chat_history = Chat.objects.all().order_by('time')

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save() #save message to database
            user_message = form.cleaned_data['message'] #user's message
            bot_response = generate_bot_response(user_message) #bots response
            Chat.objects.create(message=str(bot_response))
            return redirect('chatroom')
    else:
        form = ChatForm()
    
    return render(request, 'chatroom.html', {'form':form, 'chat_history':chat_history})

def register_view(request):
    if request.method == 'POST':
        registerform = NewUserForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect('profile')
    else:
        registerform = NewUserForm()

    return render(request, 'account.html', {'registerform':registerform})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatroom')
    else:
        return render(request, 'account.html')
    
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile_view = Profile, student = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profform = ProfileForm(request.POST)
        if profform.is_valid():
            profform.save()
            return redirect('profile')
    else:
        profform = ProfileForm()

    return render(request, 'profile.html', {'profile_view':profile_view, 'profform':profform})
