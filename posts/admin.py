from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Location
from .models import Post

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'author', 'location')
    exclude = ('create_date', ) #不要顯示的欄位

admin.site.register(Location,LocationAdmin)  #註冊至Administration(管理員後台)
admin.site.register(Post,PostAdmin)  #註冊至Administration(管理員後台)