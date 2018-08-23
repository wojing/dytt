from django.urls import path
from . import views

app_name="thunder"
urlpatterns = {
    path(r'<int:film_id>',views.detail,name="detail"),
    path(r'',views.index,name="index"),
}