from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator


def blog(request):
    posts_list = Post.objects.filter(active=1).order_by('-pub_date')
    paginator = Paginator(posts_list, 5)

    try:
        page = int(request.GET.get("page", 1))

    except:
        page = 1

    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    # breadcrumb feed
    link = reverse('blog:home')
    link1 = reverse('blog:index')

    # block aside feeds
    recent_5_posts = posts_list[:5]
    recent_5_fun = posts_list.filter(category='fun')[:5]

    context = {'posts':posts, 'recent_5_posts': recent_5_posts,
               'recent_5_fun': recent_5_fun,
               }

    return render(request, 'blog/index.html', context)

def home(request):
    return render(request, 'blog/home.html')

def trash(request):
    posts_list = Post.objects.filter(active=0).order_by('-pub_date')
    paginator = Paginator(posts_list, 5)

    try:
        page = int(request.GET.get("page", 1))

    except:
        page = 1

    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/trash.html', {'posts':posts})

def category(request, category):
    posts_list = Post.objects.filter(active=1, category=category).order_by('-pub_date')
    paginator = Paginator(posts_list, 5)

    try:
        page = int(request.GET.get("page", 1))

    except:
        page = 1

    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    # breadcrumb feed
    link = reverse('blog:home')
    link1 = reverse('blog:index')

    # block aside feeds
    recent_5_posts = posts_list[:5]
    recent_5_fun = posts_list.filter(category='fun')[:5]

    context = {'posts':posts, 'recent_5_posts': recent_5_posts,
               'recent_5_fun': recent_5_fun,
               }

    return render(request, 'blog/index.html', context)

def detail(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    comments = post.comment_set.filter(active=1).order_by('-pub_date')
    return render(request, 'blog/detail.html', {'post':post,'comments':comments})

def add(request):
    if request.method == "GET":
        return render(request, 'blog/add.html')

    elif request.method == "POST":
        now = timezone.now()
        p = Post(post_title=request.POST['post_title'],\
                 post_text=request.POST['post_text'],\
                 pub_date=now,mod_date=now,\
                 category=request.POST['category']
                 )
        p.save()

        return HttpResponseRedirect(reverse('blog:index'))

def edit(request, question_id):
    now = timezone.now()
    post = Post.objects.get(pk=question_id)
    if request.method == "GET":
        return render(request, 'blog/edit.html', {'post':post})

    else:
        post.post_title = request.POST['post_title']
        post.post_text = request.POST['post_text']
        post.mod_date = now
        post.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))
        # return HttpResponse(post.save())

def delete(request, question_id):
    post = Post.objects.get(pk=question_id)
    post.active = False
    post.save()
    return HttpResponseRedirect(reverse('blog:index'))

def comment(request, question_id):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('blog:detail', args=(question_id,)))

    elif request.method == "POST":
        now = timezone.now()
        post = get_object_or_404(Post, pk=question_id)
        post.comment_set.create(comment_text=request.POST['comment'],pub_date=now,mod_date=now)

        return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))


def like(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))

def share(request, question_id):
    post = get_object_or_404(Post, pk= question_id)
    post.pub_date = timezone.now()
    post.shares += 1
    post.save()
    return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))


def edit_comment(request, comment_id):
    now = timezone.now()
    comment = Comment.objects.get(pk=comment_id)
    post_id = comment.post_id
    if request.method == "GET":
        return render(request, 'blog/edit_comment.html', {'comment':comment})

    else:
        comment.comment_text = request.POST['comment']
        comment.mod_date = now
        comment.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(post_id,)))


def del_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post_id
    comment.active = False
    comment.save()
    return HttpResponseRedirect(reverse('blog:detail', args=(post_id,)))
