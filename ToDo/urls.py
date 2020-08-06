from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index' ),
    path('add_todo', views.add_todo,name='addtodo' ),
    path('delete/<int:todoid>', views.del_todo,name='deletetodo' ),
]
