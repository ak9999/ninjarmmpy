from .utils import return_response

import requests
from email.utils import formatdate

from ninjarmmpy.auth import NinjaAuthentication

class Client():
    NINJA_API_US_BASE_URL = 'https://api.ninjarmm.com'
    NINJA_API_EU_BASE_URL = 'https://eu-api.ninjarmm.com'

    
    def __init__(self, AccessKeyID: str, SecretAccessKey: str, Europe=False):
        self.key = AccessKeyID
        self.secret = SecretAccessKey
        self.base_url = self.NINJA_API_US_BASE_URL if not Europe else self.NINJA_API_EU_BASE_URL


    def api_get_request(self, url, params: dict = {}):
        # params can't be used because functions break with them.
        api_url = self.base_url + url
        response = requests.get(url=api_url, auth=NinjaAuthentication(self.key, self.secret))
        print(response.encoding)
        return response
    

    def api_post_request(self, url, params: dict = {}):
        # params can't be used because functions break with them.
        api_url = self.base_url + url
        response = requests.post(url=api_url, auth=NinjaAuthentication(self.key, self.secret))
        return response


    # System
    # Core system Entities and Resources
    @return_response
    def get_organizations(self, pageSize: int = 999, after: int = 0) -> requests.Response:
        """Returns list of organizations (Brief mode)

        Keyword arguments:
        pageSize -- Limit number of organizations to return
        after    -- Last organization Identifier from previous page
        """
        import urllib
        params = {'after': after}
        if pageSize is not None:
            params.update({'pageSize': pageSize})
        del params  # params can't actually be used because the NinjaRMM API is still in beta.
        return self.api_get_request(f'/v2/organizations?')


    @return_response
    def get_attachment(self, id: str) -> requests.Response:
        """Returns attachment (image, document)

        Keyword arguments:
        id -- Attachment identifier
        """
        return self.api_get_request(f'/v2/attachment/{id}')


    @return_response
    def get_groups(self, lang: str = None) -> requests.Response:
        """List groups (saved searches)
        Returns list of groups

        Keyword arguments:
        lang: str -- Description
        """
        return self.api_get_request(f'/v2/groups?')
    

    @return_response
    def get_activities(self, activityClass: str = 'ALL', before: str = None, after: str = None,
            olderThan: int = None, newerThan:int = None, type: str = None,
            status: str = None, user: str = None, seriesUid: str = None,
            df: str = None, pageSize: int = 200, lang: str = 'en', tz: str = None) -> requests.Response:
        """List activities
        Returns activity log in reverse chronological order

        Keyword arguments:
        activityClass: str -- Activity Class (System/Device) filter. Valid arguments: ALL, SYSTEM, DEVICE
        before: str        -- Return activities recorded prior to the specified date
        after:  str        -- Return activities recorded after the specified date
        olderThan: int     -- Return activities recorded that are older than specified activity ID
        newerThan: int     -- Return activities recorded that are newer than specified activity ID
        type: str          -- Return activities of type
        status: str        -- Return activities with status(es)
        user: str          -- Return activities for user(s)
        seriesUid: str     -- Return activities related to alert (series)
        df: str            -- Device filter
        pageSize: int      -- Limit number of activities to return
        lang: str          -- Language tag
        tz: str            -- Time Zone
        """
        return self.api_get_request(f'/v2/activities?')
    
    @return_response
    def get_users(self, userType: str = None) -> requests.Response:
        """List users
        Returns list of users

        Returns both technicians and end users by default

        Keyword arguments:
        userType: str -- User type filter, valid strings: TECHNICIAN or END_USER

        TODO: Implement passing query string for userType parameter
        """
        if userType:
            return self.api_get_request(f'/v2/users?userType={userType}')
        return self.api_get_request('/v2/users')

    
    @return_response
    def get_devices(self, df: str = None, pageSize: int = 50, after: int = 0) -> requests.Response:
        """List devices
        Returns list of devices (basic node information)

        Keyword arguments:
        df: str             -- Device filter
        pageSize: int       -- Limit number of devices to return
        after: int          -- Last Node ID from previous page
        """
        return self.api_get_request(f'/v2/users?')
    

    @return_response
    def get_policies(self) -> requests.Response:
        """List policies
        Returns list of policies
        """
        return self.api_get_request(f'/v2/policies')