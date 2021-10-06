from bson import Decimal128


class CPTSInfo:
    def __init__(self, cpts_info):
        self.__cpts_info = cpts_info
        self.__cpts_dict = {}
        self.__cpt_name = None
        self.__cpt_allowable = None
        self.__cpt_fee = None
        self.__extract_cpts_data()

    def __extract_cpts_data(self):
        for count, row in self.__cpts_info.iterrows():
            self.__cpts_data = self.__cpts_info.loc[count]
            self.__cpt_name = int(self.__cpts_data.get("CPT"))
            allowable = Decimal128(str(self.__cpts_data.get("Allowable")))
            cpt_allowable = "{:.2f}".format(allowable.to_decimal())
            self.__cpt_allowable = cpt_allowable
            fee = Decimal128(str(self.__cpts_data.get("Fee")))
            cpt_fee = "{:.2f}".format(fee.to_decimal())
            self.__cpt_fee = cpt_fee
            self.__bulid_main_dict()

    def __bulid_main_dict(self):
        cpt_dict = {
            self.__cpt_name: {
                "allowable": self.__cpt_allowable,
                "fee": self.__cpt_fee,
            }
        }
        self.__cpts_dict.update(cpt_dict)

    def get_cpts_info(self):
        return self.__cpts_dict
