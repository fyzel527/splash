from django.contrib import admin
from django.urls import path
from splash.views import splash_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('splash/', splash_view, name='splash'),
]
