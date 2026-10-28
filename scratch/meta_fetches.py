# Zone log: facebookexternalhit fetches of puzzlepress.* by day and path. Reads the token from .git-credentials; looks the zone up by name and never prints it.
# python3 -I scratch/meta_fetches.py <startZ> <endZ> | sed (zone mask). Keep the window to 4w2d or less.
import json, sys, urllib.request
cred = {}
for line in open('/home/walker/market-nana/.git-credentials'):
    if '=' in line and not line.startswith('http'):
        k, v = line.strip().split('=', 1); cred[k] = v
zr = json.load(urllib.request.urlopen(urllib.request.Request('https://api.cloudflare.com/client/v4/zones?name=bananafest-destiny.com', headers={'Authorization': 'Bearer ' + cred['CLOUDFLARE_API_TOKEN']}), timeout=30))
zone = zr['result'][0]['id']
q = """query($z:String!,$s:Time!,$e:Time!){viewer{zones(filter:{zoneTag:$z}){
httpRequestsAdaptiveGroups(limit:1000,filter:{datetime_geq:$s,datetime_lt:$e,clientRequestHTTPHost_like:"puzzlepress%",userAgent_like:"%facebookexternalhit%"}){
count dimensions{date clientRequestPath}}}}}"""
req = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql',
    data=json.dumps({'query': q, 'variables': {'z': zone, 's': sys.argv[1], 'e': sys.argv[2]}}).encode(),
    headers={'Authorization': 'Bearer ' + cred['CLOUDFLARE_API_TOKEN'], 'Content-Type': 'application/json'})
r = json.load(urllib.request.urlopen(req, timeout=30))
if r.get('errors'): print(r['errors']); sys.exit(1)
for x in sorted(r['data']['viewer']['zones'][0]['httpRequestsAdaptiveGroups'], key=lambda x:x['dimensions']['date']):
    print(x['dimensions']['date'], x['dimensions']['clientRequestPath'], x['count'])
