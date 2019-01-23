from rest_framework.views import APIView
from rest_framework.response import Response

from locations.mixins import WithLocation

from accounting.selectors import get_sales_report


class GetSalesReportApi(WithLocation, APIView):
    def get(self, request, *args, **kwargs):
        data = get_sales_report(location=self.location, user=request.user)

        return Response(data=data)
