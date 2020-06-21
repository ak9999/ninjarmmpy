# from .utils import return_response, api_get_request

# import requests

class ManagementMixin():
    # Management
    NINJA_API_ALERTS                                    = '/v2/alert/'
    NINJA_API_WEBHOOK                                   = '/v2/webhook'

    def __init__(self):
        pass