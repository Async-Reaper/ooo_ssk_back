"""Data access object"""
from fastapi                import HTTPException
from jose                   import jwt, JWTError
from datetime               import datetime, timedelta
from passlib.context        import CryptContext
from aiohttp                import ClientSession
from .schemas import UserRole

import json
import config

pwd_context = CryptContext(schemes=["bcrypt"])

class UserDAO:  

    @classmethod
    async def user_authorization(cls, user_login, user_password):
        async with ClientSession() as session:
            headers = {"Authorization": config.API_TOKEN}
            data = {"login": user_login, "password": user_password}

            # Запрос на авторизацию
            async with session.post(config.AUTHORIZATION, headers=headers, json=data) as response:
            # async with session.post("http://192.168.0.10/TradeWork/hs/api/authorization", headers=headers, json=data) as response:
                result = json.loads(await response.text())
                # print(result)
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail=result["message_errors"])

                return result
            
    @classmethod
    async def get_info_representative(cls, user_data: dict):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.get(config.REPRESENTATIVE.format(user_data["userGUID"]), headers=headers) as response:
                result = await response.text()
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail=result)
                return json.loads(result)
            
    @classmethod
    async def get_info_sales_point(cls, user_data: dict):
        async with ClientSession() as session:
            headers = {"Authorization": config.API_TOKEN}

            async with session.get(config.BUYER.format(user_data["userGUID"]), headers=headers) as response:
                result = await response.text()
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail=result)
                return json.loads(result)
                
class JwtManager:

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days= 7)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, config.JWT_KEY, config.JWT_ALGORITHM)
        return encoded_jwt   
    
    @classmethod
    async def decode_access_token(cls, authorisation_token):
        try:
            user_info = jwt.decode(token=authorisation_token, key=config.JWT_KEY, algorithms=config.JWT_ALGORITHM)
        except:
            raise HTTPException(status_code=400, detail="cookies are not correct")
        return user_info
    
class Utils:
    @classmethod
    async def rights_check(cls, user_data: dict):
        match user_data["role"].lower():
            case "administrator":
                user_data["user_info"] = None
            case "seller":
                user_data["role"] = UserRole.Seller
                user_data["user_info"] = await UserDAO.get_info_representative(user_data)
            case "shop":
                user_data["role"] = UserRole.Shop
                user_data["user_info"] = await UserDAO.get_info_sales_point(user_data)

