# user/serializers.py
# user 모델 가져오기
from django.contrib.auth.models import User
# 장고 패스워드 검증 도구
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
# 토큰 모델
from rest_framework.authtoken.models import Token
# 이메일 중복 방지
from rest_framework.validators import UniqueValidator

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # 비밀번호 검증
    password=serializers.CharField(

        write_only=True,
        required=True,
        validators=[validate_password],
    )

    # 비밀번호 재확인
    password2=serializers.CharField(write_only=True,required=True)

    class Meta:
        model =User
        fields=('username','password','password2','email')


    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"비밀번호가 올바르지 않습니다."}
            )

        return data


    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return user