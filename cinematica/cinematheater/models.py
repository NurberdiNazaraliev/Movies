from django.db.models import Sum
from django.utils import timezone

from django.db import models
from movies.models import Movie
# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    open_time = models.TimeField()
    close_time = models.TimeField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    room_size = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    col_number = models.IntegerField(default=1)

    class Meta:
        unique_together = ('room', 'row_number', 'col_number')


    def __str__(self):
        return f"Row {self.row_number}, column {self.col_number} in {self.room.name}"


class MovieShow(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} in {self.room.name} at {self.show_time}"



class Ticket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket for {self.seat} for {self.show}"


class Reservation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=1, default=10.00, null=True, blank=True)

    def __str__(self):
        return f"Reservation by {self.user} for {self.show}"

    def save(self, *args, **kwargs):
        super(Reservation, self).save(*args, **kwargs)  # Save to ensure the reservation has a primary key
        self.total_price = self.tickets.aggregate(total=Sum('price'))['total'] or 0
        super(Reservation, self).save(update_fields=['total_price'])  # Save again to update the total price

    def __str__(self):
        tickets_str = ", ".join([f"Ticket ID {ticket.id}" for ticket in self.tickets.all()])
        return f"Reservation {self.id} by {self.user.username} for {self.show} - Tickets: {tickets_str}"