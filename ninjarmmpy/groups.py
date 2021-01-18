from .utils import return_response, api_get_request


class GroupsMixin():
    # Groups
    NINJA_API_GROUP = '/v2/group/'

    api_get_request = api_get_request

    def __init__(self):
        pass

    # Organization info
    @return_response
    def getGroupDeviceIds(self, id: int = None, refresh: bool = None):
        """Returns list of device identifiers that match group criteria
        Keyword arguments:
        id: int       -- Group identifier, required, no default provided.
        refresh: str  -- refresh group?
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {'id': id, 'refresh': refresh}
        return self.api_get_request(f'{self.NINJA_API_GROUP}{id}/device-ids', params=params)
