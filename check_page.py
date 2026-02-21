import requests
try:
    r = requests.get('http://127.0.0.1:5000/', timeout=5)
    print(r.status_code)
    print(r.text[:800])
except Exception as e:
    print('ERROR', e)
