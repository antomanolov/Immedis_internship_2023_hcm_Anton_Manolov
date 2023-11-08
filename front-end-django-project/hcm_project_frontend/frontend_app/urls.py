from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
   path('', TemplateView.as_view(template_name= 'HR(admin)/middle-pages/index.html'), name='index page'),
   path('login/', TemplateView.as_view(template_name='login.html'), name='login lage'),
   path('register/', TemplateView.as_view(template_name = 'HR(admin)/middle-pages/add-employee.html'), name='add user'),
   path('profile/', TemplateView.as_view(template_name='HR(admin)/middle-pages/profile.html')),
   path('edit-user/', TemplateView.as_view(template_name='HR(admin)/middle-pages/edit-employee.html'), name='edit user page'),
   path('add-task/', TemplateView.as_view(template_name='HR(admin)/middle-pages/add-task.html'), name='add task page'),
   path('add-paycheck/', TemplateView.as_view(template_name='HR(admin)/middle-pages/submit-paycheck.html'), name='add paycheck page'),
   path('add-review/', TemplateView.as_view(template_name='HR(admin)/middle-pages/add-review.html'), name='add review page')
]
