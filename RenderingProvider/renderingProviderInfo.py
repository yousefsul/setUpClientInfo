class RenderingProvder:
    def __init__(self, rendering_provider_info):
        self.__rendering_provider_info = rendering_provider_info
        self.__rendering_provider_dict = {}
        self.__rendering_provider_id = None
        self.__rendering_provider_last_name = None
        self.__rendering_provider_first_name = None
        self.__rendering_provider_speciality = None
        self.__rendering_provider_speciality_code = None
        self.__rendering_provider_speciality_description = None
        self.__rendering_provider_state = None
        self.__rendering_provider_license_number = None
        self.__rendering_provider_npi = None
        self.__rendering_provider_entity_type = None
        self.__rendering_provider_phone = None

        
        self.__rendering_provider_data()
        self.__bulid_main_dict()

    def __rendering_provider_data(self):
        pass

    def __bulid_main_dict(self):
        pass