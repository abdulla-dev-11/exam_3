from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from config import settings
from .forms import CommentForm, EmailPostForm
from .models import Category, Post, Image, Comment, About
from django.views.generic import ListView, FormView


class IndexlistView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3


class AboutlistView(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'about.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk,
                             status=Post.Status.PUBLISH,
                             )
    # List of active comments for this post
    comments = post.comment.all()
    # Form for users to comment
    form = CommentForm()

    return render(request,
                  'post-detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html')


class EmailView(FormView):
    template_name = 'contact.html'
    form_class = EmailPostForm
    success_url = reverse_lazy('dashboard:success')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        massage = form.cleaned_data['message']
        to = form.cleaned_data['to']
        send_mail(
            subject,
            massage,
            settings.EMAIL_HOST_USER,
            [to],
        )

        return super(EmailView, self).form_valid(form)


def terms_view(request):
    return render(request, 'terms-conditions.html', )


def policy_view(request):
    return render(request, 'privacy-policy.html')