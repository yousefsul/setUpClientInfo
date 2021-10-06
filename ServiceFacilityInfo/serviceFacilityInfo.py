import shortuuid


class ServiceFacilityInfo:
    def __init__(self, service_facility_info):
        self.__service_facility_info = service_facility_info
        self.__service_facility_dict = {}
        self.__service_facility_id = None
        self.__service_facility_name = None
        self.__service_facility_street_address = None
        self.__service_facility_city = None
        self.__service_facility_state = None
        self.___service_facility_zip_code = None
        self.___service_facility_npi = None
        self.___service_facility_entity_type = 2
        self.__extract_service_facility_data()
        self.__bulid_main_dict()

    def __extract_service_facility_data(self):
        self.__service_facility_id = int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
        for count, row in self.__service_facility_info.iterrows():
            self.__service_facility_data = self.__service_facility_info.loc[count]
            self.__service_facility_name = self.__service_facility_data.get("Service Location")
            self.__service_facility_street_address = self.__service_facility_data.get("Address")
            self.__service_facility_city = self.__service_facility_data.get("City")
            self.__service_facility_state = self.__service_facility_data.get("State")
            self.___service_facility_zip_code = self.__service_facility_data.get("Zip")
            self.___service_facility_npi = int(self.__service_facility_data.get("NPI"))

    def __bulid_main_dict(self):
        self.__service_facility_dict = {
            "service_facility_id": self.__service_facility_id,
            "name": self.__service_facility_name,
            "address": {
                "street_address": self.__service_facility_street_address,
                "city": self.__service_facility_city,
                "state": self.__service_facility_state,
                "zip": self.___service_facility_zip_code
            },
            "npi": self.___service_facility_npi,
            "entity_type": self.___service_facility_entity_type,
        }

    def get_service_facility_info(self):
        return self.__service_facility_dict

