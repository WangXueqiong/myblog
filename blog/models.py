from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

#在admin中将Article的数据默认显示名称
    def __str__(self):
        return self.title