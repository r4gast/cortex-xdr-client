import json
from typing import Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.filters import new_request_data

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.exceptions import InvalidResponseException
from cortex_xdr_client.api.models.filters import (new_request_data, request_gte_lte_filter, request_in_contains_filter)

import requests


class IocAPI(BaseAPI):

    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(IocAPI, self).__init__(auth, fqdn, "indicators", timeout)


    def insert_csv(self):
        print('test')
        payload = {"request_data":'indicator,type,severity,expiration_date,comment,reputation,reliability,class,vendor.name,vendor.reputation,vendor.reliability\nd,HASH,LOW,1587054895000,This is an example IOC,BAD,D,Malware,IBM,GOOD,B\n'}

        print(json.dumps(payload))

        response = self._call(call_name="insert_csv", json_value=payload)
        print(response.json())



