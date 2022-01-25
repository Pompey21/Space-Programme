# this is actually Sentinel Hub API tutorial - must change name later on

"""
    Obtaining the Access Token
"""
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your client credentials
client_id = '70410bfb-954c-48bc-93a3-6949262d8643'
client_secret = 'S8K1j]@Gq,DKq8*Ax/zKvxr|p-Xd(41H5&bx5;Ng'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)


# Get token for the session
token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token',
                          client_secret=client_secret)
print()
print(token)
print()

# All requests using this session will have an access token automatically added
resp = oauth.get("https://services.sentinel-hub.com/oauth/tokeninfo")
print(resp.content)

"""
    Obtaining the Access Token
"""
access_token = 'eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyZTc2NmFiNy1mYjVlLTQyNzYtOWU1My1mOGE5YjFhZDBlZjEiLCJhdWQiOiI3MDQxMGJmYi05NTRjLTQ4YmMtOTNhMy02OTQ5MjYyZDg2NDMiLCJqdGkiOiI4OWNmODZmYS1jMmVmLTRjOTAtYTNiZS0wNzA4ZTFjNDBmZDAiLCJleHAiOjE2NDMxMTI0NTcsIm5hbWUiOiJNYXJrbyBNZWtqYXZpYyIsImVtYWlsIjoiczE4MTMzMDhAZWQuYWMudWsiLCJnaXZlbl9uYW1lIjoiTWFya28iLCJmYW1pbHlfbmFtZSI6Ik1la2phdmljIiwic2lkIjoiN2Y2NWRiN2EtZWI4OS00ZjY0LWI0OGYtODU0NjhlMGMzMDI1IiwiZGlkIjoxLCJhaWQiOiI1OTFkYTExNC1hMDcxLTQ3MzgtODQwZi04MTRjZjZlNjlhMDAiLCJkIjp7IjEiOnsicmEiOnsicmFnIjoxfSwidCI6MTEwMDB9fX0.ft0DTLZMFRPPGVY3IuDBSbzEVWkfd0sXkE3JlO47DHHJ0F0y-PaClctc7TLIP6E4GealB2Vm8WsI7-v_asMCr0o_1eQfZ-pLgdyhBkmBbwfYJ-zvte4yV-HQ-jpmbcKcfpVdCTtM1xEzrJkOZjj2pbF7sXvA7yKzJsuVvyvSYBLVtipJqDT-XrBbBVqGvzF1MKAJ-IG1Ezo5srIOoXHF_ddxeKEGIsXJ9PrcgoHG-VhlKVgsdR-l84oiqDn0L6wgKWbeEZfYg-kjqZFETfofiLEiAeT6kIJrnX9ZtZLcRa3T3ko4zJeyJDtc7Zwkv_XqnVDVpH612eQF-l3mgqlGXw'




