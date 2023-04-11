
from django.contrib import admin
from django.urls import path
from blog.admin import blog_admin
from bookstore.admin import bookstore_admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/admin/', blog_admin.urls),
    path('bookstore/admin/', bookstore_admin.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# admin.site.index_title = "Dj Book Store"
# admin.site.site_title = "Book Store"
# admin.site.site_header = "Book Store Admin"
