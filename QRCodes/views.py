from rest_framework.decorators import action
from .serializers import *
from rest_framework import viewsets
from django.http import HttpResponse
from io import BytesIO
import qrcode

class Driverview(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = driverSerializer

    @action(detail=True, methods=['get'])
    def generate_qr(self, request, pk=None):

        driver = self.get_object()
        driver_data = f'Driver Name: \n \n {driver.name}  \n \n phone :\n \n{driver.phone_number}'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(driver_data)
        qr.make(fit=True)
  
        img = qr.make_image(fill='black', back_color='white')
    
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
   
        return HttpResponse(buffer,content_type="image/png")
