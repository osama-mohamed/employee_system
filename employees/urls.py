from django.conf.urls import url, include

from .views import AddEmployeeView

urlpatterns = [
    url(r'^add/$', AddEmployeeView.as_view(), name='add'),
]
