from django.shortcuts import render
from articles.models import Article
from django.shortcuts import render, redirect
# Create your views here.
# def index(request):
#     return render(request, 'articles/index.html')
def index(request):
    article = Article.objects.all()
    context ={
        'articles':article
    }
    return render(request, 'articles/index.html',context)
     
def new(request):
    return render(request, 'articles/new.html')

# def create(request):
#     title = request.GET.get('title')
#     content = request.GET.get('content')
#     context ={
#         'title' : title,
#         'content' : content
#     }
#     return render(request, 'articles/create.html', context)
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)

    return redirect('articles:index')

def introduce(request):
    return render(request, 'articles/introduce.html')
#1. /introduce/
#2. h1 태그로 이루어진 제목
#2-1. p태그에 이름과 나이 작성
#3. back 링크로 index로 돌아갈 수 있는 링크 하나
#4. index에서 introduce 이동할 수 있는 링크 하나
#5. base.html 상속 받아서 block body 안에 작성

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html',context)

def delete(request,article_pk):
    #request method
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request,'articles/edit.html',context)

def update(request, article_pk):
    edit_title = request.POST.get('edit_title')
    edit_content = request.POST.get('edit_content')
    article = Article.objects.get(pk=article_pk)
    article.title = edit_title
    article.content = edit_content
    article.save()
    return redirect('articles:detail',article_pk)