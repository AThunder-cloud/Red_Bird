from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Post, Genre, Like, Followers, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q
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
			messages.error(request,'Username & Password not matching')
			redirect('/loginPage')
	return render(request,'signin.html')

@login_required(login_url="signin")
def signout(request):
	if request.user.is_authenticated:
		auth.logout(request)
		return redirect('index')
	else:
		messages.info(request, 'User is not loged in')
		return redirect('index')

def index(request):
	if request.method == "GET":
		q = request.GET.get('q', '') 
	posts = Post.objects.filter(
		Q(post_title__icontains=q) |
		Q(genres__name__icontains=q) |
		Q(author__user__username__icontains=q) 
	).distinct()
	images = Post.objects.only('image')
	profiles = Profile.objects.filter(
		Q(user__username__icontains=q) |
		Q(user__first_name__icontains=q) |
		Q(user__last_name__icontains=q)
		).distinct()
	context = {
	'posts' : posts,
	'images': images,
	'profiles' :profiles,
	}
	return render(request,'index.html',context)

@login_required(login_url="signin")
def user_profile(request, pk):
	user = User.objects.get(id=pk)
	posts = Post.objects.filter(author= user.profile)
	context={
		'user':user,
		'posts':posts,
	}
	return render(request, 'profile.html',context)

def post(request):
	if request.method == "GET":
		q = request.GET.get('q', '') 
	posts = Post.objects.filter(
		Q(post_title__icontains=q) |
		Q(genres__name__icontains=q) |
		Q(author__user__username__icontains=q) 
	).distinct()
	# posts =Post.objects.all()
	images = Post.objects.only('image')
	context = {
	'posts' : posts,
	'images': images
	}
	return render(request, 'feed.html',context)

@login_required(login_url="signin")
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

@login_required(login_url="signin")
def like_post(request):
	username = request.user.username
	post_id = request.POST.get("post_id")
	post = get_object_or_404(Post, id=post_id)
	like = Like.objects.filter(post_id=post_id, username=username).first()

	if like == None:
		new_like = Like.objects.create(post_id=post_id, username=username)
		new_like.save()
		post.no_likes += 1
		post.save()
		return JsonResponse({"liked":True})
	else:
		like.delete()
		post.no_likes -= 1
		post.save()
		return JsonResponse({"liked":False})
		
@login_required(login_url="signin")
def post_page(request, post_id):
	if request.method == "GET":
		q = request.GET.get('q', '') 
	posts = Post.objects.filter(
		Q(post_title__icontains=q) |
		Q(genres__name__icontains=q) |
		Q(author__user__username__icontains=q) 
	).distinct()
	post = get_object_or_404(Post, id=post_id)
	comments = post.comments.all()
	username = request.user.username
	like = Like.objects.filter(post_id=post_id, username=username).first()
	if like == None:
		is_liked = False
	else:
		is_liked = True
	context = {
		"post":post,
		"posts" : posts,
		"comments":comments,
		"is_liked": is_liked
		}
	return render(request,'main.html',context)

def profile_list(request):
	if request.method == "GET":
		q = request.GET.get('q', '')
	profiles = Profile.objects.filter(
		Q(user__username__icontains=q) |
		Q(user__first_name__icontains=q) |
		Q(user__last_name__icontains=q)
	).distinct()
	context={'profiles':profiles}
	return render(request, 'test.html' , context)

@login_required
def add_comment(request):
	if request.method == 'POST':
		post_id = request.POST.get("post_id")
		postobj = get_object_or_404(Post, id=post_id)
		text = request.POST.get('comment')
		user = request.user
		post = postobj
		comment = Comment.objects.create(user=user, post=post, text=text)
		postobj.no_comments += 1
		postobj.save()
		return redirect('postpage', post_id=post_id)
	else:
		return render(request, 'main.html', {'post_id': post_id})

@login_required
def delete_comment(request, item_id):
	comment = Comment.objects.get(id=item_id)
	print(comment)
	if request.user != comment.user:
		return HttpResponse('You cannot delete this comment !!')

	else:
		post_id = comment.post.id
		post = get_object_or_404(Post, id=post_id)
		post.no_comments -= 1
		post.save()
		comment.delete()
		return redirect('postpage', post_id=post_id)

@login_required
def edit_profile(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	if request.method == 'POST':
		fname = request.POST.get('first_name')
		lname = request.POST.get('last_name')
		location = request.POST.get('location')
		email = request.POST.get('email')
		bio = request.POST.get('bio')
		if User.objects.filter(email=email).exists() and user.email != email:
			messages.info(request, 'Email address already taken')
		else:
			profile.profile_img = request.FILES.get('profile_image', profile.profile_img)
			user.first_name = fname
			user.last_name = lname 
			profile.location = location
			user.email = email
			profile.bio = bio

			user.save()
			profile.save()
			return redirect('profile',pk=request.user.id)
	return render(request, 'edit-profile.html',{'profile' : profile})