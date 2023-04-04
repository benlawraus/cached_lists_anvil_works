
import pathlib

from pydal import DAL, Field

db = None
logged_in_user = None
abs_path = pathlib.Path(__file__).parent / 'database'
if abs_path.exists() is False:
    abs_path.mkdir()

def define_tables_of_db():
    global db
    global abs_path
    if db is None:
        db = DAL('sqlite://storage.sqlite', folder=abs_path)
    # in following definitions, delete 'ondelete=..' parameter and CASCADE will be ON.

    if 'sailboats' not in db.tables:
        db.define_table('sailboats'
            , Field('name', type='string', default=None)
            , Field('length', type='integer', default=None)
            , Field('sails', type='json', default=None)
            , Field('user_email', type='string', default=None)
        )
    if 'users' not in db.tables:
        db.define_table('users'
            , Field('email', type='string', default=None)
            , Field('enabled', type='boolean', default=None)
            , Field('last_login', type='datetime', default=None)
            , Field('password_hash', type='string', default=None)
            , Field('n_password_failures', type='integer', default=None)
            , Field('confirmed_email', type='boolean', default=None)
            , Field('signed_up', type='datetime', default=None)
        )
    return

if __name__ == '__main__':
    define_tables_of_db()
