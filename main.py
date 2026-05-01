import asyncio
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

shutdown_event = asyncio.Event()

@app.on_event("shutdown")
async def shutdown():
    await shutdown_event.wait()

@app.get("/shutdown")
async def shutdown_server():
    shutdown_event.set()
    return JSONResponse(content={"message": "Server is shutting down"}, status_code=200)

@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"status": "healthy"}, status_code=200)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. FastAPI ni qo'llayuvchi serverni ishga tushing.
2. `/shutdown` endpointiga GET request yuboring.
3. Server to'xtashini kutib oling.
