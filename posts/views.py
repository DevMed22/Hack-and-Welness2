from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
import datetime
from .forms import PostCreationForm, CommentForm
from .models import Post



class PostsListView(ListView):
    model = Post
    context_object_name = "posts_list"
    template_name = 'posts/posts_list.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy("posts:posts_list")
    template_name = "posts/create_post.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentGet(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context



class CommentPost(SingleObjectMixin, FormView):
    model = Post
    template_name = "posts/post_detail.html"
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        self.object = self.get_object()
        ob = self.object
        return reverse("posts:post_detail", kwargs={'pk':ob.pk})



class PostDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields = ('title', 'body',)
    def form_valid(self, form):
        form.instance.edited_date = datetime.datetime.now()
        return super().form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("posts:posts_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user