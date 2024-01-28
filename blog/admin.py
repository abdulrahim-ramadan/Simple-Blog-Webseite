from django.contrib import admin
from .models import Post , Comment

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display=['id','author','publish_date']
    list_filter=['publish_date','tags']
    search_fields=['name','content']
    

admin.site.register(Post,postAdmin)
admin.site.register(Comment)