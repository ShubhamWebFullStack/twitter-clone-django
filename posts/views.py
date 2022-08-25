from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post
from posts.forms import PostForm

def index(request):
    # If the request method is POST made from Templates (Front-end)
    if request.method == "POST":
        # Django Form Validation & Storing Post Data and Img Files inside the form variable via form instance of a PostForm Class in FORMS.PY.
        # Input as request for Post Data & ImgFiles, then validation in PostForm Class inside model=post.
        form = PostForm(request.POST, request.FILES)
        # If form is valid as per ModelForm Class (Model Fields, Http Request)
        if form.is_valid():
            #Then, Save the Post Details inside the Model "Post"
            form.save()
            # Redirects to Home Page.
            return HttpResponseRedirect("/")
        else:
            # If error, then redirects to error page.
            return HttpResponseRedirect(form.errors.as_json())

    # Get all the posts, limit = 20 sort by Date Modified, Object is one Post & all stands for all of its fields.
    posts = Post.objects.all().order_by("-updated_at")[:20]

    # Render all the posts on the Posts Templates.
    return render(request, "posts.html", {"posts": posts}) 

def edit (request, post_id):
    # Get the already created Post using post_id.
    # Find post
    # if request.method == "GET":
    # post = Post.objects.get(id=post_id)
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Not Valid!") 

    #         
    form = PostForm

    # Render all the edited posts on the Edit Templates.
    return render (request, "edit.html", {"post": post, "form": form})  


def delete (request, post_id):
    # Get the already created Post using post_id.
    # Find post
    # if request.method == "GET":
    # post = Post.objects.get(id=post_id)
    post = Post.objects.get(id=post_id)
    # Delete function
    post.delete()
    return HttpResponseRedirect("/")

def like (request, post_id):
    # Get the already created Post using post_id.
    # Find post
    # if request.method == "GET":
    # post = Post.objects.get(id=post_id)
    new_like = Post.objects.get(id=post_id)
    new_like.like_count += 1
    new_like.save()
    return HttpResponseRedirect("/")
