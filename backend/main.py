import random
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_fastapi_app() -> FastAPI:
    app = FastAPI(
        # docs_url=None,
        redoc_url=None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            'http://localhost:5173', 
            'http://127.0.0.1:5173',
            'http://87.228.36.65'
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = get_fastapi_app()

items = [
    {
        'id': 1,
        'name': 'Docker',
        'url': 'https://static-00.iconduck.com/assets.00/docker-icon-2048x2048-5mc7mvtn.png'
    },
    {
        'id': 2,
        'name': 'GitHub',
        'url': 'https://cdn-icons-png.flaticon.com/512/25/25231.png'
    },
    {
        'id': 3,
        'name': 'Nginx',
        'url': 'https://www.svgrepo.com/show/373924/nginx.svg'
    }
]


@app.get('/items')
async def get_items():
    shuffled_items = items.copy()
    random.shuffle(shuffled_items)
    return shuffled_items


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
