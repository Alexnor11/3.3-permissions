from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.permissions import IsOwnerOrReadOnly

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
# from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsOwnerOrReadOnly]

    def IsOwnerOrReadOnly(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "delete", "partial_update"]:
            return [IsAuthenticated()]
        return []
