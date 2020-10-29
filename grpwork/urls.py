from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url('^api/profiles/$',views.ProfileList.as_view(),name='profile_list'),
    url('^api/neighbourhood/$',views.NeighbourhoodList.as_view(),name='neighbourhood_list'),
    url('^api/business/$',views.Business_centresList.as_view(),name='business_center_list'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
