from django.shortcuts import render,redirect
from huayuan import models
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
import pymysql
import json
# Create your views here.
def index(request):
    conn = pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
    cur = conn.cursor()
    sql = 'SELECT  Humidity,Temperature FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    Temperature = []
    for data in datas:
        id.append(data[0])
        Temperature.append(data[1])


    dict={
        'id':json.dumps(id),
        'Temperature':json.dumps(Temperature)
    }

    sql = 'SELECT  Humidity,avg FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    soil_Avg = []
    for data in datas:
        id.append(data[0])
        soil_Avg.append(data[1])

    dict = {
        'ids': json.dumps(id),
        'Illumination': json.dumps(soil_Avg)
    }
    sql = 'SELECT  Humidity,Illumination FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    Illumination = []
    for data in datas:
        id.append(data[0])
        Illumination.append(data[1])

    dict = {
        'ids': json.dumps(id),
        'Illumination': json.dumps(Illumination)
    }
    user=request.session['username']
    return render(request, 'index.html',{"id":id,"Temperature":Temperature,'ids':id,'soil_Avg':soil_Avg,'ids':id,'Illumination':Illumination,'user':user})
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        useremail = request.POST.get('email','')
        password = request.POST.get('password','')
        password2 = request.POST.get('reviewpassword','')
        if username=='':
            messege='用户名不为空'
        elif useremail=='':
            messege = '邮箱不为空'
        elif password=='':
            messege = '密码不为空'
        else:
            if password == password2:
                models.userRegister.objects.create(username=username,useremail=useremail,password=password)
                return HttpResponseRedirect('/login/')
            else:
                messege = '两次密码不一致'
                # return render(request, 'register.html', {'messege': messege})
        return render(request,'register.html',{'messege':messege})

        # else:
        #     if password == password2:
        #         models.userRegister.objects.create(username=username,useremail=useremail,password=password)
        #         messege = '用户注册成功'
        #         return  render(request,'login.html',{'messege':messege})
        #     else:
        #         messege='两次密码不一致'
        #         return render(request,'register.html',{'messege':messege})
    return render(request,'register.html')

def login(request):
    if request.session.get('is_login',None):
        return  redirect('/index/')
    if request.method == 'POST':
        yonghuname = request.POST.get('yonghu')
        password = request.POST.get('password')
        user=auth.authenticate(request,yonghu=yonghuname,password=password)
        if yonghuname and password is not None:
            yonghuname=yonghuname.strip()
            try:
                user=models.userRegister.objects.get(useremail=yonghuname)
            except:
                message='用户不存在'
                return render(request,'login.html',{'message':message})
            if user.password == password:
                request.session['useremail'] = user.useremail
                request.session['username'] = user.username
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
def jsdaoru(request):
    pass
    # conn=pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
    # cur = conn.cursor()
    # sql = 'SELECT  Humidity,Temperature FROM test'
    # cur.execute(sql)
    # datas = cur.fetchall()
    # jsonData={}
    # id = []
    # Temperature = []
    # for data in datas:
    #     id.append(data[0])
    #     Temperature.append(data[1])
    # return render(request,'login.html',{'id':id,'Temperature':Temperature})
    # jsonData['id'] = id
    # jsonData['Temperature'] = Temperature
    # Temperature = json.dump(jsonData)
    # cur.close()
    # conn.close()
    # wheelsList = models.userRegister.objects.all()
    # name = list(models.userRegister.objects.values_list('name',flat=True))
    # data = list(models.userRegister.objects.values_list('trackid',flat=True))
    # return render(request,'index.html',{'Temperature':Temperature})