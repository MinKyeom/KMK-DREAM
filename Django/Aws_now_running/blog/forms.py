from django import forms

# 마크다운 필드를 만들기 위해서
import markdown
from markdownx.fields import MarkdownxFormField
from markdownx.utils import markdown

# 로그인 데이터 검증 확인 여부 10_23
class LoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    # password = forms.CharField(min_length=4)

#마크다운 문서 폼 제작
class MyForm(forms.Form):
    title = forms.CharField(min_length=3)
    content = MarkdownxFormField()