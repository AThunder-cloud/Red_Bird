from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Post
from django.db.models import Q 
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm , GenreForm
# Create your views here.


def registerPage(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			login(request,user)
			return redirect('index')
		else:
			messages.error(request,'An error occured during registration')
	return render(request,'login_register.html',{'form':form})

def loginPage(request):
	page = 'login' # login  is a prebulid function 
	if request.user.is_authenticated:
		return redirect('index')
	if request.method=='POST':
		username=request.POST.get('username').lower()
		password=request.POST.get('password')

		try:
			user= User.objects.get(username=username)
		except:
			messages.error(request,'User Does Not Exits')
		user = authenticate(request, username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			messages.error(request,'Username and Password does not exist')
	context={'page': page}
	return render(request,'user-account.html' , context)

def logoutUser(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('index')
	else:
		messages.info(request, 'User is not loged in')
		return redirect('index')


def index(request):
	posts = Post.objects.all()
	images = Post.objects.only('image')
	context = {
	'posts' : posts,
	'images': images
	}
	return render(request,'index.html',context)

def profile(request,pk):
    uprofile = Profile.object.get(id=pk)
    if request.method == 'POST':
        None

def post(request):
	posts = Post.objects.all()
	images = Post.objects.only('image')
	context = {
	'posts' : posts,
	'images': images
	}
	return render(request, 'post-body.html',context)

def create_post(request):
	form = PostForm() 
	genre = GenreForm()
	if request.method  == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/')
	context = {
		"form" : form
	}
	return render(request, 'create-post.html', context)

# def create_post(request):
# 	if request.method == "POST":
# 		body = Post.objects.create(
#         post_title=request.POST.get('post_title'),
#         text_body=request.POST.get('creating_text')
#         )
# 		if body.is_valid():
# 			post.save()
# 			return redirect('index.html')
# 		return redirect('create-post.html')
# 	return render(request, 'create-post.html')

# def delete(request,pk):
# 	post = Post.objects.get(id=pk)
# 	if request.method == 'POST':
# 		post.delete()
# 		return redirect('index')
# 	return render(request,'delete.html',{'obj': post})

def delete(request):
	object_id = request.POST.get('object_id')
	post = Post.objects.get(pk = object_id)
	Post.delete()
	return redirect('index')