import hashlib

from django.core.cache import cache
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.urls import path


def index(_):
    return HttpResponse("<h1>Django</h1><p>with Postgres and Redis</p>")


def health(_):
    return HttpResponse("ok")


def db(_):
    with connection.cursor() as c:
        c.execute("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, at timestamptz DEFAULT now())")
        c.execute("INSERT INTO visits DEFAULT VALUES")
        c.execute("SELECT count(*) FROM visits")
        n = c.fetchone()[0]
    hits = cache.get_or_set("hits", 0)
    cache.incr("hits")
    return JsonResponse({"n": n, "cached_hits": hits})


def cpu(_):
    h = b"seed"
    for _ in range(20000):
        h = hashlib.sha256(h).digest()
    return HttpResponse(h.hex()[:8])


urlpatterns = [path("", index), path("health", health), path("db", db), path("cpu", cpu)]
