from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='dairy_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='dairy_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    daily_milk_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# Base Cow Model
class Cow(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('sick', 'Sick'),
        ('dead', 'Dead'),
    ]

    BREED_CHOICES = [
        ('HF', 'Holstein Friesian'),
        ('JER', 'Jersey'),
        ('AYR', 'Ayrshire'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=3, choices=BREED_CHOICES)
    birth_date = models.DateField()
    weight = models.FloatField()
    health_status = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name

# Derived Models
class Bull(Cow):
    semen_quality = models.CharField(max_length=100)

class Heifer(Cow):
    pregnancy_status = models.BooleanField(default=False)
    last_served_date = models.DateField(blank=True, null=True)
    insemination_type = models.CharField(max_length=20, choices=[('AI', 'Artificial Insemination'), ('Bull', 'Bull')], blank=True, null=True)

class Calf(Cow):
    weaning_date = models.DateField()

# Product Model
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_measure = models.CharField(max_length=50)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Health Record
class HealthRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    treatment_date = models.DateField(auto_now_add=True)
    vet_doctor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cow.name} - {self.date}"

# Reproduction Record
class ReproductionRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cow = models.ForeignKey(Heifer, on_delete=models.CASCADE)
    insemination_date = models.DateField()
    expected_due_date = models.DateField()
    served_date = models.DateField()
    insemination_type = models.CharField(max_length=20, choices=[('AI', 'Artificial Insemination'), ('Bull', 'Bull')])
    result = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.cow.name} - {self.insemination_date}"

# Sales Record
class SalesRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.customer.user.username if self.customer else 'No Customer'} - {self.product.name if self.product else 'Cow'}"

# Milking Record
class MilkingRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    quantity_liters = models.FloatField()

    def __str__(self):
        return f"{self.cow.name} - {self.date}"

# Feeding Record
class FeedingRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    food_type = models.CharField(max_length=100)
    quantity_kg = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cow.name} - {self.date}"