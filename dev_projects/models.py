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
        ordering = ['-vote_total','-vote_ratio','title']
        verbose_name ='پروژه'
        verbose_name_plural ='بخش پروژه'

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset =self.review_set.all().values_list('owner__id',flat=True)
        return queryset


    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes =reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    VOTE_TYPE =(
        ('up','Up vote'),
        ('down','Down Vote')
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,verbose_name='مالک پروژه')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name = 'ارتباط با کدام دوره ')
    body = models.TextField(null=True,blank=True,verbose_name = 'توضیحات')
    value = models.CharField(max_length= 200,choices=VOTE_TYPE,verbose_name = 'رای مثبت یا منفی')
    created = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ ایجاد')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return  self.value

    class Meta:
        unique_together = [['owner', 'project']]
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
