import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

ITEMS = [
    {"id": 1, "title": "Learn Django", "description": "Complete basic CRUD and authentication"},
    {"id": 2, "title": "Write Blog Post", "description": "Draft article about cloud scaling"},
    {"id": 3, "title": "Fix UI Bug", "description": "Navbar alignment issue on mobile"},
    {"id": 4, "title": "Prepare Presentation", "description": "Slides for product demo"},
    {"id": 5, "title": "Optimize Database", "description": "Improve slow SQL queries"},
    {"id": 6, "title": "Team Meeting", "description": "Weekly sprint planning"},
    {"id": 7, "title": "API Testing", "description": "Postman tests for all endpoints"},
    {"id": 8, "title": "Add Logging", "description": "Improve error logs and monitoring"},
    {"id": 9, "title": "Deploy to Cloud", "description": "Push latest build to staging"},
    {"id": 10, "title": "Write Documentation", "description": "API reference and usage guide"},
]

NEXT_ID = 11  # since we already have 1–10


def _get_next_id():
    global NEXT_ID
    i = NEXT_ID
    NEXT_ID += 1
    return i


def _find_item(i):
    for it in ITEMS:
        if it["id"] == i:
            return it
    return None


@csrf_exempt
def items_collection(request):
    if request.method == "GET":
        return JsonResponse(ITEMS, safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body or "{}")
        except:
            return HttpResponseBadRequest("Invalid JSON")

        if not data.get("title"):
            return HttpResponseBadRequest("title required")

        item = {
            "id": _get_next_id(),
            "title": data["title"],
            "description": data.get("description", ""),
        }
        ITEMS.append(item)
        return JsonResponse(item, status=201)

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def item_detail(request, item_id):
    it = _find_item(item_id)
    if not it:
        return JsonResponse({"detail": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse(it)

    if request.method in ("PUT", "PATCH"):
        try:
            data = json.loads(request.body or "{}")
        except:
            return HttpResponseBadRequest("Invalid JSON")

        if request.method == "PUT":
            if not data.get("title"):
                return HttpResponseBadRequest("title required")
            it["title"] = data["title"]
            it["description"] = data.get("description", "")
        else:
            if "title" in data:
                it["title"] = data["title"]
            if "description" in data:
                it["description"] = data["description"]

        return JsonResponse(it)

    if request.method == "DELETE":
        ITEMS.remove(it)
        return JsonResponse({"detail": "deleted"}, status=204)

    return HttpResponseNotAllowed(["GET", "PUT", "PATCH", "DELETE"])
