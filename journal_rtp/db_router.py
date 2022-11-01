from .models import *

ROUTED_MODELS_CONDENSATECALC = [CondensateprodOne,
                                CondensateprodThree1,
                                CondensateprodThree2,
                                CondensateprodTwo,
                                CondrecyclingEight,
                                CondrecyclingFive,
                                CondrecyclingSix,
                                CondrecyclingTen,
                                CondrecyclingFour,
                                CondrecyclingNine,
                                CondrecyclingOne,
                                CondrecyclingSeven,
                                CondrecyclingThree,
                                CondrecyclingTwo,
                                CondrecyclingTwoDop,
                                CondrecyclingTwoDop2]

ROUTED_MODELS_GASCALC = [RecyclingcalcFive1,
                         RecyclingcalcFive2,
                         RecyclingcalcFour,
                         RecyclingcalcOne,
                         RecyclingcalcSix,
                         RecyclingcalcThree,
                         RecyclingcalcTime,
                         RecyclingcalcTwo,
                         Teclosses2dop,
                         TeclossesOne,
                         TeclossesTree,
                         TeclossesTreeDop,
                         TeclossesTwo]




class Condensatecalc_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_CONDENSATECALC:
            return 'condensatecalc'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_CONDENSATECALC:
            return 'condensatecalc'
        return None


class Gascalc_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_GASCALC:
            return 'gascalc'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_GASCALC:
            return 'gascalc'
        return None



