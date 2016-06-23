from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    active  = models.BooleanField(default = True)
    category = models.CharField(max_length=50, default="linux")
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __unicode__(self):
        return self.post_title

class Comment(models.Model):
    comment_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField()
    mod_date = models.DateField()
    post = models.ForeignKey(Post)
    active = models.BooleanField(default = True)

    def __unicode__(self):
        return self.comment_text
