from django.shortcuts import render,redirect
from huayuan import models
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        pass
    return render(request, 'register.html')


def login(request):
    if request.method == 'POSt':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=auth.ayuthenticate(request,email=email,password=password)
        if email and password is not None:
            email=email.strip()
            try:
                email=models.User.Objects.get(email=email)
            except:
                message='用户不存在'
                return render(request,'login.html',{'message':message})
            if user.password == password:
                return redirect('/index/')
            else:
                message = '登录密码错误'
                return  render(request,'login.html',{'message':message})
    return render(request, 'login.html')


def aleats(request):
    return render(request, 'alerts.html')


def blank(request):
    return render(request, 'blank.html')


def buttons(request):
    return render(request, 'buttons.html')


def cards(request):
    return render(request, 'cards.html')


def chartjs(request):
    return render(request, 'chartjs.html')


def invoice(request):
    return render(request, 'invoice.html')


def modal(request):
    return render(request, 'modals.html')


def pepei(request):
    return render(request, 'pepei.html')

def progress_bars(request):

    return render(request, 'progress_bars.html')

def ren(request):

    return render(request, 'ren.html')

def rizhi(request):

    return render(request, 'rizhi.html')

def settings(request):

    return render(request, 'settings.html')

def tabs(request):

    return render(request, 'tabs.html')

def user(request):

    return render(request, 'user.html')

def zhi(request):

    return render(request, 'zhi.html')

def zhiwuzhonglei(request):

    return render(request, 'zhiwuzhonglei.html')
