from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from user.permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrAnonymousUser, IsOwnerOrAdmin
from user.models import User
from user.serializer import UserSerializer




class MyObtainAuthToken(ObtainAuthToken):
    request = None
    format_kwarg = None



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):



        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':

            permission_classes = [IsAdminUser]
        elif  self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrAdmin]

        elif self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]

        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        #print("permission_classes :", permission_classes)

        return [permission() for permission in permission_classes]


class LoginView(ViewSet):

    serializer_class = AuthTokenSerializer



    @staticmethod
    def create(request):

        return MyObtainAuthToken().post(request=request)


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
