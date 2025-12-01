import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# In-memory storage with sample data
ITEMS = {
    1: {"id": 1, "name": "Apple", "description": "A red fruit"},
    2: {"id": 2, "name": "Laptop", "description": "A portable computer"},
    3: {"id": 3, "name": "Book", "description": "A mystery novel"},
}
NEXT_ID = 4   # Next ID after the preloaded ones


def parse_body(request):
    """Parse JSON body safely."""
    if not request.body:
        return {}
    try:
        return json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return {}


@csrf_exempt
def item_list_create(request):
    """
    GET  /api/items/         -> list all items
    POST /api/items/         -> create a new item (in-memory)
    """
    global NEXT_ID

    if request.method == "GET":
        data = list(ITEMS.values())
        return JsonResponse(data, safe=False, status=200)

    if request.method == "POST":
        body = parse_body(request)

        name = body.get("name")
        description = body.get("description", "")

        if not name:
            return JsonResponse(
                {"error": "Field 'name' is required."},
                status=400,
            )

        item_id = NEXT_ID
        NEXT_ID += 1

        item = {
            "id": item_id,
            "name": name,
            "description": description,
        }

        ITEMS[item_id] = item
        return JsonResponse(item, status=201)

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def item_detail(request, item_id):
    """
    GET    /api/items/<id>/  -> retrieve one item
    PUT    /api/items/<id>/  -> update item
    DELETE /api/items/<id>/  -> delete item
    """
    if item_id not in ITEMS:
        return JsonResponse({"error": "Item not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(ITEMS[item_id], status=200)

    if request.method == "PUT":
        body = parse_body(request)

        name = body.get("name", ITEMS[item_id]["name"])
        description = body.get("description", ITEMS[item_id]["description"])

        ITEMS[item_id]["name"] = name
        ITEMS[item_id]["description"] = description

        return JsonResponse(ITEMS[item_id], status=200)

    if request.method == "DELETE":
        del ITEMS[item_id]
        return JsonResponse({"message": "Item deleted."}, status=204, safe=False)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


def api_root(request):
    return JsonResponse({"message": "API is running"}, status=200)
