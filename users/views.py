from django.core.exceptions import BadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

<<<<<<< HEAD
# Create your views here.



"""
{
    "credential": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjMyM2IyMTRhZTY5NzVhMGYwMzRlYTc3MzU0ZGMwYzI1ZDAzNjQyZGMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI0NzA2NTMwMzU2NDQtcmtyMTlyb2YxZWNscDdmN2dtZDQwNDRqdDExMGhmOWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI0NzA2NTMwMzU2NDQtcmtyMTlyb2YxZWNscDdmN2dtZDQwNDRqdDExMGhmOWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTQ5MTQzMTU1OTgxNjg5ODEzMTAiLCJlbWFpbCI6ImthdWFubmVyeTA1MDBAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTcxNjQwMjE4NywibmFtZSI6IkthdWFuIE5lcnkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSl8xQXBDY0R4Nmc3bzd5T0Q4OXRiUTBqRFhpZk5OOE9DWUplRzkwWVV6QWhjLUdPND1zOTYtYyIsImdpdmVuX25hbWUiOiJLYXVhbiIsImZhbWlseV9uYW1lIjoiTmVyeSIsImlhdCI6MTcxNjQwMjQ4NywiZXhwIjoxNzE2NDA2MDg3LCJqdGkiOiI0YzRkMmMwYTM5NWM1NjA4YmQ4OWFiNGY2ZWU5MTlhNjk0ZGRkMTViIn0.A1SyE1ovyy3UK9DZ0u8IGE1JKCDY_G_wrRn-XUyw12RTD84lAbjPSK6t_qCWjV0tWAPYF1LdQLCQduoEFbKM12iD3WC6gE4G8R3stkQ9DUsTTTN73vjsXv3erTup-qwT9hiu3OPfHxrNMn8rHKVb0qhu7C9bT8e1A-MaqzdNIyQxEwe2v7Qu9XL3Wkvi5yA28UVrgye3OBOPThOWigcMyrNByIMa7bLW50opNgLESycOX0x50mt4xf1oDhNMjP8DsP2bf2NrmTB3oMMaBkI97cEwt4aMOMWyqdOOjmCt4zsD3rW0dhn8OGGndHMD5zTMlJKj9F4qA_pnK9fwePuXug",
    "clientId": "470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com",
    "select_by": "btn"
}
"""


"""
{
    "access_token": "ya29.a0AXooCgvpR18zNN3pScrKdaFIH7bYsNVOIx7nqyu3AmHtNUQW7PfvFsBajOO_wk6hCj8gK0fmeabwUebLF3w29IajwSS4Xx6QNjIYyQBDSC2gk0DTLPnyOTnjWy8STHF78v3Y7puHFuBmBifsNNKRJAzlb-H7EwHexr4aCgYKAbASARISFQHGX2Mib_1Vd4YydXJ75j_KwAv_7w0170",
    "token_type": "Bearer",
    "expires_in": 2617,
    "scope": "email profile https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
    "authuser": "1",
    "prompt": "none"
}
"""


=======
from core.models import Team


@require_http_methods(["POST"])
def confirm(request):
    if not request.user.is_authenticated:
        raise BadRequest("Usuário não autenticado")

    if not (subscription := request.POST.get("subscription")):
        raise BadRequest("Inscrição não informada")

    try:
        team = Team.objects.get(ref=subscription)
    except Team.DoesNotExist:
        raise BadRequest("Inscrição não encontrada")
    else:
        request.user.subscriptions.add(team)

    return render(request, "users/confirmed.html")
>>>>>>> 47d2db413d38ab8a9e87759ddf7ce20f5943283d
