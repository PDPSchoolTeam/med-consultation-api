from django.urls import path
from api.views import DoctorApiView, NewsApiView, DoctorFilterView, RegisterApiView,LoginApiView

urlpatterns = [
    path("register", RegisterApiView.as_view(), name="register"),
    path("login", LoginApiView.as_view(), name="login"),
    path('doctor', DoctorApiView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorApiView.as_view(), name='doctors-detail'),
    path("search", DoctorFilterView.as_view(), name='search'),
    path('news', NewsApiView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsApiView.as_view(), name='news-detail'),
]


