
from django.conf.urls import include, url
#from django.contrib.auth.views import login
from folders import views


urlpatterns = [
    ###### Display form for selecting Folder 
    url(r'^$',views.dirstruc, name='dirstruc'),

    ###### Sub Folders Urls
    url(r'^ajax/load-sub_directories/', views.subfoldes, name='sub_directories'),

    url(r'^ajax/load-sub_directories1/', views.subfoldes2, name='sub_directories1'),


    ##### List display of selected Folders and SubFolders
    url(r'^list/$', views.display_list, name='display_list'),

    ##### Redirect to Form
    url(r'^redirect/$', views.redirect, name='redirect'),


  
  ]