GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/docs/orders/{гуид заказа}



GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}



GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/buyer/{ГУИД торговой точки}/debts



GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/docs/orders/{гуид заказа}/declaredItems 



POST          
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
data = {
"productItems": productGuid,
"contractGUID": contractGuid 
}
http://192.168.0.10/nomenclatures/history
            


POST
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
data = {
"startDate": startDate,
"endDate": endDate,
"contractGUID": contractGuid
}
http://192.168.0.10/docs/orders/history



POST
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/docs/orders/build", 
                                    


POST
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/docs/orders/approve



GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/TradeWeb/hs/api/representative/{userGUID}/currentData"


GET
headers = {
    "Authorization": Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6aGpkdGg=
}
http://192.168.0.10/TradeWeb/hs/api/shop/{userGUID}/currentData"