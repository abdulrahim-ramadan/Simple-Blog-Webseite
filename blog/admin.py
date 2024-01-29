from django.contrib import admin
from .models import Post , Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postAdmin(SummernoteModelAdmin):
    list_display=['id','author','publish_date']
    list_filter=['publish_date','tags']
    search_fields=['name','content']
    

admin.site.register(Post,postAdmin)
admin.site.register(Comment)