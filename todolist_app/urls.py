from django.urls import path
from todolist_app import views
urlpatterns = [
    path('',views.todolist,name='todolist'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
    path('done/<task_id>',views.done_task,name='done_task'),
    path('notdone/<task_id>',views.notdone_task,name='notdone_task'),
    
]
