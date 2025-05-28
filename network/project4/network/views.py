import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.defaultfilters import pluralize

from .models import User, Post, Follow, Like

def following(request):
    followings = Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
    all_posts = Post.objects.filter(author__in=followings).order_by('-timestamp')

    paginator = Paginator(all_posts, 10)
    post_num = request.GET.get('page')
    posts = paginator.get_page(post_num)
    likes = Like.objects.filter(post__in=all_posts).values_list('post_id', flat=True)

    return render(request, "network/following.html", {
        'likes': likes,
        'posts': posts,
    })

    

def profile(request, profileid):
    if request.method == 'POST':
        target_user = User(id=profileid)
        current_user = request.user

        if target_user.id == current_user.id:
                return redirect('profile', current_user.id)

        follow_relationship = Follow.objects.filter(follower=current_user, following=target_user).first()

        if follow_relationship:
            follow_relationship.delete()
            return redirect('profile', target_user.id)
        else:
            Follow.objects.create(follower=current_user, following=target_user)
            return redirect('profile', target_user.id)
    else:
        profile_user = User.objects.get(pk=profileid)
        follower = Follow.objects.filter(following=profile_user).count()
        following = Follow.objects.filter(follower=profile_user).count()
        isFollow = False
        if request.user.is_authenticated and profile_user != request.user:
            isFollow = Follow.objects.filter(follower=request.user, following=profile_user).exists()
        

        all_posts = Post.objects.filter(author=profile_user).order_by('-timestamp')
        paginator = Paginator(all_posts, 10)
        post_num = request.GET.get('page')
        posts = paginator.get_page(post_num)
        likes = Like.objects.filter(post__in=all_posts).values_list('post_id', flat=True)

        return render(request, "network/profile.html", {
            'profile_user': profile_user,
            'follower': follower,
            'following': following,
            'isFollow': isFollow,
            'posts': posts,
            'likes': likes,
        })

def post(request, postid):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required."}, status=403)

    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=postid)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found."}, status=404)

        if post.author != request.user:
            return JsonResponse({"error": "Permission denied."}, status=403)

        data = json.loads(request.body)
        content = data.get('content')
        post.content = content
        post.save()
        return JsonResponse({"done": "true"}, status=200)
    

def like(request, postid):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required."}, status=403)

    if request.method == 'GET':
        post = Post.objects.get(pk=postid)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return JsonResponse({
                "done": "false",
                "like": f"{post.likes.count()} like{pluralize(post.likes.count())}"
            }, status=200)
        else:
            Like.objects.create(user=request.user, post=post)
            return JsonResponse({
                "done": "true",
                "like": f"{post.likes.count()} like{pluralize(post.likes.count())}"
            }, status=200)

def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        content = request.POST['content']
        Post.objects.create(content=content, author=request.user)
        return redirect('index')

    else:
        all_posts = Post.objects.all().order_by('-timestamp')
        paginator = Paginator(all_posts, 10)
        post_number = request.GET.get('page')
        posts = paginator.get_page(post_number)
        likes = []
        if request.user.is_authenticated:
            likes = Like.objects.filter(post__in=all_posts).values_list('post_id', flat=True)

        return render(request, "network/index.html", {
            'likes': likes,
            'posts': posts,
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")