from .models import *

ROUTED_MODELS_GAS_MASSA = [P5_app,
                           P6_app,
                           Const,
                           Perehod_stabilizacii,
                           Data_gas_stabilization]


class Gas_massa_db_router(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_GAS_MASSA:
            return 'gas_massa'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_GAS_MASSA:
            return 'gas_massa'
        return None