from rolepermissions.roles import AbstractUserRole


class MapEditor(AbstractUserRole):
    available_permissions = {
        'edit_branch_map': True,
    }
