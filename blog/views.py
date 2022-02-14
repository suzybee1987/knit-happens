from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm, PostForm


def blog(request):
    """
    View all blog posts
    """
    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


@login_required
def add_post(request):
    """ a view to add a post to the blog """

    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added your blog post")
            return redirect(reverse('post_detail', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add blog post, please check the form is \
                    valid")
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def post_detail(request, slug):
    """ a view to see the blog post with potential to add a comment """
    context = {}
    post = Post.objects.get(slug=slug)

    context['post'] = post

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment_author = request.user
            comment.comment_author = comment_author
            comment.save()
            messages.success(request, "Successfully added your comment")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(
                request, "Failed to add comment, please check the form is \
                    valid")
    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ edit post """
    post = Post.objects.get(slug=slug)
    user = request.user

    if request.method == "POST":
        form = PostForm(request.POST or None,
                        request.FILES or None, instance=post)
        if user == post.author:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                post = obj
                messages.success(request, "Successfully edited your blog post")
                return redirect(reverse('post_detail', args=[obj.slug]))
            else:
                messages.error(request, "Failed to update post.")
        else:
            messages.info(request, 'You are not allowed to do that as you are \
                not the post author!')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ allows the user to delete a post they have """
    post = Post.objects.get(slug=slug)
    user = request.user
    if post.author == user:
        post.delete()
        messages.success(request, f'You have deleted {post.title}')
        return redirect(reverse('blog'))

    else:
        messages.error(request, "You are not allowed to do that.")

    template = 'blog/edit_post.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
