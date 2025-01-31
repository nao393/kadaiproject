from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'created_at',)
    list_filter = ('created_at',)  # 作成日時でフィルタリング
    search_fields = ('name', 'content')
    ordering = ['-created_at']  # 最新のコメントが上に表示される

readonly_fields = ("created_at",)  # 作成日時を編集不可