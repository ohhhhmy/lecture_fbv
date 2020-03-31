from django import forms
from .models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder' : "15자 이내로 입력해주세요."}),
            'password' : forms.PasswordInput()
        }
        help_texts = {
            'username' : None,
        }
    #헬프 텍스트 딕셔너리로도 없앨 수 있음
    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, *kwargs)
    #     self.fields['username'].widget.attrs['maxlength'] = 15

        # for fieldname in ['username', 'password']:
        #     self.fields[fieldname].help_text = None
# 위젯 추가로 비밀번호 input 형식 사용 가능

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length= 20, widget = forms.PasswordInput())
    nickname = forms.CharField(max_length= 10)
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs = {
                'placeholder' : '15자 이내만 가능합니다!'
            }),
            'password' : forms.PasswordInput(),
        }


        
