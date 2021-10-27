from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post')

    class Meta:
        model = Comment
        fields = ('post', 'post_id',
                  'body', 'owner', 'photo')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'body','comments',
                  'post_url', 'owner', 'photo')
