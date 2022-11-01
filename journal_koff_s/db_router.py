from .models import *

ROUTED_MODELS_COMPRESS = [CoefPTM,
                          P2Calc,
                          P3Calc,
                          P4Calc,
                          P5Calc,
                          P6Calc,
                          P7Calc,
                          TabCoefAll,
                          TabSumAll,
                          TotalCalc]



class Compress_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_COMPRESS:
            return 'compress'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_COMPRESS:
            return 'compress'
        return None