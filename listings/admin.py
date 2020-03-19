from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', "realtors", 'title', 'is_published', 'price', 'list_date',)
    list_display_links = ('id', 'title', 'realtors')
    list_editable = ('is_published',)
    list_filter = ('realtors',)
    search_fields=('title','address','id','city','state','price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

# Register your models here.
