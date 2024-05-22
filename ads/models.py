from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
class Post(models.Model):

    POSITIONS = [
        ('Tanks', 'Танки'),
        ('Hills', 'Хилы'),
        ('DD', 'ДД'),
        ('Sellers', 'Торговцы'),
        ('Gildmasters', 'Гилдмастеры'),
        ('Kwestgiver', 'Квестгиверы'),
        ('Blacksmith', 'Кузнецы'),
        ('Tanner', 'Кожевники'),
        ('Potion master', 'Зельевары'),
        ('Spell master', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, help_text=_('автор'), on_delete=models.CASCADE)
    category = models.CharField(max_length=30, help_text=_('категория'),choices=POSITIONS, default='Tanks')
    time_in = models.DateTimeField(auto_now_add=True, null=True )

    title = models.CharField(
        max_length=255,
        help_text=('заголовок'),
        unique=True,
    )
    description = models.TextField(help_text=_('текст'))

    mediaoforder = RichTextUploadingField(null=True, default=None)


    def __str__(self):
        return f'{self.title} (Автор: {self.author.username})'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class Respond(models.Model):
    text = models.CharField(max_length=255, unique=False, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1, verbose_name='Объявление')
    time_in = models.DateTimeField(auto_now_add=True,null=True,  verbose_name='Дата отклика')
    accepted = models.BooleanField(verbose_name='Принять отклик', default=None, null=True)

    def __str__(self):
        return f'respond pk={self.pk} by {self.author.username}'




