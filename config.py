from decouple import config

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    
    DEBUG = True
    MYSQL_HOST='sicovodb.cnwv31dgaz08.us-east-1.rds.amazonaws.com'
    MYSQL_USER='admin'
    MYSQL_PASSWORD='admin123'
    MYSQL_DB='tienda_sicovo'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '20213tn063@utez.edu.mx'
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}