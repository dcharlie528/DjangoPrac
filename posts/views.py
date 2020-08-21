from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import requests
# Create your views here.

# def index(request):
#     posts = Post.objects.all()
#     #SELECT * FROM posts_post
#     return render(request, "posts/index.html", {"posts": posts})

def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/21") #28為國內旅遊
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "posts/index.html", {"articles": articles})

# def index(request):
#     posts = Post.objects.filter(location="台南")
#     # SELECT * FROM posts_post WHERE location="台南"
#     return HttpResponse("My First Django App.")    取得台南的資料

# def index(request):
#     posts = Post.objects.get(id=1)
#     # SELECT * FROM posts_post WHERE id=1
#     return HttpResponse("My First Django App.")    取的id為1的資料