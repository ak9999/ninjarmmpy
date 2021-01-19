from .utils import return_response, api_get_request


class DeviceMixin():
    # Devices
    NINJA_API_DEVICE = '/v2/device/'

    api_get_request = api_get_request

    def __init__(self):
        pass

    @return_response
    def getDevice(self, id: int = None):
        """Returns device details
        Keyword arguments:
        id: int       -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}')

    @return_response
    def getDeviceActivities(self, id: int = None, olderThan: int = None, newerThan: int = None,
            activityType: str = None, status: str = None, seriesUid: str = None,
            pageSize: int = None, lang: str = None, tz: str = None):
        """List activities
        Returns activity log in reverse chronological order
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        olderThan: int     -- Return activities recorded that are older than specified activity ID
        newerThan: int     -- Return activities recorded that are newer than specified activity ID
        activityType: str  -- Return activities of type
        status: str        -- Return activities with status(es)
        seriesUid: str     -- Return activities related to alert (series)
        pageSize: int      -- Limit number of activities to return
        lang: str          -- Language tag
        tz: str            -- Time Zone
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'olderThan': olderThan,
            'newerThan': newerThan,
            'activityType': activityType,
            'status': status,
            'seriesUid': seriesUid,
            'pageSize': pageSize,
            'lang': lang,
            'tz': tz
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/activities', params=params)

    @return_response
    def getDeviceDiskDrives(self, id: int = None):
        """Returns device disks' details
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/disks')
    @return_response
    def getDeviceVolumes(self, id: int = None):
        """Returns device volumes' details
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/volumes')

    @return_response
    def getDeviceProcessors(self, id: int = None):
        """Returns list of device Processor details

        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/processors')

    @return_response
    def getDeviceSoftware(self, id: int = None):
        """Returns list of software installed on device
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/software')

    @return_response
    def getDeviceLastLoggedOnUser(self, id: int = None):
        """Returns username that was last to login to device
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/last-logged-on-user')

    @return_response
    def getDeviceAlerts(self, id: int = None, lang: str = None, tz: str = None):
        """Returns list of active alerts (triggered conditions) for device

        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/alerts')

    @return_response
    def getDevicePendingFailedRejectedOSPatches(self, id: int = None, status: str = None, patchType: str = None, severity: str = None):
        """Returns list of pending/rejected/approved OS patches for device
        Keyword arguments:
        id: int            -- Device identifier, required, no default provided.
        status: str        -- Patch status filter
        patchType: str     -- Patch Type filter
        severity: str      -- Patch Severity filter
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'status': status,
            'type': patchType,
            'severity': severity
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/os-patches', params=params)

    @return_response
    def getDeviceInstalledOSPatches(self, id: int = None, status: str = None, installedBefore: str = None, installedAfter: str = None):
        """Returns patch installation history records (successful and failed) for device
        Keyword arguments:
        id: int                  -- Device identifier, required, no default provided.
        status: str              -- Patch Status filter (FAILED, INSTALLED)
        installedBefore: str     -- Include patches installed before specified date
        installedAfter: str      -- Include patches installed after specified date
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'status': status,
            'installedBefore': installedBefore,
            'installedAfter': installedAfter
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/os-patch-installs', params=params)

    @return_response
    def getDevicePendingFailedRejectedSoftwarePatches(self, id: int = None, status: str = None, productIdentifier: str = None,
        patchType: str = None, patchImpact: str = None):
        """Returns list of 3rd party Software patches for a device (for which there were no installation attempts)
        Keyword arguments:
        id: int                  -- Device identifier, required, no default provided.
        status: str              -- Patch Status filter (FAILED, INSTALLED)
        productIdentifier: str   -- Product identifier
        patchType: str           -- Patch Type filter
        patchImpact: str         -- Patch Impact filter
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'status': status,
            'productIdentifier': productIdentifier,
            'type': patchType,
            'impact': patchImpact
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/software-patches', params=params)


    @return_response
    def getDeviceInstalledSoftwarePatches(self, id: int = None, status: str = None, productIdentifier: str = None,
        patchType: str = None, patchImpact: str = None, installedBefore: str = None, installedAfter: str = None):
        """Returns 3rd party software patch installation history records for device (successful and failed)
        Keyword arguments:
        id: int                  -- Device identifier, required, no default provided.
        status: str              -- Patch Status filter (FAILED, INSTALLED)
        productIdentifier: str   -- Product identifier
        patchType: str           -- Patch Type filter
        patchImpact: str         -- Patch Impact filter
        installedBefore: str     -- Include patches installed before specified date
        installedAfter: str      -- Include patches installed after specified date
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'status': status,
            'productIdentifier': productIdentifier,
            'type': patchType,
            'impact': patchImpact,
            'installedBefore': installedBefore,
            'installedAfter': installedAfter
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/software-patch-installs', params=params)

    @return_response
    def getDeviceServices(self, id: int = None, name: str = None, state: str = None,
        patchType: str = None, patchImpact: str = None):
        """Returns list of Windows services and their statuses
        Keyword arguments:
        id: int                  -- Device identifier, required, no default provided.
        name: str                -- Service name
        state: str               -- Service state, Available values : UNKNOWN, STOPPED, START_PENDING, RUNNING, STOP_PENDING, PAUSE_PENDING, PAUSED, CONTINUE_PENDING
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'name': name,
            'state': state
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/windows-services', params=params)

    @return_response
    def getDeviceActiveJobs(self, id: int = None, lang: str = None, tz: str = None):
        """Returns currently running jobs for device
        Keyword arguments:
        id: int                  -- Device identifier, required, no default provided.
        lang: str                -- language code
        tz: str                  -- Time Zone
        """
        if not id:
            raise ValueError('id needs to be set to an organizational identifier.')
        params = {
            'lang': lang,
            'tz': tz
        }
        return self.api_get_request(f'{self.NINJA_API_DEVICE}{id}/jobs', params=params)
