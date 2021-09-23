"""doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from prescription import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create', views.CreatePrescription.as_view(), name='create'),
    path('pre_pres/<int:pk>', views.PrePresShow.as_view(), name='pre_pres'),
    path('update_medicine/<int:pk>', views.UpdateMedicineView.as_view(), name='update_medicine'),
    path('old_patient_search/', views.old_patient_search,name='old_patient_search'),
    path('old_patient_update/<int:pk>', views.OldPatientUpdate.as_view(), name='old_patient_update'),
    path('add_medicine/<int:pk>', views.AddMedicineView.as_view(), name='add_medicine'),
    path('print_pres/<int:pk>', views.PrintPresView.as_view(), name='print_pres'),
    path('search/', views.search,name='search'),
    path('print', views.print_search_view,name='print'),
    path('patient_list/', views.PatientList.as_view(), name='patient_list'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('', include('accounts.urls')),
]
