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


class RouteErrorPosition(Model):
    """Position where the route error happened.

    :param line: Line where the route error happened
    :type line: int
    :param column: Column where the route error happened
    :type column: int
    """

    _attribute_map = {
        'line': {'key': 'line', 'type': 'int'},
        'column': {'key': 'column', 'type': 'int'},
    }

    def __init__(self, *, line: int=None, column: int=None, **kwargs) -> None:
        super(RouteErrorPosition, self).__init__(**kwargs)
        self.line = line
        self.column = column
