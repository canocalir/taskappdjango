from django.urls import path, include
from .views import  todo_home, TodoMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home),
    # path('list-create/', Todos.as_view()),
    # path('detail/<int:pk>', TodoDetail.as_view()),
    path('', include(router.urls))
]