from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Post
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm , GenreForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cpassword']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('index')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.error(request,'Password not matching')
			redirect('/loginPage')
	return render(request,'signin.html')

def signout(request):
	if request.user.is_authenticated:
		auth.logout(request)
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
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user.profile
			post.save()
			return redirect('index')
		else:
			form = PostForm()
	return render(request, 'create-post.html', {'form':form})

@csrf_exempt
def delete(request, item_id):
	print('deleting......')
	post = get_object_or_404(Post, id=item_id)
	if request.method == 'POST':
		post.delete()
		return JsonResponse({'success':True}) 
	return JsonResponse({"success":False})

def profile(request):
	return render(request, 'profile.html')