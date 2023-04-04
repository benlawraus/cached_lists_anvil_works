from anvil.tables.basefunction import BaseFunction

TABLES = dict(
    sailboats=dict(
        name='string',
        length='number',
        sails='simpleObject',
        user_email='string',
    ),
    users=dict(
        email='string',
        enabled='bool',
        last_login='datetime',
        password_hash='string',
        n_password_failures='number',
        confirmed_email='bool',
        signed_up='datetime',
    ),
)


class AppTables:
    def __init__(self):
        self.sailboats = BaseFunction('sailboats', TABLES['sailboats'])
        self.users = BaseFunction('users', TABLES['users'])


app_tables = AppTables()
