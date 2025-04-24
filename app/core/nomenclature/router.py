from fastapi import APIRouter, Body, HTTPException, Response, status, Path, Request, Query
from ..utils.utils import convert_str_to_type, nomenclature_data_distribution_manager, add_objects_with_pictures, add_objects_with_picture

from .schemas import *
from .actions import *

nomenclature_router = APIRouter(
    prefix="/api",
    tags=["nomenclature"]
)


@nomenclature_router.post('/nomenclature/create_nomenclature')
async def create_nomenclatur(nomenclature_data: NomenclatureInput):
    nomenclature = await NomenclatureDAO.get_nomenclature_by_guid(nomenclature_data.guid)
    if not nomenclature:
        await NomenclatureDAO.nomenclature_creation(**nomenclature_data.model_dump())
        return None
    await NomenclatureDAO.update_product(**nomenclature_data.model_dump())
    
@nomenclature_router.get("/nomenclature/get_product/{product_guid}", response_model=NomenclatureOutput | None)
async def get_product(request: Request, product_guid: str = Path(..., description="GUID товара",min_length=36,max_length=36),
                      contract_guid: str | None = Query(None, description="GUID договора", min_length=36, max_length=36)):
    result = await NomenclatureDAO.get_nomenclature_by_guid(product_guid)
    await add_objects_with_picture(result)
    
    if "contract_guid" in request.query_params.items().mapping:
        result.additional_information = await UtilsDAO.get_more_info_product(result.guid, contract_guid)
    
    return result

@nomenclature_router.get("/nomenclature/get_product_by_options/{pages}/{limit}", response_model=NomenclatureGet)
async def get_product_by_options(request: Request,
                                pages: int = Path(..., description="Необходимая страница"),
                                limit: int = Path(..., description="Неоходимое количество в одной странице"),
                                title_products: str = Query(None, description="Частичное наименование товара", max_length=126),
                                brand_guid: str | None = Query(None, description="GUID бренда", min_length=36, max_length=36),
                                contract_guid: str | None = Query(None, description="GUID договора", min_length=36, max_length=36),
                                nomenclature_group: str | None = Query(None, description="GUID группы номенклатуры", min_length=36, max_length=36),
                                is_new: bool | None = Query(None, description="Признак того что товар должен быть новым"),
                                is_discount: bool | None = Query(None, description="Признак того что товар должен быть по скидке")):

    query_params = await nomenclature_data_distribution_manager(request.query_params.items())

    if not "title_products" in query_params:
        products = await NomenclatureDAO.get_product_by_options_without_title(pages = pages-1, 
                                                                              limit = limit, 
                                                                              **query_params["result"])
        result_serch = await NomenclatureDAO.get_product_by_options_without_title(pages = pages-1, 
                                                                              limit = limit,
                                                                              counter=True, 
                                                                              **query_params["result"])
                                                                              
    else:
        if query_params["title_products"] == "":
            products = await NomenclatureDAO.get_product_by_options_without_title(pages = pages-1, 
                                                                              limit = limit, 
                                                                              **query_params["result"])
            result_serch = await NomenclatureDAO.get_product_by_options_without_title(pages = pages-1, 
                                                                              limit = limit,
                                                                              counter=True, 
                                                                              **query_params["result"])
        else:
            products = await NomenclatureDAO.get_product_by_options_with_title(pages = pages-1, 
                                                                           limit = limit, 
                                                                           title=query_params["title_products"], 
                                                                           **query_params["result"])
            result_serch = await NomenclatureDAO.get_product_by_options_with_title(pages = pages-1, 
                                                                           limit = limit, 
                                                                           title=query_params["title_products"], 
                                                                           counter=True, **query_params["result"])
    
        
    if "contract_guid" in query_params and len(products) != 0:
        for product in products:
            product.additional_information = await UtilsDAO.get_more_info_product(product.guid, query_params["contract_guid"])

    await add_objects_with_pictures(products)
    total_count_products = await NomenclatureDAO.get_count_products()
    
    return {
        "total_count_products": total_count_products,
        "count_products": len(result_serch),
        "products": products
    }

@nomenclature_router.post("/nomenclature/get_nomenclatures", response_model=list[NomenclatureListOutput])
async def get_nomenclatures(nomencltureData: NomenclatureListInput):
    result = await NomenclatureDAO.get_nomenclatures(nomencltureData.nomenclatures)
    result.reverse()
    return result

@nomenclature_router.post("/nomenclature/get_nomenclatures_matrix", response_model=list[NomenclatureListOutput])
async def get_nomenclatures(nomencltureData: NomenclatureListInput):
    result = await NomenclatureDAO.get_nomenclatures_matrix(nomencltureData.nomenclatures)
    result.reverse()
    return result
    
    
    
# is_matrix: bool | None = Query(None, description="Признак того что товар матричный")