from django.db import models
from employees.models import Employee


class PerformanceReview(models.Model):

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    review_date = models.DateField()

    rating = models.IntegerField(
        choices=RATING_CHOICES
    )

    goals = models.TextField()

    feedback = models.TextField()

    reviewer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee} ({self.rating}/5)"