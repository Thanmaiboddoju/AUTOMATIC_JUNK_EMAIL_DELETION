# AUTOMATIC_JUNK_EMAIL_DELETION
automated code for deleting unwanted gmails

### token.json

The `token.json` file is automatically generated upon running the code and contains the necessary access token to authenticate and authorize the deletion of unwanted emails from your Gmail account. Ensure this file is securely stored and not shared publicly, as it grants access to your email account.


## Setting Up Google API Credentials

To authenticate and authorize the deletion of unwanted emails from your Gmail account, follow these steps to create the necessary credentials:

1. **Go to the Google Cloud Console:**
   - Open your web browser and navigate to [Google Cloud Console](https://accounts.google.com/AddSession/signinchooser?service=cloudconsole&osid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fapis%2Fdashboard%3Fproject%3Demail-excess-deletion%26pageState%3D(%2522duration%2522%3A(%2522groupValue%2522%3A%2522P30D%2522%2C%2522customValue%2522%3Anull))&hl=en_GB&ddm=0&flowName=GlifWebSignIn&flowEntry=AddSession).
   - Sign in with your Google account or create a new one if you don't have one already.

2. **Create a New Project:**
   - Once signed in, you may need to create a new project. Click on the project dropdown at the top of the page and select "New Project".
   - Name your project and click "Create".

3. **Enable Gmail API:**
   - In the Google Cloud Console, navigate to the "APIs & Services" > "Library".
   - Search for "Gmail API" and click on it.
   - Click the "Enable" button to enable the Gmail API for your project.

4. **Create OAuth 2.0 Credentials:**
   - Go to the "Credentials" tab in the "APIs & Services" section.
   - Click on the "Create Credentials" button and select "OAuth client ID".

5. **Configure the OAuth Consent Screen:**
   - If prompted, configure the OAuth consent screen by providing the necessary information such as the application name. This step is required before creating OAuth 2.0 credentials.

6. **Create OAuth Client ID:**
   - After configuring the consent screen, select "Desktop app" as the application type.
   - Give your application a name (e.g., "Email Excess Deletion").
   - Click the "Create" button.

7. **Download the Credentials File:**
   - After creating the OAuth client ID, you will see a dialog with your client ID and client secret.
   - Click the "Download" button to download the credentials file (a JSON file) to your working folder.
   - Rename the downloaded file to `credentials.json`.

8. **Add Scopes for Gmail Access:**
   - Ensure the OAuth consent screen includes the necessary scopes for accessing and deleting Gmail messages. The required scopes are:
     - `https://www.googleapis.com/auth/gmail.readonly`
     - `https://www.googleapis.com/auth/gmail.modify`
   - If these scopes were not added during the consent screen configuration, you may need to add them manually in the OAuth consent screen settings.

### Note
Keep the `credentials.json` file secure and do not share it publicly, as it contains sensitive information that allows access to your Gmail account.
