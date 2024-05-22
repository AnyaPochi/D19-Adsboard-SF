from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.contrib.auth.validators import UnicodeUsernameValidator


from .models import Post,Respond
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class PostForm(forms.ModelForm):
    mediaoforder = forms.CharField(widget=CKEditorUploadingWidget(), label='Объявление')

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'mediaoforder']
        widgets = {
            "mediaoforder": CKEditorUploadingWidget(),
        }
    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get("description")
    #     title = cleaned_data.get("title")
    #
    #     if title == description:
    #         raise ValidationError(
    #             "Описание не должно быть идентично названию."
    #         )
    #
    #     return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ['text']
class BasicSignupForm(SignupForm):
    first_name = forms.CharField(required=True,label = "Имя")
    last_name = forms.CharField(required=True,label = "Фамилия")
    username_validator = UnicodeUsernameValidator()
    username = forms.CharField(
        label='Уникальное имя пользователя',
        max_length=150,
        validators=[username_validator],
        error_messages={
            "unique": 'Пользователь с таким именем уже зарегистрирован',
        },
    )
    email = forms.EmailField(label = "Email")
    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )
