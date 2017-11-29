from flask_sqlalchemy import SQLAlchemy             
from main import app


# INIT the sqlalchemy object                            
# Will be load the SQLALCHEMY_DATABASE_URL from config.py
# SQLAlchemy 会自动的从 app 对象中的 DevConfig 中加载连接数据库的配置项
db = SQLAlchemy(app)

class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self,id,username,password):
		self.id = id
		self.password = password
		self.username = username

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)