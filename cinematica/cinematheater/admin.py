from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(MovieShow)
admin.site.register(Reservation)
admin.site.register(Ticket)