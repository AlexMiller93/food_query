from django.contrib import admin

from foods.models import Food, FoodCategory

# Register your models here.


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fields = [
        "category", "code", "name_ru", "cost", "is_publish", "additional"
    ]
    list_display = ["category", "cost", "name_ru"]
    search_fields = ["category", "name_ru", "cost"]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    fields = ["id", "name_ru", "order_id"]
    list_display = ["id", "name_ru"]
    search_fields = ["name_ru"]
