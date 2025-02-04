from pydantic import BaseModel



class PropertyGroup(BaseModel):
    NoFilter: bool = False
    Apartment_1: bool = True
    GardenApartment_3: bool = True
    Studio_4: bool = True
    Cottage_5: bool = True
    Penthouse_6: bool = True
    Duplex_7: bool = True
    HousingUnit_11: bool = True
    TourismAndRecreation_25: bool = True
    TwoFamily_39: bool = True
    Basement_49: bool = True
    Triplex_51: bool = True


    def __str__(self):
        if self.NoFilter:
            return ""
        properties = [k.split("_")[1] for k, v in self.__dict__.items() if v]
        return f"property={",".join(properties)}"

