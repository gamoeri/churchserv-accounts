from django.db import models
from django.conf import settings


# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False)
    description = models.TextField(null=False, default = '')
    default = models.TextField(null=False, default = '')
    
    def __unicode__(self):
        return self.name

class UserSnippet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "snippets")
    snippet_type = models.ForeignKey(Snippet, related_name = "user_snippets")
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    class Meta:
        ordering = ["user", "created"]
         