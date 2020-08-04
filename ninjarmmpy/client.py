from ninjarmmpy.system import SystemMixin
from ninjarmmpy.organization import OrganizationMixin
from ninjarmmpy.groups import GroupsMixin
from ninjarmmpy.device import DeviceMixin
from ninjarmmpy.queries import QueriesMixin


class Client(SystemMixin, OrganizationMixin, GroupsMixin, DeviceMixin, QueriesMixin):
    NINJA_API_US_BASE_URL = 'https://api.ninjarmm.com'
    NINJA_API_EU_BASE_URL = 'https://eu-api.ninjarmm.com'

    def __init__(self, AccessKeyID: str, SecretAccessKey: str, Europe=False):
        self.key = AccessKeyID
        self.secret = SecretAccessKey
        self.europe = Europe
        self.base_url = self.NINJA_API_US_BASE_URL if not self.europe else self.NINJA_API_EU_BASE_URL

    def __repr__(self):
        return f'{type(self).__name__}(AccessKeyID={self.key!r}, SecretAccessKey={self.secret!r}, Europe={self.europe!r})'
