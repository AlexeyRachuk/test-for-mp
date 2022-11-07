from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from post.models import Post


class PostForm(forms.ModelForm):
    text_prew = forms.CharField(label='Текст превью', widget=CKEditorUploadingWidget())
    main_text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'user', 'postdate', 'draft']
    list_filter = ('user',)
    search_fields = ('user',)
    form = PostForm

    def get_changeform_initial_data(self, request):
        return {'user': request.user}