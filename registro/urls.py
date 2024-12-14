from django.urls import path , include
from registro.views import SignUpView, home


urlpatterns = [
    path("accounts/",include('django.contrib.auth.urls')),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("",home,name="home")

]
    