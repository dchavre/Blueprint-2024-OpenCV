from django.db import models
import string
import random

# Create your models here.

def generate_unique_id():
    length = 10
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if TrashPost.objects.filter(code=code).count()==0:
            break
    
    return code

class TrashPost(models.Model):
    author = models.CharField(max_length=30)
    image = models.ImageField()
    location = models.CharField(max_length=100)
    post_id = models.CharField(max_length=10, default=generate_unique_id, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    garbage_num = models.IntegerField()

