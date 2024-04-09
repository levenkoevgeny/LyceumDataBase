from django.urls import path
from . import views

app_name = 'applicant'

urlpatterns = [
    path('', views.applicant_list, name='applicant-list'),
    path('init-db', views.init_db, name='init-db'),
    path('add-form', views.add_applicant, name='applicant-add-form'),
    path('delete/<pk>/', views.ApplicantDelete.as_view(), name='applicant-delete'),
    path('update/<applicant_id>/', views.update_applicant, name='applicant-update-form'),
]