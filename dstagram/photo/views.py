from django.shortcuts import render

# Create your views here.

# 클래스형뷰I(CRUD) 함수형뷰(다른 구조를 만들어야 될때)
# 클래스형 뷰는 제네릭 뷰를 상속받아서 만든다.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

from .models import Photo
class PhotoList(ListView):
    model = Photo
    #앱이름/모델명_list.html
    template_name = 'photo/photo_list.html'

"""
- midware
뷰를 동작하기에 앞서 어떤 절차를 추가하고 싶을때
* 자주 실행하야 되는 공통된 절차가 있다면 코드를 중복 사용해야 한다 --> 그래서 아래의 2가지 기법을 이용함
1) decorator : 함수형 뷰에 이용
2) mixin : 클래스형 뷰
"""

from django.contrib.auth.mixins import LoginRequiredMixin


class PhotoCreate(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image','description']
    template_name = 'photo/photo_upload.html'
    #Todo : 작성자 설정
    # 클래스형 뷰에서 어떤 로직을 수정하려면 오버라이드 한다
    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class PhotoUpdate(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['description']
    template_name = 'photo/photo_modify.html'


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'


class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'


from django.urls import reverse_lazy
from django.shortcuts import redirect
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_list')
    template_name = 'photo/photo_delete.html'

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != request.user:
            print("유저 일치하지 않음")
            return redirect(object.get_absolute_url())
        return super().post(request,*args,**kwargs)


