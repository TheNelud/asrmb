from .models import *

ROUTED_MODELS_KOFF = [Coef, Losses, MolMass]


class Coefficients_db_router(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_KOFF:
            return 'coefficients'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_KOFF:
            return 'coefficients'
        return None
