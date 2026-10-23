# Web Analytics beacon reads. Reads the token from .git-credentials; prints no ids.
# python3 -I scratch/beacon.py <startZ> <endZ> [compare]
import json, sys, urllib.request
from collections import Counter
cred = {}
for line in open('/home/walker/market-nana/.git-credentials'):
    if '=' in line and not line.startswith('http'):
        k, v = line.strip().split('=', 1); cred[k] = v
q = """query($a:String!,$s:Time!,$e:Time!){viewer{accounts(filter:{accountTag:$a}){
rumPageloadEventsAdaptiveGroups(limit:5000,filter:{datetime_geq:$s,datetime_lt:$e,requestHost_like:"%bananafest-destiny.com"}){
count sum{visits} dimensions{requestHost requestPath refererHost userAgentBrowser userAgentOS deviceType countryName datetimeMinute}}}}}"""
req = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql',
    data=json.dumps({'query': q, 'variables': {'a': cred['CLOUDFLARE_ACCOUNT_ID'], 's': sys.argv[1], 'e': sys.argv[2]}}).encode(),
    headers={'Authorization': 'Bearer ' + cred['CLOUDFLARE_API_TOKEN'], 'Content-Type': 'application/json'})
r = json.load(urllib.request.urlopen(req, timeout=30))
if r.get('errors'): print(r['errors']); sys.exit(1)
rows = [x for x in r['data']['viewer']['accounts'][0]['rumPageloadEventsAdaptiveGroups']
        if x['dimensions']['userAgentBrowser'] not in ('ChromeHeadless', 'Unknown')]
if len(sys.argv) > 3 and sys.argv[3] == 'compare':
    for x in sorted(rows, key=lambda x: x['dimensions']['datetimeMinute']):
        d = x['dimensions']
        if d['requestHost'].startswith('puzzlepress') and d['requestPath'].startswith('/compare'):
            print(d['datetimeMinute'], d['deviceType'], d['userAgentBrowser'], d['userAgentOS'], d['countryName'], d['refererHost'] or '(none)')
    sys.exit(0)
loads = Counter(); visits = Counter(); ref = Counter(); fb = 0
for x in rows:
    d = x['dimensions']; h = d['requestHost']; v = x['sum']['visits']
    loads[h] += x['count']; visits[h] += v; ref[d['refererHost'] or '(none)'] += v
    if 'facebook' in (d['refererHost'] or ''): fb += v
print('page loads', sum(loads.values()), 'visits', sum(visits.values()), 'facebook', fb)
for h, n in visits.most_common(): print(f'  {h}: {n} visits, {loads[h]} loads')
print('visits by referrer:')
for h, n in ref.most_common(12): print(f'  {h}: {n}')
