from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from disagreement.config import get_settings, DefaultSettings
from disagreement.endpoints import list_of_routes


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    for route in list_of_routes:
        application.include_router(route)


def get_app() -> FastAPI:
    description = 'A service that implements the ability to compare two contracts' \
                  ' and generates a protocol of disagreements'

    tags_metadata = [
        {
            'name': 'Disagreement protocol service',
            'description': 'API disagreement protocol.',
        },
    ]

    application = FastAPI(
        title="Disagreement",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="0.0.1",
        openapi_tags=tags_metadata,
    )
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
    )

