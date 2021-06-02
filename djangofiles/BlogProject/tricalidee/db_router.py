# usermanager/usermanager/db_router.py
class UserManagerDatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['data', 'staffs']:
            return 'primary'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'auth' or \
           obj2._meta.app_label == 'auth':
           return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'auth':
            return db == 'auth_db'
        elif app_label in ['staffs', 'data']:
            return db == 'primary'
        # No opinion for all other scenarios
        return None
