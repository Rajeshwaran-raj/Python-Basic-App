
import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

ITEMS=[]
NEXT_ID=1

def _get_next_id():
    global NEXT_ID
    i=NEXT_ID; NEXT_ID+=1; return i

def _find_item(i):
    for it in ITEMS:
        if it["id"]==i: return it
    return None

@csrf_exempt
def items_collection(request):
    if request.method=="GET":
        return JsonResponse(ITEMS, safe=False)
    if request.method=="POST":
        try: data=json.loads(request.body or "{}")
        except: return HttpResponseBadRequest("Invalid JSON")
        if not data.get("title"): return HttpResponseBadRequest("title required")
        item={"id":_get_next_id(),"title":data["title"],"description":data.get("description","")}
        ITEMS.append(item)
        return JsonResponse(item, status=201)
    return HttpResponseNotAllowed(["GET","POST"])

@csrf_exempt
def item_detail(request,item_id):
    it=_find_item(item_id)
    if not it: return JsonResponse({"detail":"Not found"},status=404)
    if request.method=="GET":
        return JsonResponse(it)
    if request.method in ("PUT","PATCH"):
        try: data=json.loads(request.body or "{}")
        except: return HttpResponseBadRequest("Invalid JSON")
        if request.method=="PUT":
            if not data.get("title"): return HttpResponseBadRequest("title required")
            it["title"]=data["title"]; it["description"]=data.get("description","")
        else:
            if "title" in data: it["title"]=data["title"]
            if "description" in data: it["description"]=data["description"]
        return JsonResponse(it)
    if request.method=="DELETE":
        ITEMS.remove(it)
        return JsonResponse({"detail":"deleted"}, status=204)
    return HttpResponseNotAllowed(["GET","PUT","PATCH","DELETE"])
