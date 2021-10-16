from .views import UserView, CreateUserView, UpdateUserView, EventsView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view()),
    path('update-user', UpdateUserView.as_view()),
    path('get-all-events', EventsView.as_view()),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

