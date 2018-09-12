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

from .search_results_answer_py3 import SearchResultsAnswer


class Suggestions(SearchResultsAnswer):
    """Suggestions.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar potential_action:
    :vartype potential_action:
     list[~azure.cognitiveservices.search.autosuggest.models.Action]
    :ivar immediate_action:
    :vartype immediate_action:
     list[~azure.cognitiveservices.search.autosuggest.models.Action]
    :ivar preferred_clickthrough_url:
    :vartype preferred_clickthrough_url: str
    :ivar adaptive_card:
    :vartype adaptive_card: str
    :ivar query_context:
    :vartype query_context:
     ~azure.cognitiveservices.search.autosuggest.models.QueryContext
    :param suggestion_groups: Required.
    :type suggestion_groups:
     list[~azure.cognitiveservices.search.autosuggest.models.SuggestionsSuggestionGroup]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'potential_action': {'readonly': True},
        'immediate_action': {'readonly': True},
        'preferred_clickthrough_url': {'readonly': True},
        'adaptive_card': {'readonly': True},
        'query_context': {'readonly': True},
        'suggestion_groups': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'potential_action': {'key': 'potentialAction', 'type': '[Action]'},
        'immediate_action': {'key': 'immediateAction', 'type': '[Action]'},
        'preferred_clickthrough_url': {'key': 'preferredClickthroughUrl', 'type': 'str'},
        'adaptive_card': {'key': 'adaptiveCard', 'type': 'str'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'suggestion_groups': {'key': 'suggestionGroups', 'type': '[SuggestionsSuggestionGroup]'},
    }

    def __init__(self, *, suggestion_groups, **kwargs) -> None:
        super(Suggestions, self).__init__(**kwargs)
        self.suggestion_groups = suggestion_groups
        self._type = 'Suggestions'
