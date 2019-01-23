from django.conf.urls import url

from bookings.apis import GetArrivalsApi


urlpatterns = [
    url(
        regex=r'^arrivals/$',
        view=GetArrivalsApi.as_view(),
        name='get-arrivals'
    ),
]
