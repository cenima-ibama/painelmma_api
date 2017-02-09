class SiscomRouter(object):
    """
    A router to control all database operations on models in the
    restApp application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read operations models go to painelmma_db.
        """
        if model._meta.app_label == 'painelmma_api':
            return 'painelmma_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write operations models go to painelmma_db.
        """
        if model._meta.app_label == 'painelmma_api':
            return 'painelmma_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the operations app is involved.
        """
        if obj1._meta.app_label == 'painelmma_api' or \
            obj2._meta.app_label == 'painelmma_api':
            return True
        return None