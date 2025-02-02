from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

class IndexView(TemplateView):
    template_name = "index.html"

class CommentPageView(CreateView, ListView):
    model = Comment
    template_name = "comments.html"
    form_class = CommentForm
    success_url = reverse_lazy("comments")
    ordering = ["-created_at"]

    def form_valid(self, form):
        """ログインユーザーをコメントの投稿者に設定"""
        form.instance.user = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all().order_by("-created_at")
        return context

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("comments")

    def dispatch(self, request, *args, **kwargs):
        """投稿者以外が削除しようとした場合は拒否"""
        comment = get_object_or_404(Comment, pk=kwargs["pk"])

        if comment.user != self.request.user:  # 投稿者チェック
            return HttpResponseForbidden("このコメントを削除する権限がありません。")

        return super().dispatch(request, *args, **kwargs)
