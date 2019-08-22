from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#커스텀 모델을 사용할 때(주민번호, 휴대폰 번호... 등등, 바뀔가능성이 있거나 확실히 바뀔 가능성이 있는 경우 이용)

"""
admin = User.objects.get(pk=1)
admin.photo_set
admin.photos = 내가 올린 사진들을 모두 가져옴
"""
##jango crontab --> 리눅스 크론잡 보다는 성능이 떨어짐 , e.g) 매주 월요일 마다 발송되는 DM

# Create your models here.

class Photo(models.Model):
    #필드들
    #owner = models.ForeignKey(참조할 모델,on_delete,related_name)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='photos')
    #CASCADE:탈퇴하면 모두 사진 지운다, PROTECT:사진을 지우기 전에는 탈퇴 못한다, SET_NULL:값을 비워놓겠다, SET_DEFAULT:필드에 설정되어 있는 기본 값으로 하겠다,
    # DO_NOTHING:탈퇴해도 아무것도 안하겠다, SET():여기에 설정 된 값으로 쓰겠다.
    #ORM 기능을 자동으로 활성화하기 위하여 Foreignkey를 이용함
    #e.g) 작성자가 어드민인 사진만 가져오겠다....가 가능해짐 >> Primary 키는 안됨
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    # 어디에 저장할 것이냐? 저장경로 - 옵션
    # 저장할 스토리지 - settings.py
    # 사이즈 - 제한하거나 변경하는 - 별도 모듈
    # 용량 - 웹 서버 옵션에서 제어
    # 형식 - 장고 혹은 웹서버에서 제한
    # 갯수 - 필드 당 1개 파일
    # 파일명 - 정해진 형식으로 변환해서 저장한다
    #
    description = models.TextField(blank=True) #비워놔도 괜찮다, 글 쓰는 부분
    created = models.DateField(auto_now_add=True) #웹서버들은 서버 시간을 올려서 시간을 가져옴 #처음에 글을 올렸을때만 시간이 갱신됨
    updated = models.DateField(auto_now=True) #수정했을때만 시간이 갱신됨
    #메서드들
    def __str__(self):
        return self.owner.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    #사진을 올린 시간
    #메타클레스
    class Meta:
        ordering = ['-updated' , '-created']

#python manage.py makemigrations -> 변경사항을 추척해서 마이그레이션 파일을 만든다
#python manage.py migrate --> 만들어진 쿼리를 실행한다

### foreign_key - 외래키 - 참조키
#주 키를 참조하고 있는 테이블

### primary_key - 주키

