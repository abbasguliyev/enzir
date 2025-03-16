from sqladmin import ModelView
from src.auth.models import User

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.is_active, User.is_superuser]
    column_labels = {
        User.id: 'ID',
        User.username: 'Username',
        User.email: 'Email',
        User.is_active: 'Active',
        User.is_superuser: 'Superuser'
    }
    page_size = 10
