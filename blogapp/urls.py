
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('articles/',include('article.urls')),
    path('tinymce/', include('tinymce.urls')),
]

from django.contrib import admin

admin.site.site_header = 'Articles Paradigm'                    # default: "Django Administration"
admin.site.index_title = 'Articles Paradigm'                 # default: "Site administration"
admin.site.site_title = 'Articles Paradigm adminsitration' # default: "Django site admin"

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)