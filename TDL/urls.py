from django.urls import path,include
from . import views

app_name = 'tasks'

urlpatterns = [
    path('index', views.index, name='index'),
    path('mark_complete/<int:task_id>/', views.mark_complete, name='mark_complete'),
    path('tasks/delete/<int:task_id>/',views.delete_task, name='delete_task'),
    path('tasks/edit/<int:task_id>/',views.edit_task,name ='edit_task'),
    path('formu',views.formu, name = 'formu'),

 

]
