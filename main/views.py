from blog.models import Article
from robots.models import Robot
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib import auth
from forms import RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    article_list = Article.objects.all().order_by("-Date")
    robot_list = Robot.objects.all().order_by("-Date")
    return render(request,'index.html', {'articles': article_list, 'robots': robot_list})

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user')
    c = {}
    c.update(csrf(request))    
    return render(request,'login.html', c)

def invalid(request):  
    return render(request,'invalid.html')

def user_area(request):
    c = {}
    c.update(csrf(request))    
    return render(request,'user_area.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/user')
    else:
        return HttpResponseRedirect('/invalid')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        
    else:
        form = RegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request,'register.html', args)    

