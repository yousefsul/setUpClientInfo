import shortuuid


class InsuranceInfo:
    def __init__(self, insurance_info):
        self.__insurance_info = insurance_info
        self.__insurance_info_dict = {}
        self.__insurance_info_list = []
        self.__insurance_id = None
        self.__insurance_name = None
        self.__insurance_street_address = None
        self.__insurance_city = None
        self.__insurance_state = None
        self.__insurance_zip = None
        self.__insurance_phone_number = None
        self.__insurance_first_phone_number = None
        self.__insurance_second_phone_number = None
        self.__insurance_phone_number_extenstion = None
        self.__insurance_payer_id = None
        self.__extract_insurance_data()

    def __extract_insurance_data(self):
        phone_number = None
        self.__insurance_id = int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
        for count, row in self.__insurance_info.iterrows():
            self.__insurance_data = self.__insurance_info.loc[count]
            self.__insurance_name = self.__insurance_data.get("Insurance Name")
            self.__insurance_payer_id = self.__insurance_data.get("Payer ID")
            self.__insurance_street_address = self.__insurance_data.get("Address")
            self.__insurance_city = self.__insurance_data.get("City")
            self.__insurance_state = self.__insurance_data.get("State")
            self.__insurance_zip = self.__insurance_data.get("Zip")
            self.__insurance_phone_number = self.__insurance_data.get("Phone")
            if type(self.__insurance_phone_number) == str:
                self.__insurance_phone_number = self.__insurance_data.get("Phone").splitlines()
                if len(self.__insurance_phone_number) == 1:
                    phone_number = self.__insurance_phone_number[0].split("ext.")
                    self.__insurance_first_phone_number = {
                        "number": int(phone_number[0]),
                        "extenstion": int(phone_number[1])
                    }
                    self.__insurance_second_phone_number = 0
                    break
                if len(self.__insurance_phone_number) == 2:
                    self.__insurance_first_phone_number = self.__insurance_phone_number[0]
                    self.__insurance_second_phone_number = self.__insurance_phone_number[1]
                    break
            else:
                self.__insurance_first_phone_number = int(self.__insurance_data.get("Phone"))
            self.__bulid_main_dict()

    def __bulid_main_dict(self):
        pass