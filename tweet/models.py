from django.db import models

from user.models import User

from .utils import TweetStatus


class Tweet(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tweet_content = models.TextField(blank=True)
    writed_at = models.DateTimeField(verbose_name='Writed At', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.IntegerField(choices=TweetStatus.statuses(), default=TweetStatus.PASSIVE)

    def get_tweet_status_label(self):
        return TweetStatus(self.status).name.title()

    REQUIRED_FIELDS = ['tweet_content']

    class Meta:
        verbose_name = 'tweet'
        verbose_name_plural = 'tweets'
