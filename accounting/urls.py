from django.conf.urls import url

from accounting.apis import GetSalesReportApi


urlpatterns = [
    url(
        regex=r'^sales-report/$',
        view=GetSalesReportApi.as_view(),
        name='get-sales-report'
    ),
]
