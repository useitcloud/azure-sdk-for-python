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

from .protection_policy_py3 import ProtectionPolicy


class AzureFileShareProtectionPolicy(ProtectionPolicy):
    """AzureStorage backup policy.

    All required parameters must be populated in order to send to Azure.

    :param protected_items_count: Number of items associated with this policy.
    :type protected_items_count: int
    :param backup_management_type: Required. Constant filled by server.
    :type backup_management_type: str
    :param work_load_type: Type of workload for the backup management.
     Possible values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb',
     'SQLDB', 'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type work_load_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.WorkloadType
    :param schedule_policy: Backup schedule specified as part of backup
     policy.
    :type schedule_policy:
     ~azure.mgmt.recoveryservicesbackup.models.SchedulePolicy
    :param retention_policy: Retention policy with the details on backup copy
     retention ranges.
    :type retention_policy:
     ~azure.mgmt.recoveryservicesbackup.models.RetentionPolicy
    :param time_zone: TimeZone optional input as string. For example: TimeZone
     = "Pacific Standard Time".
    :type time_zone: str
    """

    _validation = {
        'backup_management_type': {'required': True},
    }

    _attribute_map = {
        'protected_items_count': {'key': 'protectedItemsCount', 'type': 'int'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'work_load_type': {'key': 'workLoadType', 'type': 'str'},
        'schedule_policy': {'key': 'schedulePolicy', 'type': 'SchedulePolicy'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
    }

    def __init__(self, *, protected_items_count: int=None, work_load_type=None, schedule_policy=None, retention_policy=None, time_zone: str=None, **kwargs) -> None:
        super(AzureFileShareProtectionPolicy, self).__init__(protected_items_count=protected_items_count, **kwargs)
        self.work_load_type = work_load_type
        self.schedule_policy = schedule_policy
        self.retention_policy = retention_policy
        self.time_zone = time_zone
        self.backup_management_type = 'AzureStorage'
