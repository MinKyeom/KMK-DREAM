# users/serializers.py


# 장고 기본 모델인 로그인 모델 가져오기
from django.contrib.auth.models import User
# 장고의 기본 패스워드 검증 도구
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

# 장고 기본 토큰 모델 사용
"""
차후 토큰에서 보안을 위해 토큰의 유효기간을 설정하는 방향을 고민하여 개선 방향 고민해보기!
당장은 기본 토큰 모델 사용
"""
from rest_framework.authtoken.models import Token

#이메일 중복 방지 검증 도구 
from rest_framework.validators import UniqueValidator


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    
    #  cf) django는 기본적으로 회원 서비스를 제공하고 있기 때문에 따로 모델링을 해줄 필요가 없다! 
    #  cf) User.objects.all(): User 모델 즉 데이터베이스를 가져온다라는 의미
    # 이메일 중복 방지를 위한 검증
    validators=[UniqueValidator(queryset=User.objects.all())]
    
  )
  
  # 비밀번호에 대한 검증
  password =serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password],
  )
  # 비밀번호 재확인을 위한 필드
  password2 = serializers.CharField(write_only=True, required=True) 
  
  """ 
  메타데이터라는 의미에서 클래스 이름 구현
  >cf) 단, 장고 rest_framework에서는 자동으로 데이터안의 데이터라는 의미인 metadata를 찾
  """
  class Meta:
    model = User
    fields = ('username','password','password2','email')

  # 비밀번호 일치 여부 확인
  def validate(self,data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match"} )
    
    return data
  
  def create(self,validated_data):
    # create 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성함
    user = User.objects.create_user(
      username = validated_data['username'],
      email=validated_data['email'],
    )
    
    user.set_password(validated_data['password'])
    user.save()
    token = Token.objects.create(user=user)
    
    return user
  
  