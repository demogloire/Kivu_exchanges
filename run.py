import os
from environs import Env
from app import create_app

env = Env()
env.read_env()

config_name = env.str("FLASK_CONFIG", default='development')

print('this is the config name ===>', config_name)
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
