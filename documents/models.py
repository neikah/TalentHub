from django.db import models
from employees.models import Employee


class Document(models.Model):

    DOCUMENT_TYPES = [
        ('Resume', 'Resume'),
        ('Offer Letter', 'Offer Letter'),
        ('ID Proof', 'ID Proof'),
        ('Certificate', 'Certificate'),
        ('Experience Letter', 'Experience Letter'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    document_type = models.CharField(
        max_length=30,
        choices=DOCUMENT_TYPES
    )

    title = models.CharField(max_length=150)

    file = models.FileField(upload_to='documents/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.document_type}"