from django.contrib import admin
from .models import Post, Subject, Level
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    list_filter = ['subject','level']
    search_fields = ['title','content']
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Subject)
admin.site.register(Level)
