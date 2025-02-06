from fastapi import APIRouter, HTTPException, status
import logging
from app.service.yad2_sale_service.sale_service import update_ads_in_db_from_api
from app.models.city_model import City

sale_router = APIRouter()

@sale_router.post("/sale-ad", status_code=status.HTTP_200_OK)
def create_sale_ad(request: City):
    try:
        # Trigger the service function with the provided city.
        result = update_ads_in_db_from_api(request)
        return {
            "message": "Sale advertisement processed successfully.",
            "data": result
        }
    except Exception as e:
        logging.exception("Error processing sale advertisement")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )