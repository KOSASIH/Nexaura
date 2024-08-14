class Config:
    SECRET_KEY = 'secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///nexaura.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PI_NETWORK_NODE = 'https://node.pi.network'
    AI_ENGINE_MODEL = 'model.h5'
