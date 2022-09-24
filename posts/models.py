from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
model = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(model, on_delete=models.PROTECT)
    edited_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk':self.pk})

    def update(self):
        return reverse('posts:update_post', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(model, on_delete=models.PROTECT)


    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("posts:posts_list")