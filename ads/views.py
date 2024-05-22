from datetime import timezone

import pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone
from django.shortcuts import redirect

# from .filters import RespondFilter
# from ads.forms import ImageForm
from .models import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,DeleteView
)
from .forms import PostForm
from django.urls import reverse_lazy
class PostList(ListView):
    queryset = Post.objects.order_by('time_in')
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

# прописываю функции для выбора таймзоны
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/posts/')
class UserDetail(LoginRequiredMixin, DetailView):
    """Для отображения профиля"""
    model = User
    template_name = "user_profile.html"
    context_object_name = 'user'


class PostDetail(LoginRequiredMixin, DetailView):
    queryset = Post.objects.all()
    template_name = 'post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context
    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(f'/posts/{pk}')
class PostCreate(LoginRequiredMixin,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(LoginRequiredMixin,UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('posts')

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)
    # def post(self, request):/
    #     request.session['django_timezone'] = request.POST['timezone']
    #     return redirect('/posts/')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#
# # отклики на мои объявления
# @login_required
# def respond_to_me(request):
#     queryset = Respond.objects.\
#             filter(post__in=Post.objects.filter(author_id=request.user))
#
#     filterset = RespondFilter(request.GET, queryset)
#     context = {'all_respond': filterset.qs.order_by('-time_in'),
#                'filterset': filterset}
#     if request.method == "POST":
#         answer = request.POST['respond'].split(' ')
#         id = int(answer[0])
#         accept = int(answer[1])
#         Respond.objects.filter(pk=id).update(accepted=(True if accept else False))
#         respond = Respond.objects.get(pk=id)
#         if accept:
#             html_content = render_to_string(
#                 'request_accepted.html',
#                 {
#                     'user': respond.author,
#                     'writer': request.user.username,
#                     'post': respond.post,
#                 }
#             )
#             msg = EmailMultiAlternatives(
#                 subject=f'{respond.author.username.capitalize()}',
#                 from_email='ytrewq878787@yandex.ru',
#                 to=[respond.author.email],
#             )
#             msg.attach_alternative(html_content, "text/html")
#             msg.send(fail_silently=True)
#             print('Отклик принят письмо с оповещением оправленно')
#         else:
#             Post.objects.get(pk=id).delete()
#     return render(request, 'my_list.html', context=context)
#
#
# class RespondForm:
#     pass
#
#
# @login_required
# def respond_create(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == "POST":
#         form = RespondForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data['post'] = post
#             form.cleaned_data['author'] = request.user
#             Post.objects.create(**form.cleaned_data)
#             return redirect('post', pk)
#     else:
#         form = RespondForm()
#     context = {'post': post, 'form': form}
#     return render(request, 'respond_create.html', context=context)
#
#
#
# @login_required
# def respond_delete(request, post_id, pk):
#     respond = get_object_or_404(Respond, pk=pk)
#     context = {'respond': respond}
#     if request.method == "POST":
#         respond.delete()
#         return redirect("post", post_id)
#
#     else:
#         return render(request, 'respond_delete.html', context)
