from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken

from api import views
urlpatterns=[
    path("users/",views.UserAPIView.as_view()),
    path("users/<str:id>/",views.UserAPIView.as_view()),
    path("employee/", views.EmployeeGenericAPIView.as_view()),
    path("employee/<str:id>/", views.EmployeeGenericAPIView.as_view()),

    # url(r'^login/', obtain_jwt_token),
    # path("obt/", ObtainJSONWebToken.as_view()),


]