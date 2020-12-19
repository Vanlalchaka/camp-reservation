from django.contrib import admin
from .models import Chambre,Catalogue,Testimonial,Reservation
# Register your models here.
admin.site.register(Chambre)
admin.site.register(Reservation)

admin.site.register(Catalogue)
admin.site.register(Testimonial)