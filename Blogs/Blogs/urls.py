
from django.contrib import admin
from django.urls import path
from Main.views import landingpage
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage, name="op"),
    path('login/', LoginView.as_view(), name="login" )
]
