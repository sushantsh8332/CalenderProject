This project requires the use of GOOGLE_CLIENT_SECRET ID & some more things, so to run the project, first of all you have to download the client_secret.json file using the following steps:

```
    1. Go to the [Google API Console](https://console.developers.google.com/).
    2. Select your project or create a new project.
    3. In the left sidebar, click on "Credentials".
    4. Click on the "Create credentials" button and select "OAuth client ID".
    5. On the "Application type" screen, select "Web application" (or the appropriate option based on your application type).
    6. In the "Authorized JavaScript origins" field, enter the base URL of your Django application (e.g., `http://localhost:8000`).
    7. In the "Authorized redirect URIs" field, enter the redirect URI for your Django application's OAuth flow (e.g., `'http://localhost:8000/rest/v1/calendar/redirect/'`).
    8. Click on the "Create" button to create the OAuth client ID.
    9. Once created, you should see the newly created OAuth client ID listed under the "OAuth 2.0 Client IDs" section in the Credentials tab.
    10. Download the JSON file containing your client secret and rename it as client_secret.json & place it in the parent folder.
```

After this, you can run the project by using this command(provided you have django installed):
```
    python manage.py runserver
```