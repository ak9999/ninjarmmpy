from .utils import return_response, api_get_request


class OrganizationMixin():
    # Organization
    NINJA_API_ORGANIZATION = '/v2/organization/'

    api_get_request = api_get_request

    def __init__(self):
        pass

    # Organization info

    @return_response
    def getOrganization(self, id: int = None):
        """Returns organization details (policy mapping, locations)
        Keyword arguments:
        id: int       -- Organization identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_ORGANIZATION}{id}')

    @return_response
    def getOrganizationDevices(self, id: int = None, pageSize: int = None, after: int = None):
        """Returns list of organizations (Brief mode)
        Keyword arguments:
        id: int       -- Organization identifier, required, no default provided.
        pageSize: int -- Limit number of organizations to return
        after: int    -- Last organization Identifier from previous page
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {'id': id, 'pageSize': pageSize, 'after': after}
        return self.api_get_request(f'{self.NINJA_API_ORGANIZATION}{id}/devices', params=params)

    @return_response
    def getOrganizationLocations(self, id: int = None):
        """Returns list of locations for organization
        Keyword arguments:
        id: int       -- Organization identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_ORGANIZATION}{id}/locations')

    @return_response
    def getEndUsers(self, id: int = None):
        """Returns list of end-users for organization
        Keyword arguments:
        id: int       -- Organization identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_ORGANIZATION}{id}/end-users')
