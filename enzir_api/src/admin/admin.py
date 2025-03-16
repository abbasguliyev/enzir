from sqladmin import Admin
from src.database import engine
from fastapi import FastAPI
from src.admin.user import UserAdmin
from src.admin.mesvere import MesvereAdmin, MesvereQeydleriAdmin

def create_admin(app):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(MesvereAdmin)
    admin.add_view(MesvereQeydleriAdmin)
    return admin