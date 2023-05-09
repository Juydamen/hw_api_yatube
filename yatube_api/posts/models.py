from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()     # стандартная модель Django


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    description = models.TextField()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='posts/image/', null=True,
                              blank=True)

    group = models.ForeignKey(
        Group, related_name='posts', null=True, blank=True, on_delete=models.SET_NULL)


class Comment(models.Model):
    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)

    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, related_name='follow', on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name='folow', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.following}'
















################################################################
# from django.db import models


# class Achievement(models.Model):
#     name = models.CharField(max_length=64)

#     def __str__(self):
#         return self.name


# class Owner(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


# class Cat(models.Model):
#     name = models.CharField(max_length=16)
#     color = models.CharField(max_length=16)
#     birth_year = models.IntegerField()

#     owner = models.ForeignKey(
#         Owner, related_name='cats', on_delete=models.CASCADE)

#     achievements = models.ManyToManyField(
#         Achievement, through='AchievementCat')

#     def __str__(self):
#         return self.name


# class AchievementCat(models.Model):
#     achievement = models.ForeignKey(
#         Achievement, on_delete=models.CASCADE)

#     cat = models.ForeignKey(
#         Cat, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.achievement} {self.cat}'
