from django.urls import path
from posts import views

urlpatterns = [
    path("", views.get_index, name="index-page"),
    path("test/", views.test_page, name="test-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("about/", views.get_about, name="about-page"),
]