# -*- coding: utf-8 -*-
DB_NAME = 'vmail'
DB_USER = 'vmail'
DB_PW   = '{{postfix.dovecot.mysql_password}}'
MAIL_ADDR = '{{postfix.postmaster}}'
HOST    = '{{postfix.dovecot.host}}'
DOMAINS = [
{% if postfix.mailman is defined %}
{% for item in postfix.mailman.domains %}
  '{{item}}',
{% endfor %}
{% endif %}
{% if postfix.dovecot is defined %}
{% for item in postfix.dovecot.domains %}
  '{{item}}',
{% endfor %}
{% endif %}
]
