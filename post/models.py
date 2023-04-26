from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class Post(models.Model):

    class Meta:
        verbose_name = _('пост')
        verbose_name_plural = _('посты')
        ordering = ('-id',)

    title = models.CharField(max_length=150)
    image = ResizedImageField(upload_to='images/', force_format='WEBP', quality=90)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

# Create your models here.
