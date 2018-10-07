from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post

	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #this means that our post will be reverse ordered
	paginate_by = 5  #count of post by pag

class UserPostListView(ListView):
	model = Post

	template_name = 'blog/user_posts.html' 
	context_object_name = 'posts'
	paginate_by = 5 

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) #if the user exist then we return user page and if user don`t exist then we return 404
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/' #this field will redirect user when he deleted his post

	def test_func(self): #this func check that the user which want to delete the post should be author of this post
		post = self.get_object()

		if self.request.user == post.author:
			return True
		else:
			return False 

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user #set the author of the post user that created that post
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user #set the author of the post user that created that post
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		else:
			return False




def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



