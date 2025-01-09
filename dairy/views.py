from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import (
    User, Customer, Bull, Heifer, Calf, Product, HealthRecord,
    ReproductionRecord, SalesRecord, MilkingRecord, FeedingRecord
)
from .forms import (
    UserForm, CustomerForm, BullForm, HeiferForm, CalfForm, ProductForm,
    HealthRecordForm, ReproductionRecordForm, SalesRecordForm, MilkingRecordForm, FeedingRecordForm
)

def home(request):
    return render(request, 'dairy/home.html')

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Generic CRUD Views Template
def list_view(model, template_name):
    @login_required
    @user_passes_test(is_admin)
    def view(request):
        objects = model.objects.all()
        return render(request, template_name, {'objects': objects})
    return view

def create_view(form_class, template_name, redirect_url):
    @login_required
    @user_passes_test(is_admin)
    def view(request):
        if request.method == 'POST':
            form = form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect(redirect_url)
        else:
            form = form_class()
        return render(request, template_name, {'form': form})
    return view

def update_view(model, form_class, template_name, redirect_url):
    @login_required
    @user_passes_test(is_admin)
    def view(request, pk):
        obj = get_object_or_404(model, pk=pk)
        if request.method == 'POST':
            form = form_class(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect(redirect_url)
        else:
            form = form_class(instance=obj)
        return render(request, template_name, {'form': form})
    return view

def delete_view(model, template_name, redirect_url):
    @login_required
    @user_passes_test(is_admin)
    def view(request, pk):
        obj = get_object_or_404(model, pk=pk)
        if request.method == 'POST':
            obj.delete()
            return redirect(redirect_url)
        return render(request, template_name, {'object': obj})
    return view

# User Views
user_list = list_view(User, 'dairy/user_list.html')
user_create = create_view(UserForm, 'dairy/user_form.html', 'user_list')
user_update = update_view(User, UserForm, 'dairy/user_form.html', 'user_list')
user_delete = delete_view(User, 'dairy/user_confirm_delete.html', 'user_list')

# Customer Views
customer_list = list_view(Customer, 'dairy/customer_list.html')
customer_create = create_view(CustomerForm, 'dairy/customer_form.html', 'customer_list')
customer_update = update_view(Customer, CustomerForm, 'dairy/customer_form.html', 'customer_list')
customer_delete = delete_view(Customer, 'dairy/customer_confirm_delete.html', 'customer_list')

# Bull Views
bull_list = list_view(Bull, 'dairy/bull_list.html')
bull_create = create_view(BullForm, 'dairy/bull_form.html', 'bull_list')
bull_update = update_view(Bull, BullForm, 'dairy/bull_form.html', 'bull_list')
bull_delete = delete_view(Bull, 'dairy/bull_confirm_delete.html', 'bull_list')

# Heifer Views
heifer_list = list_view(Heifer, 'dairy/heifer_list.html')
heifer_create = create_view(HeiferForm, 'dairy/heifer_form.html', 'heifer_list')
heifer_update = update_view(Heifer, HeiferForm, 'dairy/heifer_form.html', 'heifer_list')
heifer_delete = delete_view(Heifer, 'dairy/heifer_confirm_delete.html', 'heifer_list')

# Calf Views
calf_list = list_view(Calf, 'dairy/calf_list.html')
calf_create = create_view(CalfForm, 'dairy/calf_form.html', 'calf_list')
calf_update = update_view(Calf, CalfForm, 'dairy/calf_form.html', 'calf_list')
calf_delete = delete_view(Calf, 'dairy/calf_confirm_delete.html', 'calf_list')

# Product Views
product_list = list_view(Product, 'dairy/product_list.html')
product_create = create_view(ProductForm, 'dairy/product_form.html', 'product_list')
product_update = update_view(Product, ProductForm, 'dairy/product_form.html', 'product_list')
product_delete = delete_view(Product, 'dairy/product_confirm_delete.html', 'product_list')

# Health Record Views
health_list = list_view(HealthRecord, 'dairy/health_list.html')
health_create = create_view(HealthRecordForm, 'dairy/health_form.html', 'health_list')
health_update = update_view(HealthRecord, HealthRecordForm, 'dairy/health_form.html', 'health_list')
health_delete = delete_view(HealthRecord, 'dairy/health_confirm_delete.html', 'health_list')

# Reproduction Record Views
reproduction_list = list_view(ReproductionRecord, 'dairy/reproduction_list.html')
reproduction_create = create_view(ReproductionRecordForm, 'dairy/reproduction_form.html', 'reproduction_list')
reproduction_update = update_view(ReproductionRecord, ReproductionRecordForm, 'dairy/reproduction_form.html', 'reproduction_list')
reproduction_delete = delete_view(ReproductionRecord, 'dairy/reproduction_confirm_delete.html', 'reproduction_list')

# Sales Record Views
sales_list = list_view(SalesRecord, 'dairy/sales_list.html')
sales_create = create_view(SalesRecordForm, 'dairy/sales_form.html', 'sales_list')
sales_update = update_view(SalesRecord, SalesRecordForm, 'dairy/sales_form.html', 'sales_list')
sales_delete = delete_view(SalesRecord, 'dairy/sales_confirm_delete.html', 'sales_list')

# Milking Record Views
milking_list = list_view(MilkingRecord, 'dairy/milking_list.html')
milking_create = create_view(MilkingRecordForm, 'dairy/milking_form.html', 'milking_list')
milking_update = update_view(MilkingRecord, MilkingRecordForm, 'dairy/milking_form.html', 'milking_list')
milking_delete = delete_view(MilkingRecord, 'dairy/milking_confirm_delete.html', 'milking_list')

# Feeding Record Views
feeding_list = list_view(FeedingRecord, 'dairy/feeding_list.html')
feeding_create = create_view(FeedingRecordForm, 'dairy/feeding_form.html', 'feeding_list')
feeding_update = update_view(FeedingRecord, FeedingRecordForm, 'dairy/feeding_form.html', 'feeding_list')
feeding_delete = delete_view(FeedingRecord, 'dairy/feeding_confirm_delete.html', 'feeding_list')