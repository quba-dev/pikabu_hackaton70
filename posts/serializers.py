from rest_framework import serializers
from .models import Post, Vote, Comments



class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.email')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()
    # commentsa = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'body', 'poster', 'poster_id', 'created', 'votes', 'post_comments']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

    # def get_commentsa(self, post):
    #     return Comments.objects.filter(post=post)

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id']

class CommentsSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='poster.email')
    # post = serializers.ReadOnlyField(source='post.id')
    # comments = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        # fields = ['id', 'text', 'user', 'post', 'comments']
        # read_only_fields = ['post', 'user']
        fields = '__all__'


    # def get_comments(self, post):
    #     return Comments.objects.filter(post=post)


