import re

import shortuuid


class BillingProviderInfo:
    def __init__(self, billing_provider_info):
        self.__billing_provider_info = billing_provider_info
        self.__billing_provider_dict = {}
        self.__billing_provider_list = []
        self.__billing_provider_id = None
        self.__billing_provider_name = None
        self.__billing_provider_entity_type = None
        self.__billing_provider_street_address = None
        self.__billing_provider_city = None
        self.__billing_provider_state = None
        self.__billing_provider_zip_code = None
        self.__billing_provider_npi = None
        self.__billing_provider_primary_taxonomy = {}
        self.__billing_provider_secondary_taxonomy = {}
        self.__billing_provider_pri_taxonomy = None
        self.__billing_provider_sec_taxonomy = None
        self.__billing_provider_taxonomy_code = None
        self.__billing_provider_taxonomy_description = None
        self.__billing_provider_license_number = None
        self.__extract_billing_provider_data()

    def __extract_billing_provider_data(self):
        self.__billing_provider_id = int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
        for count, row in self.__billing_provider_info.iterrows():
            self.__billing_provider_data = self.__billing_provider_info.loc[count]
            self.__billing_provider_name = self.__billing_provider_data.get("Billing Provider Name")
            self.__billing_provider_entity_type = int(self.__billing_provider_data.get("Entity Type"))
            self.__billing_provider_street_address = self.__billing_provider_data.get("Address")
            self.__billing_provider_city = self.__billing_provider_data.get("City")
            self.__billing_provider_state = self.__billing_provider_data.get("State")
            self.__billing_provider_zip_code = self.__billing_provider_data.get("Zip")
            self.__billing_provider_npi = self.__billing_provider_data.get("NPI")
            self.__billing_provider_license_number = int(self.__billing_provider_data.get("License Number"))
            self.__extract_taxonomy()
            self.__bulid_main_dict()
            self.__billing_provider_list.append(self.__billing_provider_dict)

    def __extract_taxonomy(self):
        try:
            self.__billing_provider_pri_taxonomy = self.__billing_provider_data.get \
                ("Primary Taxonomy level 1").strip().split(" ", 1)
            self.__billing_provider_taxonomy_code = self.__billing_provider_pri_taxonomy[0]
            self.__billing_provider_taxonomy_description = re.sub('[^A-Za-z0-9 ]+', '',
                                                                  self.__billing_provider_pri_taxonomy[1]).strip()
            self.__billing_provider_primary_taxonomy = {
                "code": self.__billing_provider_taxonomy_code,
                "description": self.__billing_provider_taxonomy_description
            }

            self.__billing_provider_sec_taxonomy = self.__billing_provider_data.get \
                ("Primary Taxonomy level 2").strip().split(" ", 1)

            self.__billing_provider_taxonomy_code = self.__billing_provider_sec_taxonomy[0]
            self.__billing_provider_taxonomy_description = re.sub('[^A-Za-z0-9 ]+', '',
                                                                  self.__billing_provider_sec_taxonomy[1]).strip()

            self.__billing_provider_secondary_taxonomy = {
                "code": self.__billing_provider_taxonomy_code,
                "description": self.__billing_provider_taxonomy_description
            }
        except Exception as e:
            pass

    def __bulid_main_dict(self):
        self.__billing_provider_dict = {
            "billing_provider_id": self.__billing_provider_id,
            "billing_provider_name": self.__billing_provider_name,
            "entity_type": self.__billing_provider_entity_type,
            "address": {
                "street_address": self.__billing_provider_street_address,
                "city": self.__billing_provider_city,
                "state": self.__billing_provider_state,
                "zip": self.__billing_provider_zip_code
            },
            "npi": self.__billing_provider_npi,
            "license_number": self.__billing_provider_license_number
        }

    def get_billing_provider_info(self):
        return self.__billing_provider_list
