from django.urls import path
from api.views import TableViewSet

urlpatterns = [
    path('get_table/', TableViewSet.as_view({'get': 'list'}), name='get_table')
]
