from robots.models import Robot 
from forms import RobotForm
from forms import EditForm
from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    robot_list = Robot.objects.all().order_by("-Date")
    return render(request,'robots.html', {'robots': robot_list})

def all(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    else:    
	    return render(request,'robots_all.html',
							 {'robots': Robot.objects.all()})

def single(request, robot_id=1):
	return render(request,'robot_single.html',
							 {'robot': Robot.objects.get(id=robot_id)})

def create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.POST:
        form = RobotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/robots')
    else:
        form = RobotForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request,'create_robot.html', args)

@csrf_exempt
def edit(request, robot_id=1):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
        
    robot_no = Robot.objects.get(id=robot_id)  
    if request.POST:
        form = EditForm(request.POST, request.FILES, instance=robot_no)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/robots')
    else: 
        form = EditForm(instance=robot_no)
    
    return render(request,'edit_robot.html',
                             {'form': form, 'robot': Robot.objects.get(id=robot_id)})
