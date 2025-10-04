from django.contrib import admin
from .models import Book, Category, Review

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']
    search_fields = ['name']
    ordering = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'average_rating', 'review_count']
    list_filter = ['category', 'created_at'] if hasattr(Book, 'created_at') else ['category']
    search_fields = ['title', 'author', 'description']
    list_editable = ['category']
    ordering = ['title']
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'category', 'description')
        }),
        ('Media', {
            'fields': ('cover_image',),
            'classes': ('collapse',)
        }),
    )
    
    def review_count(self, obj):
        return obj.reviews.count()
    review_count.short_description = 'Reviews'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at', 'comment_preview']
    list_filter = ['rating', 'created_at', 'book__category']
    search_fields = ['book__title', 'user__username', 'comment']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    def comment_preview(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment Preview'
