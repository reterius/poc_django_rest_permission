from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault, ValidationError
from tweet.models import Tweet


class TweetSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = (
            'id', 'tweet_content', 'writed_at', 'user', 'status')  # detay ve listelemelerde gözükecek property'ler
        model = Tweet

    def validate(self, attrs):
        if len(attrs['tweet_content']) > 150:
            raise ValidationError("Tweet content very long")
        elif len(attrs['tweet_content']) < 3:
            raise ValidationError("Tweet content very short")

        return attrs

    def create(self, validated_data):

        tweet = Tweet.objects.create(**validated_data)
        tweet.save()
        return tweet

    def update(self, instance, validated_data):

        # kwargs["user"] = self.fields["user"].get_default()

        instance.tweet_content = validated_data.get('tweet_content', instance.tweet_content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
