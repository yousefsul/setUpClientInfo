import shortuuid


class ClientInfo:
    def __init__(self, client_info):
        self.__client_info = client_info
        self.__client_info_dict = {}
        self.__client_id = None
        self.__client_name = None
        self.__client_phone_number = None
        self.__client_street_address = None
        self.__client_city = None
        self.__client_state = None
        self.__client_zip = None
        self.__client_contact_last_name = None
        self.__client_contact_first_name = None
        self.__client_contact_email = None
        self.__extract_client_data()
        self.__bulid_main_dict()

    def __extract_client_data(self):
        self.__client_id = "client_" + str(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
        for count, row in self.__client_info.iterrows():
            self.__client_data = self.__client_info.loc[count]
            self.__client_name = self.__client_data.get("Client Name")
            self.__client_phone_number = int(self.__client_data.get("Phone"))
            self.__client_street_address = self.__client_data.get("Steet Address")
            self.__client_city = self.__client_data.get("City")
            self.__client_state = self.__client_data.get("State")
            self.__client_zip = int(self.__client_data.get("Zip"))
            self.__client_contact_last_name = self.__client_data.get("Contact Last Name")
            self.__client_contact_first_name = self.__client_data.get("Contact First Name")
            self.__client_contact_email = self.__client_data.get("Contact Email")

    def __bulid_main_dict(self):
        self.__client_info_dict = {
            "client_id": self.__client_id,
            "name": self.__client_name,
            "phone": self.__client_phone_number,
            "address": {
                "street_address": self.__client_street_address,
                "city": self.__client_city,
                "state": self.__client_state,
                "zip": self.__client_zip
            },
            "contact": {
                "last": self.__client_contact_last_name,
                "first": self.__client_contact_first_name,
                "role": "owner",
                "email": self.__client_contact_email
            }
        }

    def get_client_info(self):
        return self.__client_info_dict
