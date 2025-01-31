from django.db import models

# Create your models here.
class Comment(models.Model):
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
        return self.name + ": " + self.content[:20]  # 最初の20文字を表示