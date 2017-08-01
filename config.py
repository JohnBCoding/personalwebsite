import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(basedir, "app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")

WTF_CSRF_ENABLED = True
SECRET_KEY = "test-code-please-ignore"

# Pagination
POSTS_PAGE = 1

