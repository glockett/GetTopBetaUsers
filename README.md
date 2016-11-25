This is a script to pick out the Top X number of users email address from a GMail account.

Create a config file called config.json.  Each node is a seperate Email account, one for a test one for 
{
  "test": {
    "host": "<EMAIL_ADDRESS",
    "login": "<USERNAME>",
    "password": "<APPS KEY>"
  },
  "android": {
    "host": "android.alpha@guardian.co.uk",
    "login": "android.alpha@guardian.co.uk",
    "password": "yijveeroobmqmosp"
  },
  "ios": {
    "host": "ios.beta@guardian.co.uk",
    "login": "ios.beta@guardian.co.uk",
    "password": "xxx"
  }
}
