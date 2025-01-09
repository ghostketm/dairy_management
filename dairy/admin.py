from django.contrib import admin
from .models import (
    User, Customer, Bull, Heifer, Calf, Product, HealthRecord,
    ReproductionRecord, SalesRecord, MilkingRecord, FeedingRecord
)

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Bull)
admin.site.register(Heifer)
admin.site.register(Calf)
admin.site.register(Product)
admin.site.register(HealthRecord)
admin.site.register(MilkingRecord)
admin.site.register(FeedingRecord)
admin.site.register(ReproductionRecord)
admin.site.register(SalesRecord)