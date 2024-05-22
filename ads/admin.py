from django.contrib import admin

from .models import Post, Respond
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    mediaoforder = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model =Post
        fields ='__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title','time_in','category')
    list_filter = ('title','time_in','category')
class RespondAdmin(admin.ModelAdmin):
    model = Respond



admin.site.register(Post, PostAdmin)
admin.site.register(Respond, RespondAdmin)

