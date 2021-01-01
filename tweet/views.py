from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from tweet.permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrAnonymousUser, IsOwnerOrAdmin
from tweet.models import Tweet
from tweet.serializer import TweetSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MyObtainAuthToken(ObtainAuthToken):
    request = None
    format_kwarg = None


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [TokenAuthentication]
    pagination_class = StandardResultsSetPagination

    def list(self, request):

        predicate = {}

        user_id = self.request.query_params.get('user_id')

        if user_id is not None:
            predicate['user_id'] = user_id

        data = Tweet.objects.filter(**predicate)

        page = self.paginate_queryset(data)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []

        if self.action == 'list':
            permission_classes = [IsAuthenticated]

        if self.action == 'create':
            permission_classes = [IsAuthenticated]

        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrAdmin, IsAuthenticated]

        return [permission() for permission in permission_classes]
