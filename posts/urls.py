from django.urls import path
from . import views #引用此資料夾中的views

urlpatterns = [
    path('',views.index, name = "Index")
]
