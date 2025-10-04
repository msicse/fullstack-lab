from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import user_or_admin_required
from .models import Book, Category, Review

# Create your views here.


def book_list(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")
    page = request.GET.get('page', 1)

    books = Book.objects.select_related('category').order_by('title')  # Add consistent ordering for pagination and optimize queries

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    if category_id:
        books = books.filter(category__id=category_id)

    # Pagination - 12 books per page
    paginator = Paginator(books, 12)
    
    try:
        books_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        books_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        books_page = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    selected_category_obj = None
    if category_id:
        try:
            selected_category_obj = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            pass
    
    context = {
        'books': books_page,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'selected_category_obj': selected_category_obj,
        'total_books': paginator.count,  # Total number of books after filtering
    }
    
    return render(request, "books/book_list.html", context)

def books_only_list(request):
    """Book list view without hero section - for /books/ URL"""
    query = request.GET.get("q")
    category_id = request.GET.get("category")
    page = request.GET.get('page', 1)

    books = Book.objects.select_related('category').order_by('title')  # Add consistent ordering for pagination and optimize queries

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    if category_id:
        books = books.filter(category__id=category_id)

    # Pagination - 12 books per page
    paginator = Paginator(books, 12)
    
    try:
        books_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        books_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        books_page = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    selected_category_obj = None
    if category_id:
        try:
            selected_category_obj = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            pass
    
    context = {
        'books': books_page,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'selected_category_obj': selected_category_obj,
        'total_books': paginator.count,  # Total number of books after filtering
        'show_hero': False,  # Flag to hide hero section
    }
    
    return render(request, "books/book_list.html", context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_has_reviewed = False
    user_can_review = False
    form_data = {}  # Store form data for re-rendering on errors
    
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        user_has_reviewed = Review.objects.filter(book=book, user=request.user).exists()
        # Users can review, admins can review
        user_can_review = request.user.profile.is_user() or request.user.profile.is_admin()

    if request.method == "POST" and request.user.is_authenticated and user_can_review:
        try:
            rating = request.POST.get("rating", "")
            comment = request.POST.get("comment", "").strip()
            
            # Store form data to preserve it on errors
            form_data = {
                'rating': rating,
                'comment': comment
            }
            
            # Validation
            if not rating:
                messages.error(request, "Please select a rating for your review.")
            elif not (1 <= int(rating) <= 5):
                messages.error(request, "Please select a valid rating between 1 and 5 stars.")
            elif not comment:
                messages.error(request, "Please write a comment for your review.")
            elif len(comment) < 10:
                messages.error(request, "Please write a more detailed review (at least 10 characters).")
            elif user_has_reviewed:
                messages.error(request, "You have already reviewed this book.")
            else:
                # Create the review
                Review.objects.create(book=book, user=request.user, rating=int(rating), comment=comment)
                messages.success(request, "Thank you for your review! It has been added successfully.")
                return redirect("book-detail", pk=book.id)
                
        except (ValueError, TypeError):
            messages.error(request, "Please select a valid rating.")
        except Exception as e:
            messages.error(request, "An error occurred while saving your review. Please try again.")

    # Refresh user_has_reviewed status in case a review was just added
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        user_has_reviewed = Review.objects.filter(book=book, user=request.user).exists()

    context = {
        'book': book,
        'user_has_reviewed': user_has_reviewed,
        'user_can_review': user_can_review,
        'form_data': form_data,  # Pass form data to template
    }
    return render(request, "books/book_detail.html", context)
