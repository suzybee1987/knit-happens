from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CommentForm, PostForm


def blog(request):
    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


@login_required
def add_post(request):
    """ a view to add a post to the blog """

    context = {}
    form = PostForm()
    context['form'] = form

    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added your blog post")
            return redirect(reverse('blog'))
        else:
            messages.error(
                request, "Failed to add blog post, please check the form is valid")
    else:
        form = PostForm()

    template = 'blog/add_post.html'
  
    return render(request, template, context)

def post_detail(request, slug):
    
    context = {}
    post = Post.objects.get(slug=slug)

    context['post'] = post

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Successfully added your comment")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(
                request, "Failed to add comment, please check the form is valid")
    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'form': form
    }

    return render(request, template, context)



# @login_required
# def add_comment(request, slug):
#     """ a view to add a comment to the post """
#     context = {}
#     form = CommentForm()
#     context['form'] = form

#     if request.method == "POST":
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid:
#             obj = form.save(commit=False)
#             author = request.user
#             obj.author = author
#             obj.save()
#             messages.success(request, "Successfully added your comment")
#             return redirect(reverse('blog'))
#         else:
#             messages.error(
#                 request, "Failed to add comment, please check the form is valid")
#     else:
#         form = PostForm()

#     template = 'blog/post_detail.html'
#     context = {
#         'form': form
#     }
#     return render(request, template, context)
