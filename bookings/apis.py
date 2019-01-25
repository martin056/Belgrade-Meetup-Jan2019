from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin

from locations.mixins import WithLocation

from bookings.selectors import get_arrivals


class GetArrivalsApi(WithLocation, LoginRequiredMixin, APIView):
    login_url = '/admin/'

    def get(self, request, *args, **kwargs):
        data = get_arrivals(location=self.location, user=request.user)

        return Response(data=data)
