
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, generics

from rest_framework.permissions import IsAdminUser

from .models import Occurrence
from django.contrib.auth.models import User

# from snippets.permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, OccurrenceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OccurrenceList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        params = request.query_params

        if params:
            query_params = dict(params)
            if "author" in query_params:
                payload = Occurrence.objects.filter(
                    author__in=query_params["author"])
                serializers = OccurrenceSerializer(
                    payload, many=True).data
                return Response(serializers)
            elif "category" in query_params:
                payload = Occurrence.objects.filter(
                    category__in=query_params["category"])
                serializers = OccurrenceSerializer(
                    payload, many=True).data
                return Response(serializers)
            elif "distance" in query_params:

                payload = Occurrence.objects.filter(
                    distance_from_hq__lte=query_params["distance"][0])
                serializers = OccurrenceSerializer(
                    payload, many=True).data
                return Response(serializers)
            else:
                return self.list(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class OccurrenceDetail(
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
