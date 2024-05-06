import hashlib

from aiohttp import web


async def healthcheck(request):
    return web.json_response({}, status=200)


async def hash_string(request):
    try:
        data = await request.json()
        input_string = data.get("string", None)
        if input_string is None:
            return web.json_response(
                {"validated_errors": "Field string is required"}, status=400
            )
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        return web.json_response({"hash_string": hashed_string})
    except ValueError:
        return web.json_response(
            {"validated_errors": "Invalid JSON format"}, status=400
        )


app = web.Application()

app.router.add_get("/healthcheck", healthcheck)
app.router.add_post("/hash", hash_string)

if __name__ == "__main__":
    web.run_app(app)
