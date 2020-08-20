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
    def delete_alert(self, uid: str = None):
        """Resets alert/condition by UID

        Keyword arguments:
        uid: str -- unique identifier of alert
        """
        if not uid:
            raise ValueError('uid needs to be set to an alert/condition identifier.')
        return self.api_delete_request(f'{self.NINJA_API_ALERTS}{uid}')

    @return_response
    def device_approval(self, mode: str = None):
        """Approve or reject devices that are waiting for approval

        Keyword arguments:
        mode: str -- Available values: APPROVE, REJECT
        curl command:
        curl -X POST "https://app.ninjarmm.com/v2/devices/approval/APPROVE" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"devices\":[0]}"
        """
        pass
        # if mode not in {'APPROVE', 'REJECT'}:
        #     raise ValueError('mode needs to be set to either APPROVE or REJECT')
        # return self.api_post_request(f'/v2/devices/approval/{mode}')

    @return_response
    def create_organization(self, templateOrganizationId: int = None):
        """Creates a new organization with optional list of locations and policy mappings.
        Template organzation ID can be specified to copy various settings.

        Keyword arguments:
        templateOrganizationId: int -- template organization to copy settings from.
        curl command:
        curl -X POST "https://app.ninjarmm.com/v2/organizations" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"string\",\"description\":\"string\",\"userData\":{\"additionalProp1\":{}},\"nodeApprovalMode\":\"AUTOMATIC\",\"tags\":[\"string\"],\"fields\":{\"additionalProp1\":{},\"additionalProp2\":{},\"additionalProp3\":{}},\"locations\":[{\"name\":\"string\",\"address\":\"string\",\"description\":\"string\",\"userData\":{\"additionalProp1\":{}},\"tags\":[\"string\"],\"fields\":{\"additionalProp1\":{},\"additionalProp2\":{},\"additionalProp3\":{}}}],\"policies\":[{\"nodeRoleId\":0,\"policyId\":0}]}"
        """
        pass
