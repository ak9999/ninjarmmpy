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
    def get_antivirus_threats(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of antivirus threats

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_ANTIVIRUS_THREATS}', params=params)

    @return_response
    def get_operating_systems(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns operating systems for devices

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_OPERATING_SYSTEMS}', params=params)

    @return_response
    def get_processors(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of processors

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_PROCESSORS}', params=params)

    @return_response
    def get_volumes(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of disk volumes

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_VOLUMES}', params=params)

    @return_response
    def get_disks(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of physical disks

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_DISKS}', params=params)

    @return_response
    def get_computer_systems(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns computer systems information for devices

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_COMPUTER_SYSTEMS}', params=params)

    @return_response
    def get_device_health(self, df: str = None, ts: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of device health summary reports

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
        return self.api_get_request(f'{self.NINJA_API_QUERIES_DEVICE_HEALTH}', params=params)

    @return_response
    def get_software_list(self, df: str = None, cursor: str = None, pageSize: int = None, installedBefore: str = None, installedAfter: str = None):
        """Returns list of software installed on devices

        Keyword arguments:
        df: str              -- Device filter
        cursor: str          -- Cursor name
        pageSize: int        -- Limit number of records per page
        installedBefore: str -- Include software installed before specified date
        installedAfter: str  -- Include software installed after specified date
        """
        params = {
            'df': df,
            'cursor': cursor,
            'pageSize': pageSize,
            'installedBefore': installedBefore,
            'installedAfter': installedAfter
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_SOFTWARE}', params=params)

    @return_response
    def get_os_patches(self, df: str = None, ts: str = None, status: str = None, 
        patch_type: str = None, severity: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of OS patches for which there were no installation attempts

        Keyword arguments:
        df: str              -- Device filter
        ts: str              -- Monitoring timestamp filter
        status: str          -- Patch Status filter
        type: str            -- Patch Type filter
        severity: str        -- Patch Severity filter
        cursor: str          -- Cursor name
        pageSize: int        -- Limit number of records per page
        """
        params = {
            'df': df,
            'ts': ts,
            'status': status,
            'type': patch_type,
            'severity': severity,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_OS_PATCHES}', params=params)

    @return_response
    def get_os_patch_installs(self, df: str = None, status: str = None, cursor: str = None, pageSize: int = None, installedBefore: str = None, installedAfter: str = None):
        """Returns pach installation history records, successful and failed

        Keyword arguments:
        df: str              -- Device filter
        status: str          -- Patch Status filter (FAILED, INSTALLED)
        cursor: str          -- Cursor name
        pageSize: int        -- Limit number of records per page
        installedBefore: str -- Include software installed before specified date
        installedAfter: str  -- Include software installed after specified date
        """
        params = {
            'df': df,
            'cursor': cursor,
            'pageSize': pageSize,
            'installedBefore': installedBefore,
            'installedAfter': installedAfter
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_OS_PATCH_INSTALLS}', params=params)

    @return_response
    def get_software_patches(self, df: str = None, ts: str = None, status: str = None,
                             productIdentifier: str = None, patch_type: str = None, impact: str = None,
                             cursor: str = None, pageSize: int = None):
        """Returns list of OS patches for which there were no installation attempts

        Keyword arguments:
        df: str                         -- Device filter
        ts: str                         -- Monitoring timestamp filter
        status: str                     -- Patch Status filter
        productIdentifier: str          -- Product identifier
        patch_type: str                 -- Patch Type filter
        impact: str                     -- Patch Impact filter
        cursor: str                     -- Cursor name
        pageSize: int                   -- Limit number of records per page
        """
        params = {
            'df': df,
            'ts': ts,
            'status': status,
            'type': patch_type,
            'productIdentifier': productIdentifier,
            'impact': impact,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_SOFTWARE_PATCHES}', params=params)

    @return_response
    def get_software_patch_installs(self, df: str = None, ts: str = None, status: str = None,
                                    productIdentifier: str = None, patch_type: str = None, impact: str = None,
                                    cursor: str = None, pageSize: int = None,
                                    installedBefore: str = None, installedAfter: str = None):
        """Returns 3rd party software patch installation history records (successful and failed)

        Keyword arguments:
        df: str                         -- Device filter
        ts: str                         -- Monitoring timestamp filter
        status: str                     -- Patch Status filter
        productIdentifier: str          -- Product identifier
        patch_type: str                 -- Patch Type filter
        impact: str                     -- Patch Impact filter
        cursor: str                     -- Cursor name
        pageSize: int                   -- Limit number of records per page
        installedBefore: str            -- Include patches installed before specified date
        installedAfter: str             -- Include patches installed after specified date
        """
        params = {
            'df': df,
            'ts': ts,
            'status': status,
            'type': patch_type,
            'productIdentifier': productIdentifier,
            'impact': impact,
            'cursor': cursor,
            'pageSize': pageSize,
            'installedBefore': installedBefore,
            'installedAfter': installedAfter
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_SOFTWARE_PATCH_INSTALLS}', params=params)

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

    @return_response
    def get_windows_services(self, df: str = None, name: str = None, state: str = None, cursor: str = None, pageSize: int = None):
        """Returns list of Windows Services and their statuses

        Keyword arguments:
        df: str         -- Device filter
        name: str       -- Service name
        state: str      -- Service state, available values: UNKNOWN, STOPPED, START_PENDING, RUNNING, STOP_PENDING, PAUSE_PENDING, PAUSED, CONTINUE_PENDING
        cursor: str     -- Cursor name
        pageSize: int   -- Limit number of records per page
        """
        params = {
            'df': df,
            'name': name,
            'state': state,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_WINDOWS_SERVICES}', params=params)

    @return_response
    def get_logged_on_users(self, df: str = None, cursor: str = None, pageSize: int = 1000):
        """Returns usernames and logon times

        Keyword arguments:
        df: str         -- Device filter
        cursor: str     -- Cursor name
        pageSize: int   -- Limit number of records per page, default value: 1000
        """
        params = {
            'df': df,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_LOGGED_ON_USERS}', params=params)

    @return_response
    def get_antivirus_status(self, df: str = None, ts: str = None, productState: str = None,
                             productName: str = None, cursor: str = None, pageSize: int = None):
        """Returns usernames and logon times

        Keyword arguments:
        df: str                 -- Device filter
        ts: str                 -- Monitoring timestamp filter
        productState: str       -- Product State filter
        productName: str        -- Product Name filter
        cursor: str             -- Cursor name
        pageSize: int           -- Limit number of records per page, default value: 1000
        """
        params = {
            'df': df,
            'ts': ts,
            'productState': productState,
            'productName': productName,
            'cursor': cursor,
            'pageSize': pageSize
        }
        return self.api_get_request(f'{self.NINJA_API_QUERIES_ANTIVIRUS_STATUS}', params=params)
