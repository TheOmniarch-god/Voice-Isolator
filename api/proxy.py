"""Vercel serverless function: proxies /api/* requests to the VoiceStudio backend.

Set the VERCEL_API_BASE environment variable in your Vercel project to the
backend's public URL (e.g. https://voice-backend.example.com).
"""

import base64
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def handler(request):
    api_base = os.environ.get("VERCEL_API_BASE", "").rstrip("/")
    if not api_base:
        return {
            "statusCode": 502,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "error": "VERCEL_API_BASE not configured. "
                    "Set it in your Vercel project settings to the backend URL."
                }
            ),
        }

    # Recover the original path from the request URL.
    url = getattr(request, "url", "") or ""
    path = ""
    if url.startswith("/api/"):
        path = url[len("/api/"):]
    elif url == "/api":
        path = ""
    else:
        path = getattr(request, "path", "") or ""
        if path.startswith("/api/"):
            path = path[len("/api/"):]
        elif path == "/api":
            path = ""

    # Preserve query string from the original request.
    query = getattr(request, "query", None) or {}
    if query:
        qs = "&".join(f"{k}={v}" for k, v in query.items())
        path = f"{path}?{qs}" if path else f"?{qs}"

    target = f"{api_base}/{path}" if path else api_base

    method = getattr(request, "method", "GET")
    body = getattr(request, "body", None) or b""
    if isinstance(body, str):
        body = body.encode()

    headers = {}
    for key, value in (getattr(request, "headers", {}) or {}).items():
        key_lower = key.lower()
        if key_lower in ("host", "content-length", "connection"):
            continue
        headers[key] = value

    try:
        req = Request(target, data=body, method=method, headers=headers)
        resp = urlopen(req)
        resp_body = resp.read()
        is_base64 = resp.headers.get("Content-Type", "").startswith(
            ("image/", "audio/", "video/", "application/octet-stream")
        )
        return {
            "statusCode": resp.status,
            "headers": {
                "Content-Type": resp.headers.get("Content-Type", "application/json"),
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, PATCH, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Requested-With",
            },
            "body": base64.b64encode(resp_body).decode() if is_base64 else resp_body.decode(errors="replace"),
            "isBase64Encoded": is_base64,
        }
    except HTTPError as e:
        resp_body = e.read()
        return {
            "statusCode": e.code,
            "headers": {
                "Content-Type": e.headers.get("Content-Type", "application/json"),
                "Access-Control-Allow-Origin": "*",
            },
            "body": resp_body.decode(errors="replace"),
        }
    except URLError as e:
        return {
            "statusCode": 502,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": f"Backend unreachable: {str(e)}"}),
        }
    except Exception as e:  # noqa: BLE001
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)}),
        }
