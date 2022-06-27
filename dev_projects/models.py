from django.db import models
from dev_users.models import Profile
import uuid
# Create your models here.

"""
    this is the Project model
"""
class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='مالک پروژه')
    title = models.CharField(max_length=200,verbose_name='عنوان')
    description = models.TextField(null=True,blank=True,verbose_name='توضیحات')
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg",verbose_name='تصویر')
    demo_link = models.CharField(max_length=2000, null=True,blank=True,verbose_name='دمولینک')
    source_link = models.CharField(max_length=2000, null=True,blank=True,verbose_name='آدرس لینک')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0 ,null=True ,blank=True)
    vote_ratio = models.IntegerField(default=0 ,null=True ,blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='پروژه'
        verbose_name_plural ='بخش پروژه'


class Review(models.Model):
    VOTE_TYPE =(
        ('up','Up vote'),
        ('down','Down Vote')
    )
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name = 'ارتباط با دوره ')
    body = models.TextField(null=True,blank=True,verbose_name = 'بدنه')
    value = models.CharField(max_length= 200,choices=VOTE_TYPE,verbose_name = 'مقدار')
    created = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ ایجاد')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return  self.value

    class Meta:
        verbose_name = ' بازبینی جدید'
        verbose_name_plural = 'بخش بازبینی'


class Tag(models.Model):

    name = models.CharField(max_length=200,verbose_name = 'نام تگ')
    created = models.DateTimeField(auto_now_add=True,verbose_name = 'زمان ایجاد')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = ' بخش تگ ها'
