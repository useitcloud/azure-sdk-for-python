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

from .events_result_data import EventsResultData


class EventsExceptionResult(EventsResultData):
    """An exception result.

    All required parameters must be populated in order to send to Azure.

    :param id: The unique ID for this event.
    :type id: str
    :param count: Count of the event
    :type count: long
    :param timestamp: Timestamp of the event
    :type timestamp: datetime
    :param custom_dimensions: Custom dimensions of the event
    :type custom_dimensions:
     ~azure.applicationinsights.models.EventsResultDataCustomDimensions
    :param custom_measurements: Custom measurements of the event
    :type custom_measurements:
     ~azure.applicationinsights.models.EventsResultDataCustomMeasurements
    :param operation: Operation info of the event
    :type operation: ~azure.applicationinsights.models.EventsOperationInfo
    :param session: Session info of the event
    :type session: ~azure.applicationinsights.models.EventsSessionInfo
    :param user: User info of the event
    :type user: ~azure.applicationinsights.models.EventsUserInfo
    :param cloud: Cloud info of the event
    :type cloud: ~azure.applicationinsights.models.EventsCloudInfo
    :param ai: AI info of the event
    :type ai: ~azure.applicationinsights.models.EventsAiInfo
    :param application: Application info of the event
    :type application: ~azure.applicationinsights.models.EventsApplicationInfo
    :param client: Client info of the event
    :type client: ~azure.applicationinsights.models.EventsClientInfo
    :param type: Required. Constant filled by server.
    :type type: str
    :param exception:
    :type exception: ~azure.applicationinsights.models.EventsExceptionInfo
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'count': {'key': 'count', 'type': 'long'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'custom_dimensions': {'key': 'customDimensions', 'type': 'EventsResultDataCustomDimensions'},
        'custom_measurements': {'key': 'customMeasurements', 'type': 'EventsResultDataCustomMeasurements'},
        'operation': {'key': 'operation', 'type': 'EventsOperationInfo'},
        'session': {'key': 'session', 'type': 'EventsSessionInfo'},
        'user': {'key': 'user', 'type': 'EventsUserInfo'},
        'cloud': {'key': 'cloud', 'type': 'EventsCloudInfo'},
        'ai': {'key': 'ai', 'type': 'EventsAiInfo'},
        'application': {'key': 'application', 'type': 'EventsApplicationInfo'},
        'client': {'key': 'client', 'type': 'EventsClientInfo'},
        'type': {'key': 'type', 'type': 'str'},
        'exception': {'key': 'exception', 'type': 'EventsExceptionInfo'},
    }

    def __init__(self, **kwargs):
        super(EventsExceptionResult, self).__init__(**kwargs)
        self.exception = kwargs.get('exception', None)
        self.type = 'exception'
