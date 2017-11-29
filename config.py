class Config(object):
    """Base config class."""
    SECRET_KEY = '你的密钥'
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
	# MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True