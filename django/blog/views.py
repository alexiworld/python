from django.forms import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts' 
    paginate_by = 5

    def get_queryset(self): # get_query_set must be get_queryset otherwise will be seeing other users posts too.
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # UserPassesTestMixin must be on the left of UpdateView!!
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # UserPassesTestMixin must be on the left of DeleteView!!
    model = Post
    success_url = '/'

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})