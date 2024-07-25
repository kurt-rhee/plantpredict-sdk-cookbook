import plantpredict as pp


def authenticate():
    """
    Enter your client_id and client_secret in the spaces below
    in order to authenticate with this function
    """

    # --- Auth ---
    client_id = ''
    client_secret = ''
    base_url = 'https://api.plantpredict.terabase.energy'
    auth_url = 'https://terabase-prd.auth.us-west-2.amazoncognito.com/oauth2/token'

    if (client_id == '') or (client_secret == ''):
        raise(InvalidInputError("Please enter a client_id or client_secret in the authenticate function"))

    api = pp.Api(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
        auth_url=auth_url
    )

    return api

class InvalidInputError(Exception):
    pass
