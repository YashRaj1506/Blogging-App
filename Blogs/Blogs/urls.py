
from django.contrib import admin
from django.urls import path
from Main.views import landingpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage, name="op"),
]
