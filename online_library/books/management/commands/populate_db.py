from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Category, Book, Review

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories_data = [
            'Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 
            'Romance', 'Biography', 'History', 'Self-Help', 'Children'
        ]
        
        categories = []
        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(name=cat_name)
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {cat_name}')
        
        # Create sample books
        books_data = [
            {
                'title': 'The Great Adventure',
                'author': 'John Smith',
                'category': categories[0],  # Fiction
                'description': 'An epic tale of courage and discovery that will take you on an unforgettable journey through mysterious lands.'
            },
            {
                'title': 'Mystery of the Old House',
                'author': 'Sarah Johnson',
                'category': categories[2],  # Mystery
                'description': 'A thrilling mystery that will keep you guessing until the very last page. Who lives in the old house on the hill?'
            },
            {
                'title': 'Space Chronicles',
                'author': 'Mike Davis',
                'category': categories[3],  # Science Fiction
                'description': 'Journey to the stars in this captivating science fiction novel about humanity\'s future among the galaxies.'
            },
            {
                'title': 'Love in Paris',
                'author': 'Emma Wilson',
                'category': categories[4],  # Romance
                'description': 'A heartwarming romance set in the beautiful city of Paris. Will love conquer all obstacles?'
            },
            {
                'title': 'The Success Mindset',
                'author': 'Robert Brown',
                'category': categories[7],  # Self-Help
                'description': 'Discover the secrets to achieving your goals and living your best life with practical strategies and inspiring stories.'
            },
            {
                'title': 'World War Stories',
                'author': 'James Miller',
                'category': categories[6],  # History
                'description': 'Compelling accounts from one of history\'s most significant periods, told through personal stories and historical analysis.'
            },
            {
                'title': 'The Little Explorer',
                'author': 'Lucy Taylor',
                'category': categories[8],  # Children
                'description': 'Join young Alex on magical adventures that teach important lessons about friendship, courage, and kindness.'
            },
            {
                'title': 'Life Lessons',
                'author': 'Dr. Patricia Lee',
                'category': categories[5],  # Biography
                'description': 'An inspiring autobiography about overcoming challenges and making a difference in the world.'
            }
        ]
        
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
            if created:
                self.stdout.write(f'Created book: {book_data["title"]}')
        
        # Create a test user if it doesn't exist
        test_user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            }
        )
        if created:
            test_user.set_password('testpass123')
            test_user.save()
            self.stdout.write('Created test user: testuser (password: testpass123)')
        
        # Create sample reviews
        books = Book.objects.all()[:3]  # Get first 3 books
        review_data = [
            {'rating': 5, 'comment': 'Absolutely amazing book! Could not put it down.'},
            {'rating': 4, 'comment': 'Really enjoyed this read. Great character development.'},
            {'rating': 5, 'comment': 'One of the best books I\'ve read this year. Highly recommend!'},
            {'rating': 3, 'comment': 'Good book overall, though the pacing was a bit slow at times.'},
            {'rating': 4, 'comment': 'Interesting story with unexpected twists. Worth reading.'},
        ]
        
        for i, book in enumerate(books):
            if i < len(review_data):
                review, created = Review.objects.get_or_create(
                    book=book,
                    user=test_user,
                    defaults=review_data[i]
                )
                if created:
                    self.stdout.write(f'Created review for: {book.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write(
            f'Created {Category.objects.count()} categories, '
            f'{Book.objects.count()} books, and {Review.objects.count()} reviews.'
        )