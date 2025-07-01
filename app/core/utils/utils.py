from config import PATH_IMAGE
from ..picture.models import Picture
from ..picture.actions import PictureDAO
from ..basket.schemas import BasketItem
from ..nomenclature.actions import NomenclatureDAO
from ..nomenclature.schemas import NomenclatureOutput
from ..nomenclature.actions import UtilsDAO

async def convert_str_to_type(values: dict) -> None:
    for value in values.values():
        try:
            bool(value)
        except:
            continue

async def nomenclature_data_distribution_manager(nomenclature_data: list) -> dict:
    result = {}
    return_data = {}

    for key, value in nomenclature_data:
        key_lower = key.lower()

        if key_lower == "title_products":
            return_data["title_products"] = value
            continue
        elif key_lower == "contract_guid":
            return_data["contract_guid"] = value
            continue

        # Преобразование true/false
        if value.lower() == "true":
            processed_value = True
        elif value.lower() == "false":
            processed_value = False
        else:
            processed_value = value

        # Обработка matrix как списка
        if key == "matrix":
            if key not in result:
                result[key] = []
            result[key].append(processed_value)
        else:
            result[key] = processed_value

    return_data["result"] = result
    return return_data

# async def nomenclature_data_distribution_manager(nomenclature_data: dict) -> dict:
#     result = {}
#     return_data = {}
#     for element in nomenclature_data:
#         if element[1].lower() == "true":
#             result.update({element[0]: True})
#             continue
#         elif element[0].lower() == "contract_guid":
#             return_data.update({"contract_guid": element[1]})
#             continue 
#         elif element[1].lower() == "false":
#             result.update({element[0]: False})
#             continue
#         elif element[0].lower() == "title_products":
#             return_data.update({"title_products": element[1].lower()})
#             continue
#         result.update({element[0]: element[1]})

#     return_data.update({"result": result})

#     return return_data

async def grouping_picture_data(nomenclature_data: Picture) -> dict:
    file_path = f"{PATH_IMAGE}{nomenclature_data.picture_category.value}/{nomenclature_data.guid_object}"
    result = {
        "guid_object": nomenclature_data.guid_object,
        "picture_type": nomenclature_data.picture_type.value,
        "picture_category":nomenclature_data.picture_category.value,
        "file_name": nomenclature_data.file_name,
        "is_main": nomenclature_data.is_main,
        "is_deleted": nomenclature_data.is_deleted,
        "path": f"{file_path}/{nomenclature_data.file_name}.{nomenclature_data.picture_type.value}"
    }
    return result

async def get_object_by_object(object_guid: str):
    return await PictureDAO.get_object_by_object(object_guid) 

async def add_objects_with_pictures(products: BasketItem) -> list:
    for product in products:
        try:
            guid = product.guid
        except:
            guid = product.product_guid

        testdata = {
            "guid_object": "00000000-0000-0000-0000-000000000000",
            "path": "/static/None/None.jpg",
            "picture_type": "jpg",
            "picture_category": "groups",
            "file_name": "Null pic",
            "is_deleted": False,
            "is_main": True
          }

        # product.pictures = await get_object_by_object(guid)
        _pictures = await get_object_by_object(product.guid)
        product.pictures = _pictures if _pictures else [testdata]
        # product.pictures = testdata

async def add_objects_with_picture(product: NomenclatureOutput) -> NomenclatureOutput:
        guid = product.guid
        product.pictures = await get_object_by_object(guid)

async def add_objects_with_more_info(products: list[BasketItem]) -> BasketItem:
    testdata = {
            "guid_object": "00000000-0000-0000-0000-000000000000",
            "path": "/static/None/None.jpg",
            "picture_type": "jpg",
            "picture_category": "groups",
            "file_name": "Null Pic",
            "is_deleted": False,
            "is_main": True
          }
    
    for product in products:

        product.other_data = await NomenclatureDAO.get_nomenclature_by_guid(product.product_guid)

        if product.other_data:
            _pictures = await get_object_by_object(product.product_guid)
            # product.other_data.pictures = await get_object_by_object(product.product_guid)
            product.other_data.additional_information = await UtilsDAO.get_more_info_product(product.product_guid, product.contract_guid)
            product.other_data.pictures = _pictures if _pictures else [testdata]

async def get_element_by_guid(elements: list, guid: str):
    result = []
    index = len(elements)-1
    for _ in reversed(elements):
        if _.parent_guid != "":
            if _.parent_guid == guid:
                result.append(_)
                elements.pop(index)
        index -= 1

    return result



