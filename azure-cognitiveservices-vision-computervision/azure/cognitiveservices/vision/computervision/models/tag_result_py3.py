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


class TagResult(Model):
    """The results of a image tag operation, including any tags and image
    metadata.

    :param tags: A list of tags with confidence level.
    :type tags:
     list[~azure.cognitiveservices.vision.computervision.models.ImageTag]
    :param request_id: Id of the REST API request.
    :type request_id: str
    :param metadata:
    :type metadata:
     ~azure.cognitiveservices.vision.computervision.models.ImageMetadata
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '[ImageTag]'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'ImageMetadata'},
    }

    def __init__(self, *, tags=None, request_id: str=None, metadata=None, **kwargs) -> None:
        super(TagResult, self).__init__(**kwargs)
        self.tags = tags
        self.request_id = request_id
        self.metadata = metadata
