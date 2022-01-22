# BI-PythonGoogleSheetsTableauPublic

1. Find dataset of your interest (static or some daily fresh web data)
2. Customize Google Cloud Console:
   1. Create new project
   2. Enable apis and services - find Google Sheets API and Enable it
   3. Go to Credentials and Create credentials and give Editor permissions to new generated user
   4. In the same topic (Credentials) find down Service Accounts and click to new generated email
   5. Go to Keys and click Add key and then Create new key, and you will get json object
   6. Save that json object to your pc 
3. Customize Google Sheet:
   1. Enter to target sheet
   2. Right-up Share
   3. Enter generated email from json key object (role must be Editor), then click Done
4. Copy json key object file to gsapi folder inside this project and rename it to credentials.json
5. Open account on Tableau Public (https://public.tableau.com/en-us/s/)
6. Download Tableau Public app (https://public.tableau.com/en-us/s/download)
7. Connect Tableau Public to Google sheets
8. Make some dashboard of your interests
9. Publish dashboard to Tableau Public account (server)
10. If you inside data folder take some live data then your Tableau Public dashboard will be updated every day


