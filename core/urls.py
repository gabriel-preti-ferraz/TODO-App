from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('todo/', include('todo.urls')),
    path('', include('index.urls'))
]
