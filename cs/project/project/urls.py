from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('products/', include('products.urls')),
    path('management/', include('management.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='account_logout'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_header= 'Computer Souq Admins'
admin.site.site_title= 'Computer Souq Admins'
admin.site.index_title= 'Computer Souq Admins'