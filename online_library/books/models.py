from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category" 
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="books")
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.reviews.aggregate(avg=Avg("rating"))["avg"] or 0

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}★ by {self.user.username} on {self.book.title}"
