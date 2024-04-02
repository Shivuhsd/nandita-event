from django.contrib import admin
from .models import Bookings, Feedback, Enquiry, Package
# Register your models here.


admin.site.register(Bookings)
admin.site.register(Feedback)
admin.site.register(Enquiry)
admin.site.register(Package)