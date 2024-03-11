from django.contrib import admin
from django.urls import path, include
from user.views import signup, dashboard, login_view, home # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Define URL pattern for the root URL
    path('login/', login_view, name='login'),  # Define URL pattern for login view
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]

# Include app URLs if needed
# urlpatterns += [path('', include('user.urls'))]

# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
