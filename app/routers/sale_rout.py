from dataclasses import asdict

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from app.api.models.city_page_model import CityPage

sale_router = APIRouter()


@sale_router.post("/city_page/", tags=["users"])
async def get_by_router_city_page(city_page: CityPage):
    try:
        return JSONResponse(content=asdict(city_page), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content={f"{e.__class__.__name__}":{str(e)}}, status_code=status.HTTP_400_BAD_REQUEST)


@sale_router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@sale_router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}