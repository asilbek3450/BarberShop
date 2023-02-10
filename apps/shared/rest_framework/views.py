from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def perform_authentication(self, request):
        super().perform_authentication(request)
        if not self.request.user.is_anonymous:
            self.user = self.request.user
