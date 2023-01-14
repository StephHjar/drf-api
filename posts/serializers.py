from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializer.ReadOnlyField(source='owner.username')
    is_owner = serializer.SerializerMethodField()
    profile_id = serializer.ReadOnlyField(source='owner.profile.id')
    profile_image = serializer.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image'
        ]
