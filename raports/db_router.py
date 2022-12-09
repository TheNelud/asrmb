from .models import *


ROUTED_MODELS_RAPORTS= []


class Raport_db_router(object):
    
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_RAPORTS:
            return 'raport'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_RAPORTS:
            return 'raport'
        return None