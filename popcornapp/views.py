from django.shortcuts import render
from .serializers import Movieserializer,Theaterserializer,Seatserializer,Screenserializer,Showserializer,Paymentserializer,Ticketserializer,Bookserializer
from rest_framework import viewsets
from .models import Movie,Theatre,Screen,Show,Booking,Tickets,Payment,Seat
# Create your views here.
class Movieview(viewsets.ModelViewSet):
    queryset=Movie.objects.all().prefetch_related('genre')
    serializer_class=Movieserializer

class Theaterview(viewsets.ModelViewSet):
    queryset=Theatre.objects.all()
    serializer_class=Theaterserializer
class Screenview(viewsets.ModelViewSet):
    queryset=Screen.objects.all()
    serializer_class=Screenserializer
class SeatView(viewsets.ModelViewSet):
    queryset = Seat.objects.all().select_related('screen')
    serializer_class = Seatserializer

class ShowView(viewsets.ModelViewSet):
    queryset = Show.objects.all().select_related('movie', 'screen')
    serializer_class = Showserializer

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all().select_related('user', 'show')
    serializer_class = Bookserializer

class TicketView(viewsets.ReadOnlyModelViewSet):  
    queryset = Tickets.objects.all().select_related('booking', 'seat')
    serializer_class = Ticketserializer

class PaymentView(viewsets.ReadOnlyModelViewSet):  
    queryset = Payment.objects.all().select_related('booking')
    serializer_class = Paymentserializer




