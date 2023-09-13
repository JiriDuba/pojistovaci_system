from django.urls import path
from . import views

urlpatterns = [
    path("pojistenci/", views.pojisteni_list, name="pojisteni_list"),
    path("pojistenci/<int:pojisteni_id>/", views.pojisteni_detail, name="pojisteni_detail"),
    path("pojistenci/novy/", views.create_pojisteni, name="create_pojisteni"),
    path("pojistenci/edit/<int:pojisteni_id>/", views.edit_pojisteni, name="edit_pojisteni"),
    path("pojistenci/smazat/<int:pojisteni_id>/", views.delete_pojisteni, name="delete_pojisteni"),
]
