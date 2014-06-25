from kili.settings import *
from horizon.utils import secret_key
SECRET_KEY = secret_key.generate_or_read_from_file('/var/lib/openstack-dashboard/secret_key')

KEYSTONE_TOKEN = "{{ keystone_admin_token }}" 
KEYSTONE_URL = "{{ keystone_admin_url }}"

BROKER_URL = 'amqp://{{ horizon_dashboard_rabbit_user }}:{{ horizon_dashboard_rabbit_password }}@{{ keystone_endpoint_host }}/{{ horizon_dashboard_rabbit_vhost }}'

DATABASES = { 
        'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'horizon_dashboard',
                    'USER': 'horizon',
                    'PASSWORD': '{{ horizon_dashboard_db_password }}',
                    'HOST': '{{ keystone_endpoint_host }}',
                    'PORT': '3306',
                },
}

OPENSTACK_HOST = "{{ keystone_endpoint_host }}"
OPENSTACK_KEYSTONE_URL = "http://{}:5000/v2.0".format(OPENSTACK_HOST)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CACHES = {
   'default': {
       'BACKEND' : 'django.core.cache.backends.memcached.MemcachedCache',
       'LOCATION' : '127.0.0.1:11211',
   }
}

COMPRESS_OFFLINE = True

ENV_NAME = "{{ env_name }}"

NEWRELIC_CONFIG_FILE = "{{ newrelic_config_path }}/newrelic_webapp.ini"

OPENSTACK_SSL_NO_VERIFY = True

LOGGING['handlers']['syslog']['level'] = "{{ horizon_min_loglevel }}"


# MERCHANT SETTINGS
MERCHANT_TEST_MODE = False

MERCHANT_SETTINGS = {
    "stripe": {
        "API_KEY": "{{ stripe_api_key }}",
        "PUBLISHABLE_KEY": "{{ stripe_pub_key }}",
    }
}

CEILOMETER_API_VERSION = 2
CEILOMETER_AUTH_DATA = {
            'os_username': 'ceilometer',
            'os_password': '{{ ceilometer_identity_password }}',
            'os_tenant_name': 'service',
            'os_auth_url': 'http://{{ public_api_address }}/keystone/v2.0'}
