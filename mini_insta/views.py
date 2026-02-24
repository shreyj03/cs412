# File: mini_insta/views.py
# Author: Shrey Jain (shreyj@bu.edu), 2/9/26
# Description: Views for mini_insta application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mini_insta.forms import *
from .models import *
# Create your views here.

class ProfileListView(ListView):
    """View to display all profiles"""
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'
    
class ProfileDetailView(DetailView):
    '''Display a single profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile" # note singular variable name
    
class PostDetailView(DetailView):
    '''Display a single post.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post" 

class CreatePostView(CreateView):
    '''A view to handle creation of a new Post.
    (1) Display the html form to the user (GET)
    (2) Process form submission and store the new post object (POST)
    '''

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"
    
    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        '''validate incoming create post form'''
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        image_file = self.request.FILES.getlist('files')
        post = form.save()
        if image_file:
            for file in image_file:
                Photo.objects.create(post=post, image_file=file)
        return super().form_valid(form)
        
        
    def get_success_url(self):
        '''redirect to the new Post’s detail page'''
        return reverse("show_post", kwargs={"pk": self.object.pk})

class UpdateProfileView(UpdateView):
    '''a view to handle the update of a profile.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def get_success_url(self):
        # redirect to the updated profile page
        return reverse("show_profile", kwargs={"pk": self.object.pk})
    
class DeletePostView(DeleteView):
    '''a view to handle the deletion of a post.'''
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        profile = post.profile
        context['post'] = post
        context['profile'] = profile
        return context
    
    def get_success_url(self):
        '''redirect to the deleted post's corresponding profile detail page.'''
        return reverse("show_profile", kwargs={"pk": self.object.profile.pk})
    
class UpdatePostView(UpdateView):
    '''a view to handle updating a post.'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        profile = post.profile
        caption = post.caption
        context['post'] = post
        context['caption'] = caption
        context['profile'] = profile
        return context
    
    def get_success_url(self):
        '''redirect to the updated post's detail page.'''
        return reverse("show_post", kwargs={"pk": self.object.pk})