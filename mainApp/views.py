from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.http import JsonResponse


# Create your views here.
def GoogleCalendarInitView(request):
    flow = InstalledAppFlow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET,
        scopes=[settings.GOOGLE_CALENDAR_SCOPE],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(access_type='offline', prompt='consent')

    request.session['oauth2_state'] = state
    return redirect(authorization_url)

def GoogleCalendarRedirectView(request):
    state = request.session.get('oauth2_state', None)
    code = request.GET.get('code', None)

    flow = InstalledAppFlow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET,
        scopes=[settings.GOOGLE_CALENDAR_SCOPE],
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
        state=state
    )
    flow.fetch_token(code=code)

    credentials = flow.credentials
    service = build('calendar', 'v3', credentials=credentials)

    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])

    return JsonResponse(events, safe=False)
