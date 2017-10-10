from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_Name = models.CharField(max_length=255)
    user_Age = models.IntegerField()
    user_email = models.CharField(max_length=255)
    user_Contactnumber = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Show(models.Model):
    show_Name = models.CharField(max_length=255)
    show_id = models.IntegerField(primary_key = True)
    ratings_id = models.ForeignKey('Ratings', on_delete = models.CASCADE)
    runtime_id = models.ForeignKey('Runtime', on_delete = models.CASCADE)
    reviews_id = models.ForeignKey('Reviews', on_delete = models.CASCADE)
    director_id =models.ForeignKey('Director', on_delete = models.CASCADE)
    budget_id = models.ForeignKey('Budget', on_delete = models.CASCADE)
    genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)



class Ratings(models.Model):
    ratings_id = models.IntegerField(primary_key = True)
    ratings = models.IntegerField()
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)



class Plan(models.Model):
    plan_Name = models.CharField(max_length=255)
    plan_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)



class Director(models.Model):
    director_id = models.IntegerField(primary_key = True)
    director_Name = models.CharField(max_length=255)
    director_Bio = models.CharField(max_length=555)



class Runtime(models.Model):
    runtime_id = models.IntegerField(primary_key = True)
    runtime = models.IntegerField()
    show_id = models.ForeignKey('Show', on_delete = models.CASCADE)



class Genre(models.Model):
    genre_id = models.IntegerField(primary_key = True)
    genre_Type = models.CharField(max_length=255)



class Payment(models.Model):
    payment_id = models.IntegerField(primary_key = True)
    payment_Amount = models.IntegerField()
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    plan_id = models.ForeignKey('Plan', on_delete = models.CASCADE)



class Budget(models.Model):
    budget_id = models.IntegerField(primary_key = True)
    budget_Amount = models.IntegerField()



class Reviews(models.Model):
    reviews_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
