from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page.as_view(), name='home_page'),
    path('index', home_page.as_view(), name='home_page'),
    path('login', login_page.as_view(), name='login_page'),
    path('artical', artical_page.as_view(), name='artical_page'),
    path('writer', writer_page.as_view(), name='writer_page'),
    path('manage', manage_page.as_view(), name='manage_page'),
    path('signin', login_page_function_login.as_view(), name='login_page_function_login'),
    path('signout', login_page_function_signout.as_view(), name='login_page_function_signout'),
    path('upload', write_page_function_upload.as_view(), name='write_page_function_upload'),
    path('search', home_page_function_search.as_view(), name='home_page_function_search'),
    path('evaluate', artical_page_function_good.as_view(), name='artical_page_function_good'),
    path('editor', manage_page_function_information.as_view(), name='manage_page_function_information'),
    path('delete', manage_page_function_delete.as_view(), name='manage_page_function_delete'),
]
