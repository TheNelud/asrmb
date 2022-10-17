from .models import *

ROUTED_MODELS_KOFF = [Coef, Losses, MolMass]


class MyDBRouter(object):

    def db_for_read_koff(self, model, **hints):
        if model in ROUTED_MODELS_KOFF:
            return 'coefficients'
        return None

    def db_for_write_koff(self, model, **hints):
        if model in ROUTED_MODELS_KOFF:
            return 'coefficients'
        return None
