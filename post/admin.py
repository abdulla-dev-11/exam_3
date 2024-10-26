from django.contrib import admin
from .models import Post, Comment, Image, Category, About


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('post', )
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ('post', )
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'status')
    list_filter = ('status', 'created', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', '-created')
    inlines = (CommentInline, ImageInline)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'comment')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', )