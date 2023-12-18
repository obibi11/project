from django.urls import path
from myapp.views import user_view, post_view, my_view

urlpatterns = [
    path('api/users/<int:user_id>/', user_view, name='user_view'),
    path('api/post/', post_view, name='post_view'),
    path('my-endpoint/', my_view, name='my_view'),

    # Додайте інші маршрути тут
]
