from rolepermissions.roles import AbstractUserRole 

class Admin(AbstractUserRole):
    available_permissions = {
        'accept_requests_account': True,
        'write_article': True,
        'modify_article': True,
        'delete_article': True,
    }

class Author(AbstractUserRole):
    available_permissions = {
        'write_article': True,
        'modify_article': True,
    }

class Registreduser(AbstractUserRole):
    available_permissions = {
        'read_article': True,
    }