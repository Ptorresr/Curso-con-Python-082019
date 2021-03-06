from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prestamo/nuevo/", views.nuevo_prestamo, name="nuevo_prestamo"),
    path("prestamo/<int:idPrestamo>/libros/elimina/<int:idLibro>/",
        views.elimina_libros_prestamo, name="elimina_libros_prestamo"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
