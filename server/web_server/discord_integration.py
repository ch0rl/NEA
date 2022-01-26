import json
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_channel(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        try:
            channel = request.POST["c"]
            user = request.POST["u"]
        except KeyError:
            return HttpResponseBadRequest("POST in form /add_channel?c=<channel id:int>&u=<user:int>")
        else:
            if not channel.isnumeric:
                return HttpResponseBadRequest("POST in form /add_channel?c=<channel id:int>&u=<user:int>")
            else:
                with open("discord_bot/vars.json", "r") as f:
                    data = json.load(f)
                
                if user in data["CHANNELS"]:
                    data["CHANNELS"][user].append(channel)
                else:
                    data["CHANNELS"][user] = [channel]

                with open("discord_bot/vars.json", "w") as f:
                    json.dump(data, f)

                return HttpResponse(f"Added channel {channel} for user {user}", status=201)
    else:
        return HttpResponseBadRequest("Endpoint /add_channel only accepts POST requests")

@csrf_exempt
def remove_channel(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        try:
            channel = request.POST["c"]
            user = request.POST["u"]
        except KeyError:
            return HttpResponseBadRequest("POST in form /remove_channel?c=<channel id:int>&u=<user:int>")
        else:
            if not channel.isnumeric or not user.isnumeric:
                return HttpResponseBadRequest("POST in form /remove_channel?c=<channel id:int>&u=<user:int>")
            else:
                with open("discord_bot/vars.json", "r") as f:
                    data = json.load(f)

                try:
                    data["CHANNELS"][user].remove(channel)
                except (ValueError, KeyError):
                    return HttpResponseBadRequest(f"Channel {channel} is not in user {user}'s channel list")

                with open("discord_bot/vars.json", "w") as f:
                    json.dump(data, f)

                return HttpResponse(f"Removed channel {channel} for user {user}")
    else:
        return HttpResponseBadRequest("Endpoint /remove_channel only accepts POST requests")

@csrf_exempt
def get_messages(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        try:
            user = request.GET["u"]
        except KeyError:
            return HttpResponseBadRequest("GET in form: /get_messages?u=<user id:int>")
        else:
            # Basic validation
            if len(user) != 4:
                return HttpResponseBadRequest("u (user id) must be a 4-digit number")
            else:
                with open("discord_bot/messages.json", "r") as f:
                    messages = json.load(f)
                
                try:
                    user_messages = messages[user]
                except KeyError:
                    return JsonResponse({"n": 0, "data": []})
                else:
                    del messages[user]
                    with open("discord_bot/messages.json", "w") as f:
                        json.dump(messages, f)
                    return JsonResponse({"n": len(user_messages), "data": user_messages})
    else:
        return HttpResponseBadRequest("Endpoint /get_messages only accepts GET requests")
