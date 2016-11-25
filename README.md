<h1>GET TOP BETA USERS FROM GMAIL - (Read me) </h1>
<p>This is a script to pick out the Top X number of users email address from a GMail account.</p>
<h2>Configuration</h2>
<p>Create a config file called ""<strong>config.json</strong>".  Each node is a seperate Email account, one for a test, one for Android and one for iOA</p>

{
  "test": {
    "host": "<EMAIL_ADDRESS",
    "login": "<GMAIL_USERNAME>",
    "password": "<APPS_KEY>"
  },
  "android": {
    "host": "<EMAIL_ADDRESS",
    "login": "<GMAIL_USERNAME>",
    "password": "<APPS_KEY>"
  },
  "ios": {
    "host": "<EMAIL_ADDRESS",
    "login": "<GMAIL_USERNAME>",
    "password": "<APPS_KEY>"
  }
}
