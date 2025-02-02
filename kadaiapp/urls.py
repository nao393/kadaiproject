from django.urls import path
from .views import IndexView, CommentPageView, CommentDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # トップページ
    path("comments/", CommentPageView.as_view(), name="comments"),  # コメントページ
    path("comment/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment_delete"),  # コメント削除
    
]
