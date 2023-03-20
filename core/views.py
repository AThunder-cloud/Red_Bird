from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Post, Genre, Like, Followers, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
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
                user = User.objects.create_user(
                    first_name=fname, 
                    last_name=lname, 
                    username=username, 
                    email=email, 
                    password=password
                    )
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
	posts = Post.objects.filter()
	images = Post.objects.only('image')
	context = {
	'posts' : posts,
	'images': images
	}
	return render(request,'index.html',context)

def user_profile(request, pk):
	user = User.objects.get(id=pk)
	posts = Post.objects.filter(author= user.profile)
	context={
		'user':user,
		'posts':posts,
	}
	return render(request, 'profile.html',context)

def post(request):
	posts = Post.objects.all()
	images = Post.objects.only('image')
	context = {
	'posts' : posts,
	'images': images
	}
	return render(request, 'feed.html',context)

def create_post(request):
	if request.method  == "POST":
		title = request.POST.get('title')
		post_body = request.POST.get('post-body')
		image = request.FILES.get('image')
		genre_ids = request.POST.getlist('genres')

		#Creating a post instance 
		post = Post.objects.create(
			author = request.user.profile,
			post_title = title,
			text_body = post_body,
			image = image
		)
		# Adding genre to the post instance
		genres = Genre.objects.filter(id__in=genre_ids)
		post.genres.set(genres)

		return redirect('index')
	# Rendering template for GET requests
	genres = Genre.objects.all()
	return render(request, 'create-post.html',{'genres':genres})      

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


def like_post(request):
	username = request.user.username
	post_id = request.GET.get("post_id")
	post = get_object_or_404(Post, id=post_id)
	like = Like.objects.filter(post_id=post_id, username=username).first()

	if like == None:
		new_like = Like.objects.create(post_id=post_id, username=username)
		new_like.save()
		post.no_likes += 1
		post.save()
		return redirect('/')
	else:
		like.delete()
		post.no_likes -= 1
		post.save()
		return redirect('/')

@csrf_exempt
def post_page(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	content={
		"post":post,
	}
	return render(request, 'test2.html', content)