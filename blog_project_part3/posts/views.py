from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.

# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author = request.user
#             post_form.save()
#             return redirect('add_post')
#     else:
#         post_form = forms.PostForm()
            
#     return render(request, 'add_post.html', {'form': post_form})

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    form_class = forms.PostForm
    model = models.Post
    success_url = reverse_lazy('add_post')
    template_name = 'add_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     post_form = forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.instance.author = request.user
#             post_form.save()
#             return redirect('profile')
            
#     return render(request, 'add_post.html', {'form': post_form})

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    form_class = forms.PostForm
    model = models.Post
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    template_name = 'add_post.html'

# @login_required
# def delete_post(request, id):
#     models.Post.objects.get(pk=id).delete()
#     return redirect('profile')
            
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    template_name = 'delete.html'
    
class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()     
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context