from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


class Production_yearAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Production_year._meta.fields]
    prepopulated_fields = {'slug': ('title',)}


    class Meta:
        model = Production_year

admin.site.register(Production_year, Production_yearAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    prepopulated_fields = {'slug': ('title',)}


    class Meta:
        model = Author

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    prepopulated_fields = {'slug': ('title',)}


    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class KinoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kino._meta.fields]
    prepopulated_fields = {'slug': ('name',)}


    class Meta:
        model = Kino

admin.site.register(Kino, KinoAdmin)


class PopularKinoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PopularKino._meta.fields]


    class Meta:
        model = PopularKino

admin.site.register(PopularKino, PopularKinoAdmin)


class RecommendationsKinoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RecommendationsKino._meta.fields]

    class Meta:
        model = RecommendationsKino


admin.site.register(RecommendationsKino, RecommendationsKinoAdmin)


class TrendKinoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TrendKino._meta.fields]

    class Meta:
        model = TrendKino


admin.site.register(TrendKino, TrendKinoAdmin)


class ScenarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Scenario._meta.fields]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Scenario


admin.site.register(Scenario, ScenarioAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)


class ProducerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producer._meta.fields]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Producer


admin.site.register(Producer, ProducerAdmin)


class SidebarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sidebar._meta.fields]

    class Meta:
        model = Sidebar


admin.site.register(Sidebar, SidebarAdmin)

