from django.forms import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

# posts = [
#     {
#         'author': 'AlexiworlD',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27th, 2018'
#     },
#     {
#         'author': 'Trump vs Biden',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28th, 2018'
#     }
# ]

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all() # posts
    }
    return render(request, 'blog/home.html', context) # the path under templates directory

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # overriding default <app>/<model>_<viewtype>.html
    # overriding ListView's default name used in context to 'posts', 
    # i.e. to match the one used in home function (see context variable with 'posts' above).
    context_object_name = 'posts' 
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})