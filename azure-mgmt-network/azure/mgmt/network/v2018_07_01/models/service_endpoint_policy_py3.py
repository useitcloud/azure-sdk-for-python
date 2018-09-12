# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class ServiceEndpointPolicy(Resource):
    """Service End point policy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param service_endpoint_policy_definitions: A collection of service
     endpoint policy definitions of the service endpoint policy.
    :type service_endpoint_policy_definitions:
     list[~azure.mgmt.network.v2018_07_01.models.ServiceEndpointPolicyDefinition]
    :param resource_guid: The resource GUID property of the service endpoint
     policy resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the service endpoint
     policy. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'service_endpoint_policy_definitions': {'key': 'properties.serviceEndpointPolicyDefinitions', 'type': '[ServiceEndpointPolicyDefinition]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, service_endpoint_policy_definitions=None, resource_guid: str=None, provisioning_state: str=None, etag: str=None, **kwargs) -> None:
        super(ServiceEndpointPolicy, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.service_endpoint_policy_definitions = service_endpoint_policy_definitions
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
