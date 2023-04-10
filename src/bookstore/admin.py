from django.contrib import admin
from bookstore.models import Book


class BookStoreAdmin(admin.AdminSite):
    site_header = "Book Store Admin"
    index_title = "Book Store"
    site_title = "Book Store By Sahadat"

bookstore_admin = BookStoreAdmin(name="bookstore_admin")


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']


bookstore_admin.register(Book, BookAdmin)