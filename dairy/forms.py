from django import forms
from .models import (
    User, Customer, Bull, Heifer, Calf, Product, HealthRecord,
    ReproductionRecord, SalesRecord, MilkingRecord, FeedingRecord
)

# User Form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'address', 'daily_milk_taken']

# Bull Form
class BullForm(forms.ModelForm):
    class Meta:
        model = Bull
        fields = ['name', 'breed', 'birth_date', 'weight', 'health_status', 'status', 'semen_quality']

# Heifer Form
class HeiferForm(forms.ModelForm):
    class Meta:
        model = Heifer
        fields = ['name', 'breed', 'birth_date', 'weight', 'health_status', 'status', 'pregnancy_status', 'last_served_date', 'insemination_type']

# Calf Form
class CalfForm(forms.ModelForm):
    class Meta:
        model = Calf
        fields = ['name', 'breed', 'birth_date', 'weight', 'health_status', 'status', 'weaning_date']

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'unit_price', 'unit_measure', 'stock_quantity']

# Health Record Form
class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['cow', 'description', 'diagnosis', 'treatment', 'vet_doctor']

# Reproduction Record Form
class ReproductionRecordForm(forms.ModelForm):
    class Meta:
        model = ReproductionRecord
        fields = ['cow', 'insemination_date', 'expected_due_date', 'served_date', 'insemination_type', 'result']

# Sales Record Form
class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ['product', 'customer', 'cow', 'quantity', 'total_price', 'date']

# Milking Record Form
class MilkingRecordForm(forms.ModelForm):
    class Meta:
        model = MilkingRecord
        fields = ['cow', 'customer', 'date', 'quantity_liters']

# Feeding Record Form
class FeedingRecordForm(forms.ModelForm):
    class Meta:
        model = FeedingRecord
        fields = ['cow', 'date', 'food_type', 'quantity_kg', 'price']