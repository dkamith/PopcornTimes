from django.db import models
from django.contrib.auth.models import User

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
        unique_together=("screen","seat_number")


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
    BOOKING_STATUS=(("PENDING","Pending"),
                    ("CONFIRMED","Confirmed"),
                    ("CANCELLED","Cancelled"),
                    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    show=models.ForeignKey(show,on_delete=models.CASCADE)
    booking_time=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=BOOKING_STATUS)
    total_amount=models.DecimalField(max_digits=8,decimal_places=3)

    def __str__(self):
        return self.user.username

class Tickets(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    seat=models.ForeignKey(Seat,on_delete=models.CASCADE)
    class Meta:
        unique_together=("booking","seat")
    def __str__(self):
        return f"{self.booking.id}-{self.seat.seat_number}"
    
class Payment(models.Model):
    PAYMENT_CHOICE=(("SUCCESS","Success"),
                    ("FAILED","Failed"),
                    ("PENDING","Pending"),
                    )
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=4)
    status=models.CharField(max_length=50,choices=PAYMENT_CHOICE)
    payment_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"payment {self.payment_id}"
    
    

    



