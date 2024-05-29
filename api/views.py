import os.path

from django.conf import settings
from django.contrib.auth import login
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from core.views import UserService
from users.services import Credentials, CredentialsService
from webapp.secrets import get_secret
from rest_framework.decorators import api_view
from django.http import JsonResponse
from google_auth_oauthlib.flow import Flow
from google.auth.transport import Request

#new-imports
from google_auth_oauthlib.flow import Flow
from google.auth.transport import Request

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SCOPES = [
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
<<<<<<< HEAD
    "openid",
=======
    "openid",   
>>>>>>> da576de (tests code)
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

@api_view(['POST'])
def calendar_token(request):
    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
<<<<<<< HEAD
    flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri="http://localhost:3000")
    code = request.data['code']
    
    try:
        flow.fetch_token(code=code)
        credentials = Credentials.from_flow(flow.credentials)

        user_service = UserService.from_credentials(credentials)
        user, _ = user_service.update_local(user_service.remote())
        user_service.check_calendar(user)

        login(request, user)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"error": str(e)})
=======
    flow = Flow.from_client_config(config,scopes=SCOPES,redirect_uri="http://127.0.0.1:3000")
    code = request.data['code']
    print('code', code)
    # flow.fetch_token(code)  
    # 4/0AdLIrYdjDBOqa7mxm9bGUUdXo_lyOu1YgKIiDh6_UhBCmfZNI_JMkRDLvg33YTHPSaWe2A
    try:
        credentials = flow.fetch_token(code=code)
        print('crendentials:', credentials)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"error": str(e)})
    
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
>>>>>>> da576de (tests code)
    else:
        return JsonResponse({"sucess": True})