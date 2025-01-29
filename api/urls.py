from django.urls import path
from api.views import (
    RegisterApiView,
    LoginApiView,
    DoctorListApiView,
    DoctorDetailApiView,
    DoctorFilterView,
    NewsApiView,
)

urlpatterns = [
    path("register/", RegisterApiView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),

    # Doctor routes
    path("doctors/", DoctorListApiView.as_view(), name="doctors-list"),
    path("doctors/<int:pk>/", DoctorDetailApiView.as_view(), name="doctors-detail"),

    # Doctor search route
    path("search/", DoctorFilterView.as_view(), name="doctor-search"),

    # News routes
    path("news/", NewsApiView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsApiView.as_view(), name="news-detail"),
]
