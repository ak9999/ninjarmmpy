from .utils import return_response, api_get_request

import requests

class DeviceMixin():
    # Devices
    NINJA_API_DEVICE = '/v2/device/'

    api_get_request = api_get_request

    def __init__(self):
        pass

    # Organization info
    @return_response
    def get_device_details(self, id: int = None) -> requests.Response:
        """Returns device details

        Keyword arguments:
        id: int       -- Group identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}')