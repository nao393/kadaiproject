from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all().order_by("-created_at")
        return context

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("comments")

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs["pk"])
        comment.delete()
        return HttpResponseRedirect(self.success_url)
