from django.db import models

class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=100, default="")
    user_name = models.CharField(max_length=150, default="")
    user_email = models.EmailField(default="", unique=True)
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f"Nickname: {self.user_nickname} | E-mail: {self.user_email}"

class UserProfile(models.Model):  # 1:1
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=30, blank=True, default="")

class Task(models.Model):  # 1:n
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

class Group(models.Model):  # n:n
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name="groups")
