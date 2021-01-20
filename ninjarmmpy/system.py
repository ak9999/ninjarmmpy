from .utils import return_response, api_get_request


class SystemMixin():
    # System Endpoints
    NINJA_API_ORGANIZATIONS                             = '/v2/organizations'
    NINJA_API_ORGANIZATIONS_DETAILED                    = '/v2/organizations-detailed'
    NINJA_API_ATTACHMENT                                = '/v2/attachment/'
    NINJA_API_GROUPS                                    = '/v2/groups'
    NINJA_API_ACTIVITIES                                = '/v2/activities'
    NINJA_API_USERS                                     = '/v2/users'
    NINJA_API_DEVICES                                   = '/v2/devices'
    NINJA_API_POLICIES                                  = '/v2/policies'
    NINJA_API_SOFTWARE_PRODUCTS                         = '/v2/software-products'
    NINJA_API_DEVICES_DETAILED                          = '/v2/devices-detailed'
    NINJA_API_ALERTS                                    = '/v2/alerts'
    NINJA_API_JOBS                                      = '/v2/jobs'
    NINJA_API_TASKS                                     = '/v2/tasks'
    NINJA_API_LOCATIONS                                 = '/v2/locations'
    NINJA_API_ROLES                                     = '/v2/roles'

    api_get_request = api_get_request

    def __init__(self):
        pass

    # Core system Entities and Resources
    @return_response
    def getOrganizations(self, pageSize: int = None, after: int = None):
        """Returns list of organizations (Brief mode)

        Keyword arguments:
        pageSize -- Limit number of organizations to return
        after    -- Last organization Identifier from previous page
        """
        params = {'pageSize': pageSize, 'after': after}
        return self.api_get_request(self.NINJA_API_ORGANIZATIONS, params=params)


    @return_response
    def getAttachment(self, id: str):
        """Returns attachment (image, document)

        Keyword arguments:
        id -- Attachment identifier
        """
        return self.api_get_request(f'{self.NINJA_API_ATTACHMENT}{id}')

    @return_response
    def getDevices(self, df: str = None, pageSize: int = None, after: int = None):
        """List devices
        Returns list of devices (basic node information)

        Keyword arguments:
        df: str             -- Device filter
        pageSize: int       -- Limit number of devices to return
        after: int          -- Last Node ID from previous page
        """
        params = {
            'df': df,
            'pageSize': pageSize,
            'after': after
        }
        return self.api_get_request(self.NINJA_API_DEVICES, params=params)

    @return_response
    def getActivities(self, activityClass: str = 'ALL', before: str = None, after: str = None,
            olderThan: int = None, newerThan: int = None, activityType: str = None,
            status: str = None, user: str = None, seriesUid: str = None,
            df: str = None, pageSize: int = 200, lang: str = 'en', tz: str = None):
        """List activities
        Returns activity log in reverse chronological order

        Keyword arguments:
        activityClass: str -- Activity Class (System/Device) filter. Valid arguments: ALL, SYSTEM, DEVICE
        before: str        -- Return activities recorded prior to the specified date
        after:  str        -- Return activities recorded after the specified date
        olderThan: int     -- Return activities recorded that are older than specified activity ID
        newerThan: int     -- Return activities recorded that are newer than specified activity ID
        activityType: str  -- Return activities of type
        status: str        -- Return activities with status(es)
        user: str          -- Return activities for user(s)
        seriesUid: str     -- Return activities related to alert (series)
        df: str            -- Device filter
        pageSize: int      -- Limit number of activities to return
        lang: str          -- Language tag
        tz: str            -- Time Zone
        """
        params = {
            'activityClass': activityClass,
            'before': before,
            'after': after,
            'olderThan': olderThan,
            'newerThan': newerThan,
            'type': activityType,
            'status': status,
            'user': user,
            'seriesUid': seriesUid,
            'df': df,
            'pageSize': pageSize,
            'lang': lang,
            'tz': tz
        }
        return self.api_get_request(f'{self.NINJA_API_ACTIVITIES}', params=params)

    @return_response
    def getLocations(self, pageSize: int = None, after: int = None):
        """Returns a list of all locations for all organizations
        Keyword arguments:
        pageSize: int       -- Limit number of organizations to return
        after: int          -- Last Organization Identifier from previous page
        """
        params = {
            'pageSize': pageSize,
            'after': after
        }
        return self.api_get_request(self.NINJA_API_LOCATIONS, params=params)

    @return_response
    def getOrganizationsDetailed(self, pageSize: int = None, after: int = None):
        """Returns a list of organizations with locations and policy mappings
        Keyword arguments:
        pageSize: int       -- Limit number of organizations to return
        after: int          -- Last Organization Identifier from previous page
        """
        params = {
            'pageSize': pageSize,
            'after': after
        }
        return self.api_get_request(self.NINJA_API_ORGANIZATIONS_DETAILED, params=params)

    @return_response
    def getNodeRoles(self):
        """Returns a list of device roles"""
        return self.api_get_request(self.NINJA_API_ROLES)

    @return_response
    def getPolicies(self):
        """Returns list of policies"""
        return self.api_get_request(self.NINJA_API_POLICIES)

    @return_response
    def getSoftwareProducts(self):
        """Returns available software products (3rd party patching)"""
        return self.api_get_request(self.NINJA_API_SOFTWARE_PRODUCTS)

    @return_response
    def getDevicesDetailed(self, df: str = None, pageSize: int = None, after: int = None):
        """Returns list of devices with additional information
        Keyword arguments:
        df: string           -- string with the Device Filter syntax
        pageSize: int        -- Limit number of devices to return
        after: int           -- Last device identifier from previous page
        """
        params = {
            'df': df,
            'pageSize': pageSize,
            'after': after
        }
        return self.api_get_request(self.NINJA_API_DEVICES_DETAILED, params=params)

    @return_response
    def getAlerts(self, sourceType: str = None, df: str = None, lang: str = None, tz: str = None):
        """Returns list of active alerts/triggered conditions
        sourceType: str      -- Source of the alert/triggered condition
        df: str              -- string with the Device Filter syntax
        lang: str            -- Language tag
        tz: str              -- Time Zone
        """
        params = {
            'sourceType': sourceType,
            'df': df,
            'lang': lang,
            'tz': tz
        }
        return self.api_get_request(self.NINJA_API_ALERTS, params=params)

    @return_response
    def getActiveJobs(self, jobType: str = None, df: str = None, lang: str = None, tz: str = None):
        """Returns a list of running jobs
        Keyword arguments:
        jobType: str        -- Job Type filter
        df: str             -- Device filter
        lang: str           -- Language tag
        tz: str             -- Time Zone
        """
        params = {
            'jobType': jobType,
            'df': df,
            'lang': lang,
            'tz': tz
        }
        return self.api_get_request(self.NINJA_API_JOBS, params=params)

    @return_response
    def getScheduledTasks(self):
        """Returns a list of registered scheduled tasks"""
        return self.api_get_request(self.NINJA_API_TASKS)

    @return_response
    def getUsers(self, userType: str = None):
        """List users
        Returns list of users

        Returns both technicians and end users by default

        Keyword arguments:
        userType: str -- User type filter, valid strings: TECHNICIAN or END_USER
        """
        params = {'userType': userType}
        return self.api_get_request(self.NINJA_API_USERS, params=params)

    @return_response
    def getGroups(self, lang: str = None):
        """List groups (saved searches)
        Returns list of groups

        Keyword arguments:
        lang: str -- Description
        """
        params = {'lang': lang}
        return self.api_get_request(f'{self.NINJA_API_GROUPS}', params=params)
