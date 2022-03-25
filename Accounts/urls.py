from django.urls import path
from . import views
urlpatterns=[
    path('1/1' ,views.newstudent, name='newstudent'),
    path('1/2', views.neworphan,name='neworphan'),
    path('1/3', views.newfamily, name='newfamily'),
    path('2/1',views.newmedicine, name='newmedicine'),
    path('2/2',views.newpatient, name='newpatient'),
    path('3/1', views.elec, name='elec')]
