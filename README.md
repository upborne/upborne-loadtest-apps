# upborne-loadtest-apps

Small apps of the kinds people run on a PaaS, used to load test Upborne end to end.
Each one answers the same routes, so one traffic script drives all of them:

- `/` a page
- `/health` ok
- `/db` one write and one read on its database (where it has one)
- `/cpu` about 10 ms of hashing

Databases come in as `DATABASE_URL` (the one SQL database) and `REDIS_URL`.
