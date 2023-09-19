
from django.urls import path, include
from django.contrib import admin
from . import url_handlers


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", url_handlers.index_handler),
    path('pojisteni/', include('pojistovna_app.urls')),
]