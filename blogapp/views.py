from django.shortcuts import render,Http404,get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView,FormView
from models import User, Message, SiteDesc ,Comment,Blog

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Blog
    context_object_name = 'blog'

class AboutMe(ListView):
    template_name = 'about.html'
    model = User
    context_object_name = "aboutme"

    def get_context_data(self, **kwargs):

        context = super(AboutMe, self).get_context_data(**kwargs)
        context['aboutme'] = User.objects.all()
        return context

class Article(DetailView):
    template_name = 'post.html'
    context_object_name = 'blog'
    def get_object(self):
        blog = Blog.objects.get(id=self.kwargs.get('id'))
        return blog

class ListArticle(ListView):
    pass

class Contact(CreateView):
    model = Message
    #template_name_suffix = '_create_form'git
    template_name = 'contact.html'
    fields = '__all__'
    success_url = "/"


