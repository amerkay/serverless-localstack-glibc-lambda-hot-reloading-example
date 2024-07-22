import os
import plivo


def get_plivo_client():
    auth_id = os.environ["PLIVO_AUTH_ID"]
    auth_token = os.environ["PLIVO_AUTH_TOKEN"]
    return plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
