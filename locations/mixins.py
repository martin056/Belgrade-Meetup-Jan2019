from rest_framework.generics import get_object_or_404

from locations.models import Location


class WithLocation:
    def dispatch(self, *args, **kwargs):
        self.location = get_object_or_404(Location, ref=self.kwargs.get('location_ref'))

        return super().dispatch(*args, **kwargs)
