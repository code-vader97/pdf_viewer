from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.index, name='index'),
    path('view_pdf/<str:order_type>/<str:page_number>', views.pdf_view, name='view_pdf'),
]