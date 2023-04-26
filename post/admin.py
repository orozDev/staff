from django.contrib import admin
from django.utils.safestring import mark_safe

from post.models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminFrom(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_image')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    readonly_fields = ('get_image',)
    form = PostAdminFrom

    @admin.display(description='image')
    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.image.url}" width="300px">')

# Register your models here.
