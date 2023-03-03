from django.urls import path, include

from . import views

app_name = "game"

urlpatterns = [
    path(
        "word/",
        include(
            [
                path("list/", views.WordListView.as_view(), name="list"),
                path("create/", views.WordCreateView.as_view(), name="create"),
                path("room-create/", views.RoomCreate.as_view(), name="room_create"),
                path("rooms-list/", views.RoomListView.as_view(), name="rooms_list"),
                path("room/<int:pk>", views.RoomView.as_view(), name="room"),
            ]
        ),
    ),
]
