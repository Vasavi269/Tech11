from flask import Flask, g
from flask_oidc import OpenIDConnect
import json

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'NotVerySecretKey',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'myRealm',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)

@app.route('/', methods=['GET'])
def home_page():
    return "Welcome to home page <a href = '/login'><button>Login</button></a"

@app.route('/login')
@oidc.require_login
def login():
    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])

    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')
    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
            print ('access_token=<%s>' % access_token)
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            #greeting = requests.get('http://localhost:8080/greeting', headers=headers).text
        except:
            print ("Could not access greeting-service")
            greeting = "Hello %s" % username
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)