from fastapi import APIRouter, Body, Path, HTTPException, Response, Request, status, Depends
from fastapi import Request, Response
from .schemas import *
from .actions import *

router_user = APIRouter(
    tags=["user"],
    prefix="/api/service"
)


@router_user.get("/user/authorization", 
                 response_model=UserItem,
                 description="Метод для аутентификация пользователя")
async def read_cookies(request: Request, response: Response):
    
    if not "access_token" in request.headers and not "access_token" in request.cookies:
        raise HTTPException(status_code=401, detail="Incorrect access_token value")
    
    cookies = request.headers["access_token"] if "access_token" in request.headers else request.cookies["access_token"]
    if not cookies:
        raise HTTPException(status_code=400, detail="cookies not found") 
    user_data = await JwtManager.decode_access_token(cookies)

    await Utils.rights_check(user_data)

    return user_data

@router_user.delete("/user/logout",
                    description="Метод для отчистки Cookies")
async def delete_cookie(response: Response):
    response.delete_cookie("access_token")
                
@router_user.post("/user/authentication", 
                  description= "Авторизация пользователя")
async def user_authorization(response: Response, request:Request, user_data: User = Body(..., description="Данные пользователя для авторизации")):
    
    existing_user = await UserDAO.user_authorization(user_login=str(user_data.login), 
                                                         user_password=str(user_data.password))
    
    access_token = JwtManager.create_access_token(
        {"userGUID": str(existing_user["userGUID"]),
        "role": str(existing_user["role"])}
        )
    
    response.set_cookie("access_token", access_token)
    response.headers["Authorization"] = access_token

    return {"JWT": access_token}
    