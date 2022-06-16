from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# posts = [
#     {
#         'author':'ABC',
#         'title':'Blog post 1',
#         'content':'First post content',
#         'date_posted':'16 april, 1995'
#     },
#      {
#         'author':'DEF',
#         'title':'Blog post 2',
#         'content':'Second post content',
#         'date_posted':'20 april, 1995'
#     }

# ]
def home(request):
    context = {
        # 'posts' : posts
        'posts' : Post.objects.all()
    }
    return render(request,"blog/home.html", context)

def about(request):
    return render(request,"blog/about.html",{'title':'About'})

