import numpy as np
import pandas as pd

from BillingProvider.billingProviderInfo import BillingProviderInfo
from CPTSInfo.cptsInfo import CPTSInfo
from ClientInfo.clientInfo import ClientInfo
from InsuranceInfo.insuranceInfo import InsuranceInfo
from ServiceFacilityInfo.serviceFacilityInfo import ServiceFacilityInfo


class SetupClient:
    def __init__(self, client_file):
        self.__client_file = client_file
        self.__client_excel_file = pd.ExcelFile(self.__client_file)
        self.__extract_client_info()
        self.__extract_insurance_info()
        # self.__extract_billing_provider_info()
        # self.__extract_service_facility_info()
        # self.__extract_cpts_info()

    def __extract_client_info(self):
        self.__client_info = pd.read_excel(self.__client_excel_file, 'Client_Info').replace(np.nan, '', regex=True)
        self.__client_info_obj = ClientInfo(self.__client_info)

    def __extract_insurance_info(self):
        self.__insurance_info = pd.read_excel(self.__client_excel_file, 'Insurance_Info').replace(np.nan, '',
                                                                                                  regex=True)
        self.__insurance_info_obj = InsuranceInfo(self.__insurance_info)
        # print(json.dumps(self.__insurance_info_obj.() , indent= 4 ))


    def __extract_billing_provider_info(self):
        self.__billing_provider_info = pd.read_excel(self.__client_excel_file, 'Billing_Provider') \
            .replace(np.nan, '', regex=True)
        self.__billing_provider_info_obj = BillingProviderInfo(self.__billing_provider_info)

    def __extract_service_facility_info(self):
        self.__service_facility_info = pd.read_excel(self.__client_excel_file, 'Service_Facility_Info') \
            .replace(np.nan, '', regex=True)
        self.__service_facility_info_obj = ServiceFacilityInfo(self.__service_facility_info)

    def __extract_cpts_info(self):
        self.__cpts_info = pd.read_excel(self.__client_excel_file, 'CPTs') \
            .replace(np.nan, '', regex=True)
        self.__cpts_info_obj = CPTSInfo(self.__cpts_info)
