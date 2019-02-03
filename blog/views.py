from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs':blogs})


def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})
    
def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()   #블로그로 부터 블로그 객체를 생성
    blog.title = request.GET['title'] 
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() 
    blog.save()         # 쿼리셋 메소드 중 하나 / 저장해라라는 의미
    return redirect('/blog/'+str(blog.id))
