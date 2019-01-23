from rest_framework.views import APIView
from rest_framework.response import Response

from locations.mixins import WithLocation

from bookings.selectors import get_arrivals


class GetArrivalsApi(WithLocation, APIView):
    def get(self, request, *args, **kwargs):
        data = get_arrivals(location=self.location, user=request.user)

        return Response(data=data)
