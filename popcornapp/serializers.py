from rest_framework import serializers
from .models import Movie,Theatre,Screen,Payment,Show,Tickets,Seat,Booking

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"

class Theaterserializer(serializers.ModelSerializer):
    class Meta:
        model=Theatre
        fields="__all__"
class Seatserializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields="__all__"

class Showserializer(serializers.ModelSerializer):
    class Meta:
        model=Show
        fields="__all__"
class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model=Tickets
        fields="__all__"

class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"
class Screenserializer(serializers.ModelSerializer):
    class Meta:
        model=Screen
        fields="__all__"
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"

    
