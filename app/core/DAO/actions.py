from aiohttp                import ClientSession
from fastapi        import HTTPException, status

import json
import config


class Dao:
    @classmethod
    async def get_order_header(cls, orderGuid: str):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.get(f"{config.URL_1C}/hs/api/docs/orders/{orderGuid}", 
                                    headers = headers) as response:
                result = json.loads(await response.text())
                return result
            
    @classmethod
    async def get_receive_accounts_receivable(cls, contractGuid: str):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.get(f"{config.URL_1C}/hs/api/buyer/{contractGuid}/debts", 
                                    headers = headers) as response:
                result = json.loads(await response.text())
                return result
            
    @classmethod
    async def get_order_table(cls, orderGuid: str):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.get(f"{config.URL_1C}/hs/api/docs/orders/{orderGuid}/declaredItems", 
                                    headers = headers) as response:
                result = json.loads(await response.text())
                return result
            
    @classmethod
    async def get_history_product(cls, productGuid: str, contractGuid: str):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }
            data = {
            "productItems": productGuid,
            "contractGUID": contractGuid 
            }
            async with session.post(f"{config.URL_1C}/hs/api/nomenclatures/history", 
                                    headers = headers, json= data) as response:
                result = json.loads(await response.text())
                if response.status != 404:
                    result = json.loads(await response.text())
                    return result
                raise HTTPException(status_code=404, detail="Данный пользователь не найден")
            
    @classmethod
    async def get_history_by_date(cls, startDate: str, endDate: str, contractGuid: str):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }
            data = {
            "startDate": startDate,
            "endDate": endDate,
            "contractGUID": contractGuid
            }
            async with session.post(f"{config.URL_1C}/hs/api/docs/orders/history", 
                                    headers = headers, json= data) as response:
                result = json.loads(await response.text())
                return result

    @classmethod
    async def build_order(cls, **kwargs):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.post(f"{config.URL_1C}/hs/api/docs/orders/build", 
                                    headers = headers, 
                                    json=dict(kwargs)) as response:
                result = json.loads(await response.text())
                if response.status != 200:
                    raise HTTPException(status_code=400, detail=result)

                return result
            
    @classmethod
    async def approve_order(cls, **kwargs):
        async with ClientSession() as session:
            headers = {
                "Authorization": config.API_TOKEN
            }

            async with session.post(f"{config.URL_1C}/hs/api/docs/orders/approve", 
                                    headers = headers, 
                                    json=dict(kwargs)) as response:
                result = json.loads(await response.text())
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail=result)

                return result