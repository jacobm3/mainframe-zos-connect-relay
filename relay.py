
import basicauth
import hvac
import json
import os
import re
import requests
from flask import Flask
from flask import request


VAULT_ADDR = os.environ.get('VAULT_ADDR')
VAULT_NAMESPACE = os.environ.get('VAULT_NAMESPACE')
VAULT_SKIP_VERIFY = os.environ.get('VAULT_SKIP_VERIFY')

app = Flask(__name__)

basic_auth_re = re.compile(r'Basic (\S+)')
basic_auth_decoded_re = re.compile(r'(\S+):(\S+)')

@app.route("/",methods=['POST'])
def relay_basic_auth():

    encoded_str = request.headers.get('Authorization')
    username, password = basicauth.decode(encoded_str)

    # Authenticate to Vault userpass
    client = hvac.Client(url=os.environ['VAULT_ADDR'])
    resp = hvac.v1.api.auth_methods.Userpass(client.adapter).login(username=str(username), password=str(password))
    status = client.is_authenticated()

    #return "%s %s" % (username, resp)
    return "%s" % json.dumps(resp)

