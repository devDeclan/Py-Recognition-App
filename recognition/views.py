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
      #handle_video_upload(video)
      #return render(request, "app.html", {"video": True})
    else:
      return render(request, 'index.html')
  except Exception as e:
    print(e)
    print("aborted")

def app(request):
  video= request.GET.get("video")
  return render(request, "app.html", {"video": False})

#def video(request):
#  try:
#    return StreamingHttpResponse(generator(VideoReader("/tmp/py_recognition.mp4")), content_type="multipart/x-mixed-replace;boundary=frame")
#  except Exception as e:
#    print(e)
#    print("aborted")

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

#def handle_video_upload(file):
#  with open("/tmp/py_recognition.mp4", "wb+") as destination:
#    for chunk in file.chunks():
#      destination.write(chunk)