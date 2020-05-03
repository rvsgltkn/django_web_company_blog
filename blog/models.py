from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Language(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=5)

    class Meta:
        db_table = 'adek_language'
        ordering = ('-id',)

    def __str__(self):
        return self.name

class Index(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, blank=True, null=True)
    introduction=models.CharField(max_length=200, blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    created_date=models.DateField(default=timezone.now)
    image_url=models.FileField(upload_to='uploads/index/')
    language=models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_index'
        ordering=('-id',)


    def __str__(self):
        return self.title



class Service(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, blank=True, null=True)
    introduction=models.CharField(max_length=200, blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    created_date=models.DateField(default=timezone.now)
    image_url=models.FileField(upload_to='uploads/service/')
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_services'
        ordering=('-id',)


    def __str__(self):
        return self.title


class Testimonial(models.Model):
    id=models.AutoField(primary_key=True)
    customer=models.CharField(max_length=100, blank=True, null=True)
    description=models.CharField(max_length=200, blank=True,null=True)
    created_date=models.DateField(default=timezone.now)
    image_url=models.FileField(upload_to='uploads/testimonial/')
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_testimonial'
        ordering=('-id',)


    def __str__(self):
        return self.customer



class Gallery(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, blank=True, null=True)
    description=models.CharField(max_length=200, blank=True,null=True)
    created_date=models.DateField(default=timezone.now)
    image_url=models.FileField(upload_to='uploads/gallery/')
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_gallery'
        ordering=('-id',)


    def __str__(self):
        return self.title


class About(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    created_date=models.DateField(default=timezone.now)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_about'
        ordering=('id',)


    def __str__(self):
        return self.title



class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=200, blank=True, null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    tel=models.CharField(max_length=100,blank=True,null=True)
    description = RichTextUploadingField(blank=True, null=True)
    created_date=models.DateField(default=timezone.now)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    class Meta:
        db_table='adek_contact'
        ordering=('id',)


    def __str__(self):
        return self.company_name


PAGE_CHOICES=(
    ('index','Index'),
    ('about','About'),
    ('service','Service'),
    ('contact','Contact'),
)
class Banner(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, blank=True, null=True)
    image_url = models.FileField(upload_to='uploads/banner/')
    page=models.CharField(choices=PAGE_CHOICES, max_length=20)
    created_date=models.DateField(default=timezone.now)

    class Meta:
        db_table='adek_banner'
        ordering=('id',)


    def __str__(self):
        return self.title

# class Post(models.Model):
#     author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title=models.CharField(max_length=200)
#     text=models.TextField()
#     created_date=models.DateField(default=timezone.now)
#     published_date=models.DateField(blank=True,null=True)
#
#     def publish(self):
#         self.published_date=timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
#
# class Comment(models.Model):
#     post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
#     author=models.CharField(max_length=200,default="Anonymus")
#     text=models.TextField(blank=True,null=True)
#     created_date=models.DateTimeField(default=timezone.now)
#     approved_comment=models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment=True
#         self.save()
#
#     def __str__(self):
#         return self.text


