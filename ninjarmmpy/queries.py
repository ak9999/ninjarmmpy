from .utils import return_response, api_get_request  # noqa, flake8 issue


class QueriesMixin():
    # Queries
    NINJA_API_QUERIES                                   = '/v2/queries'
    NINJA_API_QUERIES_ANTIVIRUS_THREATS                 = NINJA_API_QUERIES + '/antivirus-threats'
    NINJA_API_QUERIES_OPERATING_SYSTEMS                 = NINJA_API_QUERIES + '/operating-systems'
    NINJA_API_QUERIES_PROCESSORS                        = NINJA_API_QUERIES + '/processors'
    NINJA_API_QUERIES_VOLUMES                           = NINJA_API_QUERIES + '/volumes'
    NINJA_API_QUERIES_DISKS                             = NINJA_API_QUERIES + '/disks'
    NINJA_API_QUERIES_COMPUTER_SYSTEMS                  = NINJA_API_QUERIES + '/computer-systems'
    NINJA_API_QUERIES_DEVICE_HEALTH                     = NINJA_API_QUERIES + '/device-health'
    NINJA_API_QUERIES_SOFTWARE                          = NINJA_API_QUERIES + '/software'
    NINJA_API_QUERIES_OS_PATCHES                        = NINJA_API_QUERIES + '/os-patches'
    NINJA_API_QUERIES_OS_PATCH_INSTALLS                 = NINJA_API_QUERIES + '/os-patch-installs'
    NINJA_API_QUERIES_SOFTWARE_PATCHES                  = NINJA_API_QUERIES + '/software-patches'
    NINJA_API_QUERIES_SOFTWARE_PATCH_INSTALLS           = NINJA_API_QUERIES + '/software-patch-installs'
    NINJA_API_QUERIES_RAID_CONTROLLERS                  = NINJA_API_QUERIES + '/raid-controllers'
    NINJA_API_QUERIES_RAID_DRIVES                       = NINJA_API_QUERIES + '/raid-drives'
    NINJA_API_QUERIES_WINDOWS_SERVICES                  = NINJA_API_QUERIES + '/windows-services'
    NINJA_API_QUERIES_LOGGED_ON_USERS                   = NINJA_API_QUERIES + '/logged-on-users'
    NINJA_API_QUERIES_ANTIVIRUS_STATUS                  = NINJA_API_QUERIES + '/antivirus-status'

    def __init__(self):
        pass

    @return_response
    def get_raid_controllers(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of RAID controllers

        Keyword arguments:
        df: str       -- Device filter
        ts: str       -- Monitoring timestamp filter
        cursor: str   -- Cursor name
        pageSize: int -- Limit number of records per page
        """
        params = {
            'df': df,
            'ts': ts,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_RAID_CONTROLLERS}', params=params)

    @return_response
    def get_raid_drives(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of drives connected to RAID controllers

        Keyword arguments:
        df: str       -- Device filter
        ts: str       -- Monitoring timestamp filter
        cursor: str   -- Cursor name
        pageSize: int -- Limit number of records per page
        """
        params = {
            'df': df,
            'ts': ts,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_RAID_DRIVES}', params=params)
