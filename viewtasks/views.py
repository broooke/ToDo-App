from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, TaskCompleted
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth import login as dj_login


# Create your views here.

def home(request):
	tasks = Task.objects.all()
	tasks_completed = TaskCompleted.objects.all()
	form = TaskForm()
	if request.method=='POST':
	 	form = TaskForm(request.POST)
	 	if form.is_valid():
	 		form.save()
	 	return redirect('/')
	for task in tasks:
		if  task.complete==True:
			task_complete = TaskCompleted(title_completed=task.title)
			task.delete()
			task_complete.save()
			return redirect('/')
	# try:
	#  	for i in tasks:
	#  		if i.complete==True:
	#  			a.append(i.title)
	# except Exception as e:
	#  	return redirect('/')

	dictionary = {'tasks':tasks, 'form':form, 'tasks_completed': tasks_completed}
	return render(request,'home.html', dictionary)

def update(request, task_id):
	task = Task.objects.get(id=task_id)
	form = TaskForm(instance=task)
	if request.method=='POST':
	 	form = TaskForm(request.POST, instance=task)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('/')

	dictionary = {'task':task, 'form':form}
	return render(request, 'update.html', dictionary)

def delete(request,task_id):
	task = Task.objects.get(id=task_id)
	task.delete()
	return redirect('/')

def deletecompleted(request,task_id):
	task = TaskCompleted.objects.get(id=task_id)
	task.delete()
	return redirect('/')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = SignUpForm()

	dictionary = {'form':form}
	return render(request, 'signup.html', dictionary)

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				dj_login(request, user)
				return redirect('/')
			else:
				messages.add_message(request, messages.INFO, 'Hello world.')
	else:
		form = AuthenticationForm()
			
	return render(request, 'login.html')

def loginout(request):
	logout(request)
	return HttpResponseRedirect('/login/')






# def add(request):
# 	task = Task(title=request.POST['add'])
# 	task.save()
# 	return HttpResponseRedirect('../')



