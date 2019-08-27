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


class PhotoCreate(CreateView):
    model = Photo
    fields = ['image','description']
    template_name = 'photo/photo_upload.html'
    #Todo : 작성자 설정
    # 클래스형 뷰에서 어떤 로직을 수정하려면 오버라이드 한다
    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['description']
    template_name = 'photo/photo_modify.html'


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'


from django.urls import reverse_lazy
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_list')
    template_name = 'photo/photo_delete.html'


