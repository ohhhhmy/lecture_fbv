from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm, SignupForm
from django.http import HttpResponse
from django.template import RequestContext #무엇?


# Create your views here.


# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username = request.POST['username'],
#                 password = request.POST['password1']
#             )
#             nickname = request.POST['nickname']
#             profile = Profile(user = user, nickname = nickname)
#             profile.save()
#             auth.login(request, user)
#             return redirect('lectureList')
#     return render(request, 'signup.html')

    
# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username = username, password = password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('lectureList')
#         else:
#             return render(request, 'login.html', {'error' : 'ID나 패스워드 오류!'})
#     else:
#         return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('lectureList')
    

def loginform(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('lectureList')
        else:
            return HttpResponse('아이디 혹은 패스워드 오류')
        
    else:
        form = LoginForm()
        return render(request, 'loginform.html', {'form' : form})


def signupform(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
            user = User.objects.create_user(username = request.POST['username'],
            password = request.POST['confirm_password'])
            nickname = request.POST['nickname']

            profile = Profile(user = user, nickname = nickname)
            profile.save()
            auth.login(request, user)
            return redirect('lectureList')
        else:
            return HttpResponse('비밀번호 불일치!')
    else:
        form = SignupForm() # get 방식은 form 제공
        return render(request, 'signupform.html', {'form' : form})
        
