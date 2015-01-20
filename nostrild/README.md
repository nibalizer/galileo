nostrild
--------


authentication daemon for snot



description
-----------

nostrild performs ldap binds on user/password combinations and returns
cryptographically signed strings which can be used to authenticate
requests against other daemons




usage
-----


curl -XPOST -d '{"user": "nibz", "password": "derp"}' /auth




configuration
-------------


You can setup nostrild to bind to ldap, or to always allow authentication. See example_config.yaml for details. Your configuration will go in config.yaml



notes
-----


python-ldap requires libsasl2-dev
