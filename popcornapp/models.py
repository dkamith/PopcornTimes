from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    duration=models.PositiveIntegerField()
    release_date=models.DateField()
    genre=models.ManyToManyField(Genre)
    language=models.CharField(max_length=50)
    rating=models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return self.title
class Theatre(models.Model):
    name=models.CharField(max_length=150)
    city=models.CharField(max_length=50)
    address=models.TextField()

    def __str__(self):
        return f"{self.name} - {self.city}"
    
class Screen(models.Model):
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE,related_name='screens')
    name=models.CharField(max_length=50)
    total_seats=models.IntegerField()

    def __str__(self):
        return f"{self.theatre.name}-{self.name}"
    
class Seat(models.Model):
    SEAT_TYPE=(("REGULAR","Regular"),
               ("PREMIUM","Premium"),
               ("RECLINER","Recliner"),)
    screen=models.ForeignKey(Screen,on_delete=models.CASCADE,related_name='seats')
    seat_number=models.CharField(max_length=10)
    seat_type=models.CharField(max_length=20,choices=SEAT_TYPE)
    price=models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        unique_together=("screen","seat_numer")


    def __str__(self):
        return f"{self.screen.name}-{self.seat_number}"

class show(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    Screen =models.ForeignKey(Screen,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} | {self.start_time}"
    
class Booking(models.Model):
    pass
    

    



