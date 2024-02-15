from django.contrib import admin
from .models import Post , Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postAdmin(SummernoteModelAdmin):
    list_display=['title','publish_date']
    list_filter=['publish_date','tags']
    search_fields=['title','content']

class commentAdmin(admin.ModelAdmin):
    list_display=['user','comment','created_at']
    list_filter=['created_at']
    search_fields=['comment']
    
    

admin.site.register(Post,postAdmin)
admin.site.register(Comment,commentAdmin)