from django.urls import path
from . import views
from . import url_handlers

urlpatterns = [
    path("pojistenci_list/", views.PojistenciList.as_view(), name="pojistenci_list"),
    path("<int:pk>/pojistenec_detail/", views.PojistenecDetail.as_view(), name="pojistenec_detail"),
    path("pojistenec_novy/", views.PojistenecNovy.as_view(), name="pojistenec_novy"),
    path("", url_handlers.index_handler),
]
