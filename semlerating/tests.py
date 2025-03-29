from django.test import TestCase
from .models import Semlor, Rating


class SemlorModelTests(TestCase):
    def setUp(self):
        # Create a sample Semlor instance for tests.
        self.sem = Semlor.objects.create(
            bakery='Test Bakery',
            city='Test City',
            picture_name='test.jpg',
            vegan=True,
            price=2.99,
            kind='Test Kind'
        )

    def test_semlor_str(self):
        # __str__ should return the bakery name.
        self.assertEqual(str(self.sem), 'Test Bakery')

    def test_rating_str(self):
        # Create a Rating and test its string representation.
        rating = Rating.objects.create(semla=self.sem, rating=4)
        self.assertEqual(str(rating), '4')

    def test_avg_rating_no_ratings(self):
        # Without any ratings, avg_rating should be None.
        self.assertIsNone(self.sem.avg_rating)

    def test_avg_rating_with_ratings(self):
        # Create several ratings and test the computed average.
        Rating.objects.create(semla=self.sem, rating=3)
        Rating.objects.create(semla=self.sem, rating=4)
        Rating.objects.create(semla=self.sem, rating=5)
        # The average of [3, 4, 5] is 4.0.
        self.assertEqual(self.sem.avg_rating, 4.0)

    def test_avg_rating_rounding(self):
        # Test that an annotated average gets rounded to two decimals.
        # Manually set _annotated_avg to simulate an annotated query.
        self.sem._annotated_avg = 4.126
        # It should round to 4.13.
        self.assertEqual(self.sem.avg_rating, 4.13)
