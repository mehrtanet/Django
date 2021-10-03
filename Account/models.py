from django.core.validators import MaxValueValidator, MinValueValidator
from Fariba_project.settings import AUTH_PASSWORD_VALIDATORS
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core import validators
from django.db import models
from django.db.models.fields import (BooleanField,
                                     DateTimeField, 
                                     IntegerField, 
                                     SmallIntegerField, )
from .utils import (
                    Profile_Gender,
                    profile_files_path ,
                    check_is_digit, )


#-------------------------------------- Profile model ------------------------------------
class Profile(models.Model) :
    user = models.OneToOneField(User, verbose_name="نام کاربر", on_delete=models.CASCADE, related_name="profile")
    m_time = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد",auto_now_add=True) #membership time
    age = models.PositiveSmallIntegerField(verbose_name="سن", null=True)
    n_code = models.CharField(verbose_name="کدملی", max_length=10, validators=[check_is_digit]) #national code
    phone = models.CharField(verbose_name="شماره تماس", max_length=11, validators=[check_is_digit])
    bio = RichTextField(verbose_name="درباره ی من", null=True , blank=True) #biography
    gender = models.CharField(verbose_name="جنسیت", choices=Profile_Gender, default="دیگری", max_length=6)
    is_writer = models.BooleanField(verbose_name=" نویسنده ", default=False)
    cv = models.FileField(verbose_name=" فایل رزومه", upload_to=profile_files_path)

    
    def get_date(self):
        return self.m_time.strftime('%H:%m - %Y/%m/%d ')
    get_date.short_description = 'تاریخ عضویت'
    

    def __str__(self):
        return self.user.get_full_name()


    def get_username(self):
        return self.user.username
    

    def get_first_name(self):
        return self.user.first_name
    

    def get_last_name(self):
        return self.user.last_name


    def get_full_name(self):
        return self.user.first_name + "-" + self.user.last_name
    get_full_name.short_description = "نام و نام خانوادگی"


    class Meta : 
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
        ordering  = ['-m_time'] 

