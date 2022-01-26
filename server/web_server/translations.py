import json
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sync_rules(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        try:
            ver = request.GET["v"]
        except KeyError:
            return HttpResponseBadRequest("GET in form: /sync_rules?v=<current version:int>")
        else:
            with open("translations.json") as f:
                translations = json.load(f)
            
            if int(ver) == translations["version"]:
                return HttpResponse("Rules already up-to-date", status=204)
            else:
                return JsonResponse(translations)
    else:
        return HttpResponseBadRequest("Endpoint /sync_rules only accepts GET requests")
