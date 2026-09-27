from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Stream


def home(request):
    return render(request, "streamapp/registerapp/add_stream.html")


def add_stream(request):
    if request.method == "POST":
        stream_name = request.POST.get("stream_name")
        stream_image = request.FILES.get("stream_image")  # Get the uploaded image file

        if stream_name:
            stream = Stream.objects.create(name=stream_name, image=stream_image)

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

    # DataTable values
    draw = int(request.GET.get("draw", 1))
    start = int(request.GET.get("start", 0))
    length = int(request.GET.get("length", 10))

    search_value = request.GET.get("search[value]", "")

    # Get all streams
    streams = Stream.objects.all().order_by("-id")

    # Total records before filtering
    total_records = streams.count()

    # Filtering
    if search_value:
        streams = streams.filter(
            name__icontains=search_value
            
        )

    # Total records after filtering
    filtered_records = streams.count()

    # Pagination
    streams = streams[start:start + length]

    data = []

    for stream in streams:
        data.append({
            
            "id": stream.id,
            "name": stream.name,
            "image": stream.image.url if stream.image else None #kjasndj
        })

    return JsonResponse({
        "draw": draw,
        "recordsTotal": total_records,
        "recordsFiltered": filtered_records,
        "data": data
    })

def update_stream(request, id):

    if request.method == "POST":

        stream_name = request.POST.get("stream_name")
        stream_image = request.FILES.get("stream_image")  # Get the uploaded image file

        try:
            stream = Stream.objects.get(id=id)

        except Stream.DoesNotExist:
            return JsonResponse({ "success": False, "message": "Stream not found."}, status=404)

        if stream_name:
            stream.name = stream_name
        if stream_image:
            stream.image = stream_image
        stream.save()

        return JsonResponse({"success": True, "message": "Stream updated successfully." })
        
    return JsonResponse({ "success": False, "message": "Please enter a stream name."}, status=400)
    

def delete_stream(request, id):
    if request.method == "DELETE":
        try:
            stream = Stream.objects.get(id=id)
            stream.delete()
            return JsonResponse({"success": True, "message": "Stream deleted successfully."})
        except Stream.DoesNotExist:
            return JsonResponse({"success": False, "message": "Stream not found."}, status=404)

    return JsonResponse({"success": False, "message": "Invalid request."}, status=405)