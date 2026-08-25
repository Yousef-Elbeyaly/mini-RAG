from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

# تصحيح المسمى إلى الجمع http_requests_total وتوحيد الـ labels
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["method", "handler", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP Request Latency", ["method", "handler"])

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/sys_internal_v2_9f8a2b3c4d5e":
            return await call_next(request)

        start_time = time.time()
        response = await call_next(request)
        
        duration = time.time() - start_time
        endpoint = request.url.path

        REQUEST_LATENCY.labels(method=request.method, handler=endpoint).observe(duration)
        REQUEST_COUNT.labels(method=request.method, handler=endpoint, status=str(response.status_code)).inc()

        return response


def setup_metrics(app: FastAPI):
    app.add_middleware(PrometheusMiddleware)

    @app.get("/sys_internal_v2_9f8a2b3c4d5e", include_in_schema=False)
    def metrics():
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)