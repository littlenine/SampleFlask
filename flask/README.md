## API

### Get MD5 of website

#### REQUEST  
`GET /url/<url>`

```
curl -i http://127.0.0.1/url/https://www.google.com
```

#### RESPONSE
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 32
Server: Werkzeug/0.16.0 Python/3.6.8
Date: Fri, 17 Dec 2021 15:32:20 GMT

64cad98e15a27b84745e346cf303c341
```