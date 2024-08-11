from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
#User model

class User(AbstractUser):
    ROLES = (
        ('CUSTOMER', 'customer'),
        ('LANDLORD', 'landlord'),
        ('WEBMASTER', 'webmaster'),
    )
    GENDER = (
        ('MALE', 'Nam'),
        ('FEMALE', 'Nu'),
        ('OTHER', 'Khac'),
    )
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    gender = models.CharField(max_length=50, null=False, choices=GENDER)
    role = models.CharField(max_length=50, null=False, choices=ROLES)
    avatar = CloudinaryField(null = True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.get_full_name())

class RoomType(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()

class RoomImage(BaseModel):
    url = CloudinaryField()
    room_id = models.ForeignKey('Rooms',related_name='images',on_delete=models.CASCADE)


class Rooms(BaseModel):
    title = models.CharField(max_length=400)
    description = models.TextField()
    price = models.FloatField()
    max_people = models.IntegerField()
    status = models.BooleanField(default=True)
    landlord_id = models.ForeignKey(User, related_name='landlord', on_delete=models.CASCADE)
    location_id = models.ForeignKey('Locations', related_name='room_location', on_delete=models.SET_NULL, null=True)
    roomtype_id = models.ForeignKey('RoomType', related_name='room_type', on_delete=models.SET_NULL, null=True)

class Locations(models.Model):
    adress = models.TextField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    area = models.FloatField()
    latidue = models.FloatField()
    longtidue = models.FloatField()




