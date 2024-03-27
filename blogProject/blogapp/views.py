from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import createPostForm

# Create your views here.

# ----The views receives http request from or to client
# The view is aka Controller
# ----Then there will be Query sets to the models in models.py
# When model sends back the data, the views sends the data to the templates (html, css & JS pages)


# The controller gives us an interface to define all routes for our application
# ---/home, /about

# django provides us with an ORM that uses QuerySet manager that allows us to interact eith our tables in database with the functions:
# nameofdtbase.objects.create() ---- 
# nameofdtbase.objects.get() --------same as 
# nameofdtbase.objects.filter() -----same as WHERE in SQL
# nameofdtbase.objects.count() -----same as WHERE in SQL
# by deafult every view function it takes an object known as request
# and returns a page(through render)

# list of all the posts
@login_required
def post_list(request):
    posts = Post.objects.all()
    # this line queries the database returns all instances of the Post Model

    return render(request, 'blog/post/list.html', {'posts':posts})

@login_required
def post_view(request, id):
    post = Post.objects.get(id = id)

    return render(request, 'blog/post_detail.html', {'post': post, 'value':24})


@login_required
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                # return HttpResponse('You have successfully logged in')
                return redirect(reverse('blogapp:post_list'))
            else:
                return HttpResponse('user does not exist')
    else:
        form=LoginForm()
        return render(request, 'blog/login.html', {'form': form})

# after succesful login, the user is stored in a session

def CreatAPost(request):
    if request.method == 'POST':
        form = createPostForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            post = Post.objects.create(
                
                    title = cleaned_form['title'],
                    slug= cleaned_form['slug'],
                    body= cleaned_form['body'],               
                 
            )
            post.user = request.user
            post.save()
            return redirect(reverse('blog:post_list'))
        else:
            return redirect(reverse('blog:post_list'))
    else:
        form = createPostForm()
        
def welcome(request):
    return render( request,'post/welcome.html')