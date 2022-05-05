from django.contrib import admin

from blogging.models import Post, Categories

admin.site.register(Post)
admin.site.register(Categories)


class CategoryInline(admin.TabularInline):
    model = Categories.posts.through


class CategoriesAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]
    exclude = ("Posts",)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]



