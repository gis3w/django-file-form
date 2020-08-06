from django.urls import path
from django.contrib.auth.views import LoginView

from . import views


urlpatterns = (
    path('', views.ExampleView.as_view(), name='example'),
    path('success', views.ExampleSuccessView.as_view(), name='example_success'),
    path('multiple', views.MultipleExampleView.as_view(), name='multiple_example'),
    path('form_set', views.FormSetExampleView.as_view(), name='form_set_example'),
    path('without_js', views.WithoutJsExampleView.as_view(), name='without_js_example'),
    path('multiple_without_js', views.MultipleWithoutJsExampleView.as_view(), name='multiple_without_js_example'),
    path('wizard', views.WizardExampleview.as_view(), name='wizard_example'),
    path('login/', LoginView.as_view(template_name='admin/login.html')),
    path('placeholder', views.PlaceholderView.as_view(), name='placeholder_example'),
)
