
from django.contrib import admin
from django.urls import path
from blog.admin import blog_admin
from bookstore.admin import bookstore_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/admin/', blog_admin.urls),
    path('bookstore/admin/', bookstore_admin.urls),
]



# admin.site.index_title = "Dj Book Store"
# admin.site.site_title = "Book Store"
# admin.site.site_header = "Book Store Admin"
