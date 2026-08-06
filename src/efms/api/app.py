from fastapi import FastAPI

from efms.api.routes import router


def create_api() -> FastAPI:

    app = FastAPI(

        title="Enterprise File Management System API",

        version="1.0.0",

    )

    app.include_router(router)

    return app