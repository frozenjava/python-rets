from hashlib import md5
from rets.versions.rets_version import RETSVersion


class Configuration(object):
    AUTH_BASIC = 'basic'
    AUTH_DIGEST = 'digest'
    allowed_auth = [AUTH_BASIC, AUTH_DIGEST]

    username = None
    password = None
    login_url = None
    user_agent = 'Python RETS'
    user_agent_password = None
    rets_version = None
    _http_authentication = 'digest'
    options = {}

    def __init__(self, version='1.5'):
        self.rets_version = RETSVersion(version)

    @property
    def http_authentication(self):
        return self._http_authentication

    @http_authentication.setter
    def http_authentication(self, auth_method):
        if auth_method not in self.allowed_auth:
            raise ValueError("Given authentication method is invalid, must be in {}".format(self.allowed_auth))
        self._http_authentication = auth_method

    def load(self, configuration=None):
        if configuration is None:
            configuration = []

        variables = {
            'username': 'Username',
            'password': 'Password',
            'login_url': 'LoginUrl',
            'user_agent': 'UserAgent',
            'user_agent_password': 'UserAgentPassword',
            'rets_version': 'RetsVersion',
            'http_authentication': 'HttpAuthenticationMethod'
        }

        # Not sure yet what to do here
        # https://github.com/troydavisson/PHRETS/blob/master/src/Configuration.php#L175
        me = {}

        for k, v in variables.items():
            if k in configuration:
                me[k] = configuration[k]

    def is_valid(self):
        return None not in [self.login_url, self.username]

    def user_agent_digest_hash(self, session):
        ua_a1 = md5.new('{0}:{1}::{2}:{3}'.format(self.user_agent.strip(),
                                                  self.user_agent_password.strip(),
                                                  session.client.strip(),
                                                  self.rets_version.as_header().strip())).digest()
        return ua_a1
