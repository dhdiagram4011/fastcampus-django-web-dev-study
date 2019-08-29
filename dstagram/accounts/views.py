from django.shortcuts import render

# Create your views here

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        # 회원 가입 완료 버튼을 누른 후 회원 정보를 DB 에 저장하는 단계
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False) #인스턴스는 만들지만 데이터베이스에는 저장하지 않음(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user':new_user})
    else:
        # 회원가입 페이지에 접속했을 때 가입 폼이 보이는
        form = RegisterForm()
    return render(request, 'accounts/register.html',{'form':form})
