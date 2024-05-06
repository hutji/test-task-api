import click
from aiohttp import web

from handlers import hash_string, healthcheck


@click.command()
@click.option("--port", default=8080)
def run_server(port):
    app = web.Application()
    app.router.add_get("/healthcheck", healthcheck)
    app.router.add_post("/hash", hash_string)
    web.run_app(app, port=port)


if __name__ == "__main__":
    run_server()
