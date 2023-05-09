from rest_framework import serializers
from posts.models import Post, Group, Comment, User
import base64
from django.core.files.base import ContentFile
from djoser.serializers import UserSerializer


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name')


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)




















################################################################
# from rest_framework import serializers, status
# from posts.models import Cat, Owner, Achievement, AchievementCat


# class AchievementSerializer(serializers.ModelSerializer):
    # achievement_name = serializers.CharField(source='name')


#     class Meta:
#         model = Achievement
#         fields = ('id', 'achievement_name')


# class CatSerializer(serializers.ModelSerializer):
#     achievements = AchievementSerializer(many=True, required=False)
#     # owner = serializers.StringRelatedField(read_only=True)
#     age = serializers.SerializerMethodField()


#     class Meta:
#         model = Cat
#         fields = ('id', 'name', 'color', 'birth_year', 'owner', 'achievements')

#     def create(self, validated_data):
#         if 'achievements' not in self.initial_data:
#             cat = Cat.objects.create(**validated_data)
#             return cat
#         achievements = validated_data.pop('achievements')

#         cat = Cat.objects.create(**validated_data)

#         for achievement in achievements:
#             current_achievement, status = Achievement.objects.get_or_create(
#                 **achievement)
#             AchievementCat.objects.create(
#                 achievement=current_achievement, cat=cat)
#         return cat


# class OwnerSerializer(serializers.ModelSerializer):

#     cats = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Owner
#         fields = ('id', 'first_name', 'last_name', 'cats')