from django.core.validators import MaxValueValidator, MinValueValidator
from Fariba_project.settings import AUTH_PASSWORD_VALIDATORS
from django_jalali.db import models as jmodels
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from Account.models import  Profile
from django.db import models
from django.utils.text import slugify
from django.db.models.fields import (BooleanField,
                                     DateTimeField,
                                     IntegerField,
                                     SmallIntegerField,)
from .utils import  (
                     POST_STATUS_TYPES,
                     POST_CATEGORY_TYPES,
                     post_image_path,
                     )

#-----------------------------------------Post model------------------------------------
class Post(models.Model) :
    slug = models.SlugField(allow_unicode=True, unique=True, null=True)
    author = models.ManyToManyField(Profile, verbose_name="نویسنده ", related_name="posts" , blank=True)
    m_time = jmodels.jDateTimeField(verbose_name="تاریخ عضویت ", auto_now_add=True ) #membership time
    edit_date = jmodels.jDateTimeField(verbose_name="تاریخ آخرین ویرایش ",  auto_now_add=True )  #last edit
    title = models.CharField(verbose_name="عنوان", max_length=50)
    su_des = models.CharField(verbose_name="توضیحات خلاصه",max_length=300 ) #summary description
    co_des = RichTextField(verbose_name="توضیحات کامل" ) #complete description
    state = models.PositiveSmallIntegerField(verbose_name="وضعیت", choices=POST_STATUS_TYPES, default=1)
    category = models.PositiveSmallIntegerField(verbose_name="دسته بندی", choices=POST_CATEGORY_TYPES, default=0 )

    height = models.IntegerField(null=True , blank=True)
    width = models.IntegerField(null=True, blank=True)
    img = models.ImageField(null=True, height_field='height', width_field='width', upload_to=post_image_path)


    def __str__ (self):
        return self.title
        
        

    def get_full_name(self):
        return self.first_name + "-" + self.last_name


    def get_image(self):
         return mark_safe('<img src="{}" alt="{}" width="100" height="100"  >'.format("/media/" + str(self.img), str(self.title)))
    get_image.short_description='عکس پست'

    

    def get_date(self):
            return self.m_time.strftime('%H:%m - %Y/%m/%d ')
    get_date.short_description = 'تاریخ عضویت'


    def get_edit_date(self):
        return self.edit_date.strftime('%H:%m - %Y/%m/%d ')
    get_edit_date.short_description = 'تاریخ آخرین ویرایش'


    def get_authors(self):
        authors = ''
        for author in self.author.all():
            authors = authors + ' ' + str(author)
        return authors
    get_authors.short_description = 'نویسندگان'



    def save(self, *args, **kwargs) : 
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


    class Meta : 
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering  = ['m_time'] 



#-----------------------------------------Comment model------------------------------------
class Comment(models.Model) :
    post = models.ForeignKey(Post, verbose_name="عنوان پست ", on_delete=models.CASCADE, related_name="comments" )
    user = models.ForeignKey(Profile, verbose_name=" نام کاربر", on_delete=models.SET_NULL, null=True)
    m_time = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True) #membership time
    message = models.TextField(verbose_name=" دیدگاه" ) 
    state = models.PositiveSmallIntegerField(verbose_name="وضعیت", choices=POST_STATUS_TYPES, default=1 )
    

    def __str__ (self):
        return str(self.user)


    def get_date(self):
        return self.m_time.strftime('%H:%m - %Y/%m/%d ')
    get_date.short_description = 'تاریخ ایجاد'


    class Meta : 
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering  = ['-m_time'] 


