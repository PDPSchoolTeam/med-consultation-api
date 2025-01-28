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
    path("doctors/", DoctorListApiView.as_view(), name="doctors-list"),  # plural route for list
    path("doctors/<int:pk>/", DoctorDetailApiView.as_view(), name="doctors-detail"),  # plural for consistency

    # Doctor search route
    path("search/", DoctorFilterView.as_view(), name="doctor-search"),

    # News routes
    path("news/", NewsApiView.as_view(), name="news-list"),  # plural route for list
    path("news/<int:pk>/", NewsApiView.as_view(), name="news-detail"),  # singular for a single item
]
