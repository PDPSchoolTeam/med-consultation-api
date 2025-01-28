from rest_framework import serializers
from api.models import Doctor, User, News
from root import settings


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.avatar:
            representation['avatar'] = settings.BASE_URL + instance.avatar.url
        else:
            representation['avatar'] = None
        return representation


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_free', 'available_today', 'rating_percentage', 'patient_stories']


class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = News
        fields = ["user", "title", "img", "created_at"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.img:
            representation['img'] = settings.BASE_URL + instance.img.url
        else:
            representation['img'] = None
        return representation
