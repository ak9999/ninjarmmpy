from .utils import (
    return_response,
    api_get_request,
    api_post_request,
    api_put_request,
    api_patch_request,
    api_delete_request
)


class ManagementMixin():
    # Management
    NINJA_API_ALERTS = '/v2/alert/'
    NINJA_API_WEBHOOK = '/v2/webhook'

    def __init__(self):
        pass

    @return_response
    def resetAlert(self, uid: str = None):
        """Resets alert/condition by UID
        Keyword arguments:
        uid: str -- unique identifier of alert
        """
        if not uid:
            raise ValueError('uid needs to be set to an alert/condition identifier.')
        return self.api_delete_request(f'{self.NINJA_API_ALERTS}{uid}')

    @return_response
    def nodeApprovalOperation(self, mode: str = None, devices: list = None):
        """Approve or reject devices that are waiting for approval
        Keyword arguments:
        mode: str       -- Available values: APPROVE, REJECT
        devices: list   -- List of device identifiers (integers)
        curl command:
        curl -X POST "https://app.ninjarmm.com/v2/devices/approval/APPROVE" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"devices\":[deviceId]}"
        """
        if mode not in {'APPROVE', 'REJECT'}:
            raise ValueError('mode needs to be set to either APPROVE or REJECT')
        if not devices:
            raise ValueError('devices needs to be a non-empty list of device identifiers of type `int`')
        params = {'devices': devices}
        return self.api_post_request(f'/v2/devices/approval/{mode}', params=params)
