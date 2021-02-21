from django.contrib import admin
from .models import Article, Category


# change title admin page

admin.site.site_header = 'وبلاگ جنگویی من'


## action custom
def make_published(modeladmin, request, queryset):
    row_updated = queryset.update(status='p')
    if row_updated == 1:
        massage_bit = 'منتشر شد.'
    else:
        massage_bit = 'منتشر شدن.'
        
    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,massage_bit))
make_published.short_description = 'انتشار مقالات انتخاب شده' 

def make_drafted(modeladmin, request, queryset):
    row_updated = queryset.update(status='d')
    if row_updated == 1:
        massage_bit = 'پیش نویس شد.'
    else:
        massage_bit = 'پیش نویس شدن.'
        
    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,massage_bit))
make_drafted.short_description = 'پیش نویس مقالات انتخاب شده' 



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', "title", "slug",'parent', "status")
    list_filter = (["status"])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}
 

admin.site.register(Category, CategoryAdmin),


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",'thumbnail_tag' ,"slug", "jpublish", "status","category_to_str")
    list_filter = (
        "publish",
        "status",
    )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['status', '-publish']
    actions = [make_published,make_drafted]

    def category_to_str(self,obj):
        return ' , '.join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Article, ArticleAdmin),
