from django.db import models
from django.contrib.auth.models import User
import  uuid


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='یوزر')
    name = models.CharField(max_length=200,null=True,blank=True,verbose_name='نام')
    email = models.EmailField(max_length=500,null=True,blank=True,verbose_name='ایمیل')
    short_bio = models.CharField(max_length=200,null=True,blank=True,verbose_name='معرفی کوتاه')
    username = models.CharField(max_length=200,null=True,blank=True,verbose_name='نام کاربری ')
    bio = models.TextField(null=True,blank=True,verbose_name='بیوگرافی')
    location = models.CharField(max_length=200,null=True,blank=True,verbose_name='محل زندگی')
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default="profiles/user-default.png",verbose_name='عکس پروفایل')
    social_github = models.CharField(max_length=200,null=True,blank=True,verbose_name='گیت هاب')
    social_twitter = models.CharField(max_length=200,null=True,blank=True,verbose_name='توئیتر')
    social_linkedin = models.CharField(max_length=200,null=True,blank=True,verbose_name='لینکدین')
    social_website = models.CharField(max_length=200,null=True,blank=True,verbose_name='وب سایت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'یوزر'
        verbose_name_plural = 'پروفایل'


class Skill(models.Model):

    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,verbose_name='یوز مربوط ')
    name = models.CharField(max_length=200,null=True,blank=True,verbose_name='نام ')
    description =models.TextField(null=True,blank=True,verbose_name='توضیحات ')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد ')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'