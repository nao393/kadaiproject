from django.db import models
from django.conf import settings

# Create your models here.
class Comment(models.Model):
#投稿時のユーザー情報のフィールド
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name="投稿者")
#名前のフィールド
    name = models.CharField(max_length=50,
                            default="名無しさん",
                            verbose_name="名前")

#コメントのフィールド
    content = models.TextField(max_length=500,
                                verbose_name="本文")

#投稿日時のフィールド
    created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="投稿日時")

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"  # 最初の20文字を表示