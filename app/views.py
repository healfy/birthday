from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView
)
from django.contrib.auth import login
from .forms import PostForm, Post
from .models import Photo


class IndexView(TemplateView):
    template_name = 'bla.html'
    # login_url = 'login/'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['photos'] = Photo.objects.all()
        return ctx


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = '/post/list'

    def form_invalid(self, form):
        data = self.get_context_data(form=form)
        print(data['form'].errors)
        return super().form_invalid(form)


class PostListView(ListView):
    template_name = 'list_post.html'
    model = Post


class SinglePost(DetailView):
    template_name = 'single_post.html'
    model = Post
    queryset = Post.objects.all()
