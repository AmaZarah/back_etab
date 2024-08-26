
from django.urls import path
from teacher.views import list_teacher, add_teacher, edit_teacher
  


app_name = "teacher"

urlpatterns =[
    path('',add_teacher, name='addteacher'),
    path('llistteacher',list_teacher, name='llistteacher' ),
    path('editteacher',edit_teacher, name='editteacher')
   
]