from .models import *

ROUTED_MODELS_PERIOD = [Calc_losses,
                        Losses_gas_apparatus,
                        ]


class Period_db_router(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_PERIOD:
            return 'period'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_PERIOD:
            return 'period'
        return None
