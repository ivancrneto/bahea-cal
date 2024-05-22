import os.path
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import redirect
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from users.services import Credentials
from users.services import CredentialsService
from webapp.secrets import get_secret

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseBadRequest
from googleapiclient.discovery import build as google_build

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",

    
]

REDIRECT_URL = f"{settings.BASE_URL}/calendar/redirect/"
API_SERVICE_NAME = "calendar"
API_VERSION = "v3"

@api_view(['GET'])
def calendar_init_view(request):
    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
    creds = CredentialsService.init_for(request.user, scopes=SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(config, SCOPES)
            flow.redirect_uri = REDIRECT_URL

            authorization_url, state = flow.authorization_url(
                access_type="offline",
                prompt="consent", include_granted_scopes="true"
            )
            request.session["state"] = state

            return JsonResponse({"authorization_url": authorization_url})

    return JsonResponse({"message": "Sucess"})


def calendar_flow_view2(request):

    """
    from google_auth_oauthlib.flow import Flow
from users.services import Credentials
#cred=Credentials(
obj={
    "access_token": "ya29.a0AXooCgvpR18zNN3pScrKdaFIH7bYsNVOIx7nqyu3AmHtNUQW7PfvFsBajOO_wk6hCj8gK0fmeabwUebLF3w29IajwSS4Xx6QNjIYyQBDSC2gk0DTLPnyOTnjWy8STHF78v3Y7puHFuBmBifsNNKRJAzlb-H7EwHexr4aCgYKAbASARISFQHGX2Mib_1Vd4YydXJ75j_KwAv_7w0170",
    "token_type": "Bearer",
    "expires_in": 2617,
    "scope": "email profile https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
    "authuser": "1",
    "prompt": "none"
}
obj2={
    "credential": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjMyM2IyMTRhZTY5NzVhMGYwMzRlYTc3MzU0ZGMwYzI1ZDAzNjQyZGMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI0NzA2NTMwMzU2NDQtcmtyMTlyb2YxZWNscDdmN2dtZDQwNDRqdDExMGhmOWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI0NzA2NTMwMzU2NDQtcmtyMTlyb2YxZWNscDdmN2dtZDQwNDRqdDExMGhmOWcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTQ5MTQzMTU1OTgxNjg5ODEzMTAiLCJlbWFpbCI6ImthdWFubmVyeTA1MDBAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTcxNjQwMjE4NywibmFtZSI6IkthdWFuIE5lcnkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSl8xQXBDY0R4Nmc3bzd5T0Q4OXRiUTBqRFhpZk5OOE9DWUplRzkwWVV6QWhjLUdPND1zOTYtYyIsImdpdmVuX25hbWUiOiJLYXVhbiIsImZhbWlseV9uYW1lIjoiTmVyeSIsImlhdCI6MTcxNjQwMjQ4NywiZXhwIjoxNzE2NDA2MDg3LCJqdGkiOiI0YzRkMmMwYTM5NWM1NjA4YmQ4OWFiNGY2ZWU5MTlhNjk0ZGRkMTViIn0.A1SyE1ovyy3UK9DZ0u8IGE1JKCDY_G_wrRn-XUyw12RTD84lAbjPSK6t_qCWjV0tWAPYF1LdQLCQduoEFbKM12iD3WC6gE4G8R3stkQ9DUsTTTN73vjsXv3erTup-qwT9hiu3OPfHxrNMn8rHKVb0qhu7C9bT8e1A-MaqzdNIyQxEwe2v7Qu9XL3Wkvi5yA28UVrgye3OBOPThOWigcMyrNByIMa7bLW50opNgLESycOX0x50mt4xf1oDhNMjP8DsP2bf2NrmTB3oMMaBkI97cEwt4aMOMWyqdOOjmCt4zsD3rW0dhn8OGGndHMD5zTMlJKj9F4qA_pnK9fwePuXug",
    "clientId": "470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com",
    "select_by": "btn"
}
cred=Credentials(obj["access_token"],token_uri="https://oauth2.googleapis.com/token"
   ...: , client_id=obj2["clientId"],client_secret="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"
   ...: ,scopes=[
   ...:     "https://www.googleapis.com/auth/calendar",
   ...:     "https://www.googleapis.com/auth/calendar.app.created",
   ...:     "https://www.googleapis.com/auth/userinfo.email",
   ...:     "https://www.googleapis.com/auth/userinfo.profile", "openid"])
cred.refresh()
cred=Credentials(obj["access_token"],token_uri="https://oauth2.googleapis.com/token"
   ...:    ...: , client_id=obj2["clientId"],client_secret="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"
   ...:    ...: ,scopes=[
   ...:    ...:     "https://www.googleapis.com/auth/calendar",
   ...:    ...:     "https://www.googleapis.com/auth/calendar.app.created",
   ...:    ...:     "https://www.googleapis.com/auth/userinfo.email",
   ...:    ...:     "https://www.googleapis.com/auth/userinfo.profile", "openid"],

  request=Request(url="https://oauth2.googleapis.com/token"))
 cred=Credentials(obj["access_token"],token_uri="https://oauth2.googleapis.com/token"
   ...:    ...:    ...: , client_id=obj2["clientId"],client_secret="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"     
   ...:    ...:    ...: ,scopes=[
   ...:    ...:    ...:     "https://www.googleapis.com/auth/calendar",
   ...:    ...:    ...:     "https://www.googleapis.com/auth/calendar.app.created",
   ...:    ...:    ...:     "https://www.googleapis.com/auth/userinfo.email",
   ...:    ...:    ...:     "https://www.googleapis.com/auth/userinfo.profile", "openid"],
   ...:  request=Request(url="https://oauth2.googleapis.com/token"))
cred=Credentials(obj["access_token"], token_uri="https://oauth2.googleapis.com/token",
client_id=obj2["clientId"], client_secret="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",
scopes = [ "https://www.googleapis.com/auth/calendar",
"https://www.googleapis.com/auth/calendar.app.created",
"https://www.googleapis.com/auth/userinfo.email",
"openid"],
request = Request(url="https://oauth2.googleapis.com/token"))
from google.auth.transport.requests import Request
cred=Credentials(obj["access_token"], token_uri="https://oauth2.googleapis.com/token",
    ...: client_id=obj2["clientId"], client_secret="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",
    ...: scopes = [ "https://www.googleapis.com/auth/calendar",
    ...: "https://www.googleapis.com/auth/calendar.app.created",
    ...: "https://www.googleapis.com/auth/userinfo.email",
    ...: "openid"],
    ...: request = Request(url="https://oauth2.googleapis.com/token"))
from google.auth.transport import Request
cred=Credentials(obj["access_token"], token_uri="https://oauth2.googleapis.com/token",
    ...:     ...: client_id=obj2["clientId"], client_secret="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",
    ...:     ...: scopes = [ "https://www.googleapis.com/auth/calendar",
    ...:     ...: "https://www.googleapis.com/auth/calendar.app.created",
    ...:     ...: "https://www.googleapis.com/auth/userinfo.email",
    ...:     ...: "openid"],
    ...:     ...: request = Request(url="https://oauth2.googleapis.com/token"))
cred=Credentials(token_uri="https://oauth2.googleapis.com/token",
client_id=obj2["clientId"], client_secret="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",
scopes = [ "https://www.googleapis.com/auth/calendar",
"https://www.googleapis.com/auth/calendar.app.created",
"https://www.googleapis.com/auth/userinfo.email",
"openid"],
request = Request(url="https://oauth2.googleapis.com/token"), obj["access_token"])
cred=Credentials(obj["access_token"], token_uri="https://oauth2.googleapis.com/token",
client_id=obj2["clientId"], client_secret="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",
scopes = [ "https://www.googleapis.com/auth/calendar",
     "https://www.googleapis.com/auth/calendar.app.created",
     "https://www.googleapis.com/auth/userinfo.email",
     "openid"])
cred.refresh( request = Request(url="https://oauth2.googleapis.com/token") )
cred.refresh( request = Request() )
from google.auth import Request
cred.refresh( request = Request(url="https://oauth2.googleapis.com/token", method="GET") )
from google.auth.transport import Request
cred.refresh( request = Request(url="https://oauth2.googleapis.com/token", method="GET") )
from google.auth.transport import Request
cred.refresh(Request())
cred.refresh(Request)
cred.refresh()
cred=Credentials(refresh_token=obj["access_token"], token_uri="https://oauth2.googleapis.com/token",client_id=obj2["clientId"], client_secret="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",
scopes = [ "https://www.googleapis.com/auth/calendar",
"https://www.googleapis.com/auth/calendar.app.created",
"https://www.googleapis.com/auth/userinfo.email",
"openid"])
SCOPES = [
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
from webapp.secrets import get_secret
config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
from django.conf import settings
config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
flow = Flow.from_client_config
#flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri="localhost:8000"
from api.views import REDIRECT_URL
flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri=REDIRECT_URL)
flow.fetch_token(code="4/0AdLIrYd22OGu0Q9vX1z6wu7pJf2vUFddst4GK28knMmfPJVZowvF9Bf2qp189ldKdVgQjg")
flow.fetch_token(code="4/0AdLIrYf1j1qEwIn-L5rw4texwyjW_VN7HnKXfBWuRBDSZ57lsIP6bKK3zd7m_2T-nieZOA")
flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri="http://localhost:3000")
flow.fetch_token(code="4/0AdLIrYf1j1qEwIn-L5rw4texwyjW_VN7HnKXfBWuRBDSZ57lsIP6bKK3zd7m_2T-nieZOA")
flow.fetch_token(code="4/0AdLIrYc3zyoA4bJT5aqfkppY5Igc6JJpx32Sjh9l62cEE9KDLF_6CGBDyYtmplDjUriECw")
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",


]
flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri="http://localhost:3000")
flow.fetch_token(code="4/0AdLIrYd8vBabhgfGRw65Puu_H6-ZGngfdgfG0Z1-Cs_x3I2jRh2UHiuhy1Qmet7gGAnEuA")
history
    """


@api_view(['GET'])
def calendar_flow_view(request):
    state = request.session.get("state") or request.GET.get("state")
    if state is None:
        return JsonResponse({"error": "Algo de errado aconteceu."})

    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
    flow = google_auth_oauthlib.flow.Flow.from_client_config(config, scopes=SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URL

    authorization_response = request.get_full_path()
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    userinfo_service = googleapiclient.discovery.build("oauth2", "v2", credentials=credentials)
    user_info = userinfo_service.userinfo().get().execute()

    email = user_info.get("email")
    User = get_user_model()
    user, created = User.objects.get_or_create(username=email, email=email)
    if created:
        user.set_unusable_password()
        user.save()

    if not CredentialsService.get_for(user):
        saved_credentials = CredentialsService.create_for(user, credentials)
    else:
        saved_credentials = CredentialsService.update_for(user, credentials)
    if not saved_credentials:
        return redirect("api/v1/calendar/init")

    saved_credentials.user = user
    saved_credentials.save(update_fields=["user"])

    authenticated_user = authenticate(request, username=email)
    if authenticated_user:
        login(request, authenticated_user)

    try:
        service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

        if not user.calendar_id:
            calendar = {"summary": "BaheaCal", "timeZone": "America/Bahia"}
            created_calendar = service.calendars().insert(body=calendar).execute()
            user.calendar_id = created_calendar["id"]
            user.save(update_fields=["calendar_id"])

        service.events().list(calendarId=user.calendar_id).execute()
    except Exception as e:
        return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"sucess": True})


"""
{
  "iss": "https://accounts.google.com",
  # id do projeto 
  "azp": "470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com",
  "aud": "470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com",
  "sub": "114914315598168981310",
  "email": "kauannery0500@gmail.com",
  "email_verified": true,
  "nbf": 1716401193,
  "name": "Kauan Nery",
  "picture": "https://lh3.googleusercontent.com/a/ACg8ocJ_1ApCcDx6g7o7yOD89tbQ0jDXifNN8OCYJeG90YUzAhc-GO4=s96-c",
  "given_name": "Kauan",
  "family_name": "Nery",
  "iat": 1716401493,
  "exp": 1716405093,
  "jti": "443530fad5c317fea6218712c8b499242432e57e"
}
"""




@api_view(['POST'])
@method_decorator(csrf_exempt)
def calendar_token(request):
    # print('body', request.body['accessToken'])
    payload = json.loads(request.body)
    print('payload', payload)
    # access_token = payload['access_token']
    
    if not payload:
        return HttpResponseBadRequest("Não foi enviado nada do front")
    
    if 'state' in request.session:
        print('req session state >>>>>',request.session['state'])
    
    # state = request.session.get("state") or request.GET.get("state")
    # print('state', state)
    # if state is None:
    #     return JsonResponse({"error": "Algo de errado aconteceu."})
    
    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
    flow = google_auth_oauthlib.flow.Flow.from_client_config(client_config=config, scopes=SCOPES)
    flow.redirect_uri = REDIRECT_URL
    
    try:
        flow.fetch_token(code=access_token)
    except Exception as e:
        return JsonResponse({"error":str(e)})
    
    credentials = flow.credentials
    print(credentials)
    
    userinfo_service = googleapiclient.discovery.build("oauth2", "v2", credentials=credentials)
    user_info = userinfo_service.userinfo().get().execute()
    
    email = user_info.get("email")
    User = get_user_model()
    user, created = User.objects.get_or_create(username=email, email=email)
    if created:
        user.set_unusable_password()
        user.save()
        
    if not CredentialsService.get_for(user):
        saved_credentials = CredentialsService.create_for(user, credentials)
    else:
        saved_credentials = CredentialsService.update_for(user, credentials)
    if not saved_credentials:
        return HttpResponseBadRequest("Erro ao salvar as credenciais.")
    
    saved_credentials.user = user
    saved_credentials.save(update_fields=["user"])
    
    authenticate_user = authenticate(request, username=email)
    if authenticate_user:
        login(request, authenticate_user)
    
    try:
        service = google_build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
        
        if not user.calendar_id:
            calendar = {"summary" : "BaheaCal", "timeZone": "America/Bahia"}
            created_calendar = service.calendars().insert(body=calendar).execute()
            user.calendar_id = created_calendar["id"]
            user.save(update_fields=["calendar_id"])
            
        service.events().list(calendarID=user.calendar_id).execute()
    except Exception as e:
        return JsonResponse({"error": str(e)})
    
    else:
        return JsonResponse({"sucess": True})