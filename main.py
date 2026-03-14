from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dao.parts import Part
from handler.parts import PartHandler
app = FastAPI()
#origins = ['*'
#    "http://localhost.tiangolo.com",
#    "https://localhost.tiangolo.com",
#    "http://localhost",
#    "http://localhost:8080",
#]
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/PartsApp/parts")
async def get_parts(color: str | None = None):
    print("Color: ", color)
    if color is None:
        return PartHandler().get_all_parts()
    else:
        return PartHandler().get_parts_by_color(color)


@app.post("/PartsApp/parts")
async def create_part(new_part: Part):
    return PartHandler().create_part(new_part)


@app.get("/PartsApp/parts/{part}")
async def get_part(part: int):
    return PartHandler().get_part_by_id(part)

@app.put("/PartsApp/parts/{part}")
async def update_part(part: int, part_data: Part):
    return PartHandler().update_part(part, part_data)

@app.delete("/PartsApp/parts/{part}")
async def delete_part(part: int):
    return PartHandler().delete_part(part)
