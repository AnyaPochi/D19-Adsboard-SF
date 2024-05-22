from django.contrib import admin

from .models import Post, Respond
from modeltranslation.admin import TranslationAdmin

class PostTranslationAdmin(admin.ModelAdmin):
    model = Post
# admin.ModelAdmin
    list_display = ('title','time_in','category')
    list_filter = ('title','time_in','category')
class RespondTranslationAdmin(admin.ModelAdmin):
    model = Respond



admin.site.register(Post, PostTranslationAdmin)
admin.site.register(Respond, RespondTranslationAdmin)

