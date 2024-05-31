from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="starting-page"),
    path("rep_counter", views.rep_counter, name="rep_counter"),
    path('start-video-capture/', views.start_video_capture, name='start_video_capture'),
    path("workout_plan_generator/", views.workout_plan_generator_view, name="workout_plan_generator"),
]
