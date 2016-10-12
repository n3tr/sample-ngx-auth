```
docker-compose build
docker-compose up

```

Request to

```bash
http://{docker-host}:8080


HEADER:
X-Authorization: 1234
# Forward to origin context


X-Authorization: 500
# return 500


Otherwise return 401
```
