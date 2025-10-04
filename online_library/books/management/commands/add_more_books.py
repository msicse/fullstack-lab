from django.core.management.base import BaseCommand
from books.models import Category, Book

class Command(BaseCommand):
    help = 'Add more sample books for pagination testing'

    def handle(self, *args, **options):
        self.stdout.write('Adding more sample books...')
        
        # Get existing categories
        categories = list(Category.objects.all())
        if not categories:
            self.stdout.write(self.style.ERROR('No categories found. Please run populate_db first.'))
            return
        
        # Sample book data for testing pagination
        additional_books = [
            {'title': 'The Green Garden', 'author': 'Emily Green', 'description': 'A beautiful story about finding peace in nature and the healing power of gardens.'},
            {'title': 'Forest Adventures', 'author': 'Mark Woods', 'description': 'Join young explorers as they discover the secrets hidden deep in the ancient forest.'},
            {'title': 'Ocean Mysteries', 'author': 'Sarah Waters', 'description': 'Dive into the depths of the ocean and uncover its most amazing mysteries and creatures.'},
            {'title': 'Mountain Climbing Guide', 'author': 'Alex Peak', 'description': 'Essential tips and techniques for safe and successful mountain climbing adventures.'},
            {'title': 'Desert Survival', 'author': 'Jake Sand', 'description': 'Learn the art of surviving in harsh desert environments with practical survival skills.'},
            {'title': 'River Journey', 'author': 'Lisa Flow', 'description': 'Follow the path of a great river from source to sea in this captivating nature story.'},
            {'title': 'Butterfly Dreams', 'author': 'Maya Wing', 'description': 'A magical tale about transformation and the beautiful journey of butterflies.'},
            {'title': 'Tree Wisdom', 'author': 'Oliver Bark', 'description': 'Ancient wisdom from the trees and what we can learn from the forest elders.'},
            {'title': 'Flower Power', 'author': 'Rose Petal', 'description': 'Discover the amazing world of flowers and their important role in our ecosystem.'},
            {'title': 'Animal Kingdom', 'author': 'Leo Wild', 'description': 'Explore the fascinating behaviors and relationships in the animal kingdom.'},
            {'title': 'Seasons of Change', 'author': 'Autumn Leaf', 'description': 'Experience the beauty and cycles of nature through the changing seasons.'},
            {'title': 'Crystal Clear Waters', 'author': 'Crystal Brook', 'description': 'The importance of clean water and how we can protect our precious water resources.'},
            {'title': 'Wind Whispers', 'author': 'Aiden Breeze', 'description': 'Listen to the stories the wind tells as it travels across different landscapes.'},
            {'title': 'Sunset Memories', 'author': 'Golden Sky', 'description': 'Heartwarming memories created during magical sunset moments in nature.'},
            {'title': 'Moonlight Tales', 'author': 'Luna Night', 'description': 'Enchanting stories that unfold under the silver light of the full moon.'},
            {'title': 'Earth Chronicles', 'author': 'Terra Firma', 'description': 'The incredible history of our planet told through geological wonders.'},
            {'title': 'Bird Songs', 'author': 'Melody Chirp', 'description': 'Learn the language of birds and understand their beautiful songs and calls.'},
            {'title': 'Herb Garden Secrets', 'author': 'Sage Mint', 'description': 'Growing and using herbs for cooking, medicine, and natural living.'},
            {'title': 'Peaceful Meadows', 'author': 'Grace Field', 'description': 'Find inner peace and mindfulness through quiet moments in natural meadows.'},
            {'title': 'Nature Photography', 'author': 'Focus Nature', 'description': 'Master the art of capturing the beauty of nature through your camera lens.'},
        ]
        
        created_count = 0
        for i, book_data in enumerate(additional_books):
            category = categories[i % len(categories)]  # Rotate through categories
            
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults={
                    'author': book_data['author'],
                    'category': category,
                    'description': book_data['description']
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'Created book: {book_data["title"]}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} additional books!')
        )
        self.stdout.write(f'Total books in database: {Book.objects.count()}')