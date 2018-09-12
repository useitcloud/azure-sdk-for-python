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

from msrest.serialization import Model


class UpdateTrustedIdProviderWithAccountParameters(Model):
    """The parameters used to update a trusted identity provider while updating a
    Data Lake Store account.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The unique name of the trusted identity provider to
     update.
    :type name: str
    :param id_provider: The URL of this trusted identity provider.
    :type id_provider: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id_provider': {'key': 'properties.idProvider', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpdateTrustedIdProviderWithAccountParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.id_provider = kwargs.get('id_provider', None)
