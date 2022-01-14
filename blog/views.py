from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    """
    a view to show the post
    """
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def add_post(request):
    """ a view to add a post to the blog """

    if not request.user:
        messages.error(request, 'Sorry, you need to log in to do that.')
        return redirect(reverse('login'))

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            messages.success(request, "Successfully added blog post!")
            return redirect('blog', slug=post.slug)
        else:
            messages.error(
                request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = CommentForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_comment(request, slug):
    """ a view to add a comment to the post """
    post = get_object_or_404(Post, slug=slug)

    if not request.user:
        messages.error(request, 'Sorry, you need to log in to do that.')
        return redirect(reverse('login'))

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Successfully added comment!")
            return redirect('add_comment', slug=post.slug)
        else:
            messages.error(
                request, 'Failed to add comment. Please ensure the form is valid.')
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'post': post, 'form': form})
