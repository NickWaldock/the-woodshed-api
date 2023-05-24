from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile_id')
    profile_image = serializers.ReadOnlyField(source='owner.profile_image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.is_owner
    
    class Meta:
        model = Post
        fields = "__all__"
