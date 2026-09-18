from django.shortcuts import render
from django.http import JsonResponse
from .models import Stream


def home(request):
    return render(request, "streamapp/registerapp/add_stream.html")


def add_stream(request):
    if request.method == "POST":
        stream_name = request.POST.get("stream_name")

        if stream_name:
            stream = Stream.objects.create(name=stream_name)

            return JsonResponse({
                "success": True,
                "message": "Stream saved successfully",
                "id": stream.id,
                "name": stream.name
            })

        return JsonResponse({
            "success": False,
            "message": "Please enter a stream name"
        }, status=400)

    return JsonResponse({
        "success": False,
        "message": "Invalid request"
    }, status=405)

def get_streams(request):
    streams = Stream.objects.all()

    data = []

    for stream in streams:
        data.append({
            "id": stream.id,
            "name": stream.name
        })

    return JsonResponse({
        "streams": data
    })