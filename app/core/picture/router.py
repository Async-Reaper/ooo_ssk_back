from fastapi import APIRouter, Body, Path, HTTPException, Response, Request, status, Depends
from fastapi import Request, Response
from ..utils import utils
from .schemas import *
from .actions import *

router_picture = APIRouter(
    tags=["picture"],
    prefix="/api/picture"
)

@router_picture.post("/create_picture")
async def create_picture(picture_data: PictureInput):

    presencePic = await PictureDAO.serch_picture_py_name(picture_data.model_dump()["file_name"], 
                                                         picture_data.model_dump()["picture_type"].value)
    
    picture_dict = await utils.grouping_picture_data(nomenclature_data=picture_data)
    picture_dict["path"] = picture_dict["path"].replace("./templates", "/static")
    await PictureManager.image_decoding_and_recording(picture_data=picture_data)
    if not presencePic:
        await PictureDAO.picture_creation(**picture_dict)
        return None
    
    await PictureDAO.update_picture_by_name(picture_data.model_dump()["file_name"], 
                                            picture_data.model_dump()["picture_type"].value,
                                            **picture_dict)
    
