from time import perf_counter
from django.db import models
import uuid
def _generate():
    return str(uuid.uuid4())
# Create your models here.
class Task(models.Model):
    id = models.CharField(primary_key=True,unique=True,default=_generate(),max_length=300)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
