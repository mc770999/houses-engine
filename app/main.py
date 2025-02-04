from fastapi import FastAPI

from app.routers.sale_rout import sale_router
from app.utils.json_util import write_data_on_json
from app.utils.api_util import get_yad2_url_rent, get_yad2_url_sale
import numpy as np

app = FastAPI()

app.include_router(sale_router, prefix="/users", tags=["Users"])


if __name__ == '__main__':
    print("start server")
    # city_name, city_code, pages = "natanya", "7400", 1
    # res = [get_api_by_page(get_yad2_url_sale(city_code,i)) for i in range(1, pages + 1)]
    # flat_res = np.array(res).flatten().tolist()
    # best_houses = calc_and_sorted(flat_res)
    # write_data_on_json(city_name, best_houses)
