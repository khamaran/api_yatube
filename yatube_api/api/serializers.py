from rest_framework import serializers

from posts.models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post', )
