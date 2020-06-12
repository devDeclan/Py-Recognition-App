from django.shortcuts import render, HttpResponse, redirect
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from .models import VideoReader

# Create your views here.

@gzip.gzip_page
def index(request):
  try:
    if(request.method == "POST"):
      video = request.FILES.get('video').temporary_file_path()
      return StreamingHttpResponse(generator(VideoReader(video)), content_type="multipart/x-mixed-replace;boundary=frame")
    else:
      return render(request, 'index.html')
  except Exception as e:
    print(e)
    print("aborted")

def app(request):
  video= request.GET.get("video")
  return render(request, "app.html", {"video": False})

def camera(request):
  try:
    return StreamingHttpResponse(generator(VideoReader(0)), content_type="multipart/x-mixed-replace;boundary=frame")
  except Exception as e:
    print(e)
    print("aborted")

def generator(camera):
  while True:
    frame = camera.get_frame()
    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
