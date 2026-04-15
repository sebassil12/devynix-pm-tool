from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

#### Variables ####
DATABASE_URL = env('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')



# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
