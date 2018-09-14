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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
import uuid
from .operations.subscriptions_operations import SubscriptionsOperations
from .operations.tenants_operations import TenantsOperations
from . import models


class SubscriptionClientConfiguration(AzureConfiguration):
    """Configuration for SubscriptionClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SubscriptionClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-resource/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class SubscriptionClient(SDKClient):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: azure.mgmt.resource.subscriptions.v2016_06_01.operations.SubscriptionsOperations
    :ivar tenants: Tenants operations
    :vartype tenants: azure.mgmt.resource.subscriptions.v2016_06_01.operations.TenantsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        super(SubscriptionClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.subscriptions = SubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tenants = TenantsOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def list_operations(
            self, custom_headers=None, raw=False, **operation_config):
        """Lists all of the available Microsoft.Resources REST API operations.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Operation
        :rtype:
         ~azure.mgmt.resource.subscriptions.v2016_06_01.models.OperationPaged[~azure.mgmt.resource.subscriptions.v2016_06_01.models.Operation]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_operations.metadata['url']

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.OperationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.OperationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_operations.metadata = {'url': '/providers/Microsoft.Resources/operations'}
