from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tasks/', include('tasks.urls', namespace="tasks")),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
]
