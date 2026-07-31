from collections import defaultdict
from datetime import datetime, timedelta

from fastapi import HTTPException, Request


requests = defaultdict(list)


def rate_limit(request: Request):

    ip = request.client.host

    now = datetime.utcnow()

    requests[ip] = [
        t for t in requests[ip]
        if now - t < timedelta(minutes=1)
    ]

    if len(requests[ip]) >= 60:
        raise HTTPException(
            status_code=429,
            detail="Too Many Requests"
        )

    requests[ip].append(now)