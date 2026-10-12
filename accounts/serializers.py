from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User

        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "role",
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            phone_number=validated_data.get("phone_number", ""),
            role=validated_data.get("role", "ORGANIZATION"),
        )

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)

    def validate(self, data):

        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("ایمیل یا رمز عبور اشتباه است.")

        if not user.is_active:
            raise serializers.ValidationError("این حساب کاربری غیرفعال است.")

        data["user"] = user

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "is_active",
        ]

        read_only_fields = [
            "id",
            "is_active",
        ]
