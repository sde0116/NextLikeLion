from pdb import post_mortem
from django.shortcuts import render, redirect
from .models import Post, Comment

def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

def new(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        new_post = Post.objects.create(
            title=title,
            # new.html input name이 title인 것을 model에서 만든 title이라는 틀에 담음.
            content=content)
        return redirect('detail', new_post.pk)
        # 여기서 detail은 함수 이름? vs url 이름
    
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('detail', post_pk)
        # detail이라는 함수로 redirect
    return render(request, 'detail.html', {'post':post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.filter(pk=post_pk).update(
            title=title,
            content=content
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post':post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)