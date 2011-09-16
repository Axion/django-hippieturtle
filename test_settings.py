DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hippieturtle',
        'USER': 'root',
        'PASSWORD': '14121988'

    }
}

DISABLE_TRANSACTION_MANAGEMENT = True

INSTALLED_APPS = (
    'orm_tests',
)

DEBUG=False