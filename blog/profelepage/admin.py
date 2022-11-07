from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import UserPage


class UserPageForm(forms.ModelForm):
    map = forms.CharField(label='Карта',
                          help_text='Сгенерировать яндекс-карту с любой меткой и вставить сюда через источник',
                          widget=CKEditorUploadingWidget())
    tel = forms.CharField(label='Телефон', help_text='Добавить код через источник',
                          widget=CKEditorUploadingWidget())
    email = forms.CharField(label='Email', help_text='Добавить код через источник',
                            widget=CKEditorUploadingWidget())


class Meta:
    model = UserPage
    fields = '__all__'


@admin.register(UserPage)
class AdminUserPage(admin.ModelAdmin):
    fields = ['user', 'map', 'tel', 'email']
    form = UserPageForm

    def get_changeform_initial_data(self, request):
        return {'user': request.user}
