from django.db import models

# Create your models here.
# 모델은 클래스 형태
# 테이블 이름 앱이름_모델이름(전체 소문자)
# O.R.M
# 객채와 관계형 DB를 연결하는 것
# python manage.py makemigrations bmi
# python manage.py migrate bmi 0001

# 공부 포인트
# 1. 기본필드들
# 2. 커스텀 필드
# 3. https://docs.djangoproject.com/en/2.2/ref/models/fields/
class BMI(models.Model):
    #이름 , 키 , 체중, BMI
    name = models.CharField(max_length=20, verbose_name="회원명")
    height = models.FloatField(verbose_name="신장")
    weight = models.FloatField(verbose_name="체중")
    bmi_level = models.FloatField(blank=True, null=True, verbose_name="비만도")

## f == 3.7 부터 사용 가능
    def __str__(self):  # --> 던더 메소드 == 오버라이드
        return f"{self.name}의 키 {self.height} 몸무게 {self.weight}"

## super -- 오버라이드
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

# bmi = 체중 / 키(m단위)의 제곱
        self.bmi_level = self.weight / (self.height/100)**2
        return super().save(force_insert,force_update,using,update_fields)

# 1. 프론트에서 Form 을 이용해서 데이터를 전달
# 2. 데이터를 받은 view 에서 데이터를 검증
# * Validation method 직전에
# *데이터를 할당
# * 작성자 지정

# 3. Save - 모델 - Save method 에서
# 4. Signal - 데이터베이스에 저장하기 전 후,