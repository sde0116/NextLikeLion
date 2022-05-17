from django.contrib import admin
from .models import Post, Comment
# model import 하기

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'address', 'hit')
    empty_value_display = '입력값 없음'
# admin 페이지 커스터마이징 하는 것

admin.site.register(Comment)
# admin.site.register 호출해서 model 등록하기