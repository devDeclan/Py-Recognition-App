from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("app", views.app, name="app"),
	#path("video", views.video, name="video"),
	path("camera", views.camera, name="camera")
]