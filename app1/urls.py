
from django.urls import path,include
from  app1 import views
urlpatterns = [
    path('index/',views.StudentView.as_view(),name='student'),
    path('login/',views.Loginpage.as_view(),name='login'),
    path('about/',views.About,name='about'),
    path('course/',views.course,name='course'),
    path('instructor/',views.instructor,name='instructor'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('mycourses/',views.mycourses,name='mycourses'),
    path('itcourse/',views.Itcourses,name="it")

]

