from django.contrib.auth import get_user_model
from django import forms

class RegisterForm(forms.ModelForm):
    #새로운 필드들
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    #추가로직 및 매서드
    def clean_password2(self): #clean_필드명으로 정해져 있음
        #valid 메서드가 실행될때
        #clean_date : 입력된 데이의 escaping 처리 등을 담당함
        cd = self.cleaned_data
        #self.request.POST.get('password2') - 안전하지 않은 데이터
        #입력받은 값을 -> cleaned -> hashing -> 비교
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords not matched!')
        return cd['password2']

    #메타클래스
    class Meta:
        model = get_user_model()
        #1.모델의 필드들
        #2.새로운 필드들
        # 써준 순서대로 나타남
        fields = ['username','password','password2','first_name','last_name','email']