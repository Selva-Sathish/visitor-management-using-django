import base64
import os
import uuid
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import VisitorForm
from .models import Visitor

def entry(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            
            # Decode and save the photo
            photo_data = request.POST.get('photoData')
            if photo_data:
                # Decode the base64-encoded image data
                format, imgstr = photo_data.split(';base64,') 
                ext = format.split('/')[-1]  # Extract the image extension
                decoded_img = base64.b64decode(imgstr)
                
                # Generate a unique filename for the image
                unique_filename = str(uuid.uuid4()) + f'.{ext}'
                photo_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
                with open(photo_path, 'wb') as f:
                    f.write(decoded_img)
                
                # Update the photo_path field in the Visitor model
                visitor.photo_path = os.path.join(settings.MEDIA_URL,  unique_filename)
            
            visitor.save()
            return HttpResponse('<h1> submitted successfully</h1>')  # Redirect to success page after saving
    else:
        form = VisitorForm()
    return render(request, 'entry.html', {'form': form})
