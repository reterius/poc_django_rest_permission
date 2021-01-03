from rest_framework.serializers import ModelSerializer, CurrentUserDefault
from user.models import User


class UserSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'view' in self.context and self.context['view'].action in ['update']:

            # Kullanıcı eğer admin statüsünde değilse group bilgisini set edemez
            if self.context['request'].user.groups.name != "admin":
                self.fields.pop('groups', None)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'groups')
        # read_only_fields = ('groups',)
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user
