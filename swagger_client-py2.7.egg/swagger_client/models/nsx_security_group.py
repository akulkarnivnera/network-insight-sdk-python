# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXSecurityGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_id': 'str',
        'name': 'str',
        'entity_type': 'EntityType',
        'members': 'list[Reference]',
        'direct_source_rules': 'list[RuleSet]',
        'direct_destination_rules': 'list[RuleSet]',
        'indirect_source_rules': 'list[RuleSet]',
        'indirect_destination_rules': 'list[RuleSet]',
        'parents': 'list[Reference]',
        'direct_members': 'list[Reference]',
        'vendor_id': 'str',
        'excluded_members': 'list[Reference]',
        'nsx_managers': 'list[Reference]',
        'scope': 'ScopeEnum',
        'ip_sets': 'list[Reference]',
        'security_tags': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'members': 'members',
        'direct_source_rules': 'direct_source_rules',
        'direct_destination_rules': 'direct_destination_rules',
        'indirect_source_rules': 'indirect_source_rules',
        'indirect_destination_rules': 'indirect_destination_rules',
        'parents': 'parents',
        'direct_members': 'direct_members',
        'vendor_id': 'vendor_id',
        'excluded_members': 'excluded_members',
        'nsx_managers': 'nsx_managers',
        'scope': 'scope',
        'ip_sets': 'ip_sets',
        'security_tags': 'security_tags'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, members=None, direct_source_rules=None, direct_destination_rules=None, indirect_source_rules=None, indirect_destination_rules=None, parents=None, direct_members=None, vendor_id=None, excluded_members=None, nsx_managers=None, scope=None, ip_sets=None, security_tags=None):
        """
        NSXSecurityGroup - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._members = None
        self._direct_source_rules = None
        self._direct_destination_rules = None
        self._indirect_source_rules = None
        self._indirect_destination_rules = None
        self._parents = None
        self._direct_members = None
        self._vendor_id = None
        self._excluded_members = None
        self._nsx_managers = None
        self._scope = None
        self._ip_sets = None
        self._security_tags = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if members is not None:
          self.members = members
        if direct_source_rules is not None:
          self.direct_source_rules = direct_source_rules
        if direct_destination_rules is not None:
          self.direct_destination_rules = direct_destination_rules
        if indirect_source_rules is not None:
          self.indirect_source_rules = indirect_source_rules
        if indirect_destination_rules is not None:
          self.indirect_destination_rules = indirect_destination_rules
        if parents is not None:
          self.parents = parents
        if direct_members is not None:
          self.direct_members = direct_members
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if excluded_members is not None:
          self.excluded_members = excluded_members
        if nsx_managers is not None:
          self.nsx_managers = nsx_managers
        if scope is not None:
          self.scope = scope
        if ip_sets is not None:
          self.ip_sets = ip_sets
        if security_tags is not None:
          self.security_tags = security_tags

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXSecurityGroup.

        :return: The entity_id of this NSXSecurityGroup.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXSecurityGroup.

        :param entity_id: The entity_id of this NSXSecurityGroup.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXSecurityGroup.

        :return: The name of this NSXSecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXSecurityGroup.

        :param name: The name of this NSXSecurityGroup.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXSecurityGroup.

        :return: The entity_type of this NSXSecurityGroup.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXSecurityGroup.

        :param entity_type: The entity_type of this NSXSecurityGroup.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def members(self):
        """
        Gets the members of this NSXSecurityGroup.

        :return: The members of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this NSXSecurityGroup.

        :param members: The members of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._members = members

    @property
    def direct_source_rules(self):
        """
        Gets the direct_source_rules of this NSXSecurityGroup.

        :return: The direct_source_rules of this NSXSecurityGroup.
        :rtype: list[RuleSet]
        """
        return self._direct_source_rules

    @direct_source_rules.setter
    def direct_source_rules(self, direct_source_rules):
        """
        Sets the direct_source_rules of this NSXSecurityGroup.

        :param direct_source_rules: The direct_source_rules of this NSXSecurityGroup.
        :type: list[RuleSet]
        """

        self._direct_source_rules = direct_source_rules

    @property
    def direct_destination_rules(self):
        """
        Gets the direct_destination_rules of this NSXSecurityGroup.

        :return: The direct_destination_rules of this NSXSecurityGroup.
        :rtype: list[RuleSet]
        """
        return self._direct_destination_rules

    @direct_destination_rules.setter
    def direct_destination_rules(self, direct_destination_rules):
        """
        Sets the direct_destination_rules of this NSXSecurityGroup.

        :param direct_destination_rules: The direct_destination_rules of this NSXSecurityGroup.
        :type: list[RuleSet]
        """

        self._direct_destination_rules = direct_destination_rules

    @property
    def indirect_source_rules(self):
        """
        Gets the indirect_source_rules of this NSXSecurityGroup.

        :return: The indirect_source_rules of this NSXSecurityGroup.
        :rtype: list[RuleSet]
        """
        return self._indirect_source_rules

    @indirect_source_rules.setter
    def indirect_source_rules(self, indirect_source_rules):
        """
        Sets the indirect_source_rules of this NSXSecurityGroup.

        :param indirect_source_rules: The indirect_source_rules of this NSXSecurityGroup.
        :type: list[RuleSet]
        """

        self._indirect_source_rules = indirect_source_rules

    @property
    def indirect_destination_rules(self):
        """
        Gets the indirect_destination_rules of this NSXSecurityGroup.

        :return: The indirect_destination_rules of this NSXSecurityGroup.
        :rtype: list[RuleSet]
        """
        return self._indirect_destination_rules

    @indirect_destination_rules.setter
    def indirect_destination_rules(self, indirect_destination_rules):
        """
        Sets the indirect_destination_rules of this NSXSecurityGroup.

        :param indirect_destination_rules: The indirect_destination_rules of this NSXSecurityGroup.
        :type: list[RuleSet]
        """

        self._indirect_destination_rules = indirect_destination_rules

    @property
    def parents(self):
        """
        Gets the parents of this NSXSecurityGroup.

        :return: The parents of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this NSXSecurityGroup.

        :param parents: The parents of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._parents = parents

    @property
    def direct_members(self):
        """
        Gets the direct_members of this NSXSecurityGroup.

        :return: The direct_members of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._direct_members

    @direct_members.setter
    def direct_members(self, direct_members):
        """
        Sets the direct_members of this NSXSecurityGroup.

        :param direct_members: The direct_members of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._direct_members = direct_members

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this NSXSecurityGroup.

        :return: The vendor_id of this NSXSecurityGroup.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this NSXSecurityGroup.

        :param vendor_id: The vendor_id of this NSXSecurityGroup.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def excluded_members(self):
        """
        Gets the excluded_members of this NSXSecurityGroup.

        :return: The excluded_members of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._excluded_members

    @excluded_members.setter
    def excluded_members(self, excluded_members):
        """
        Sets the excluded_members of this NSXSecurityGroup.

        :param excluded_members: The excluded_members of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._excluded_members = excluded_members

    @property
    def nsx_managers(self):
        """
        Gets the nsx_managers of this NSXSecurityGroup.

        :return: The nsx_managers of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._nsx_managers

    @nsx_managers.setter
    def nsx_managers(self, nsx_managers):
        """
        Sets the nsx_managers of this NSXSecurityGroup.

        :param nsx_managers: The nsx_managers of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._nsx_managers = nsx_managers

    @property
    def scope(self):
        """
        Gets the scope of this NSXSecurityGroup.

        :return: The scope of this NSXSecurityGroup.
        :rtype: ScopeEnum
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this NSXSecurityGroup.

        :param scope: The scope of this NSXSecurityGroup.
        :type: ScopeEnum
        """

        self._scope = scope

    @property
    def ip_sets(self):
        """
        Gets the ip_sets of this NSXSecurityGroup.

        :return: The ip_sets of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._ip_sets

    @ip_sets.setter
    def ip_sets(self, ip_sets):
        """
        Sets the ip_sets of this NSXSecurityGroup.

        :param ip_sets: The ip_sets of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._ip_sets = ip_sets

    @property
    def security_tags(self):
        """
        Gets the security_tags of this NSXSecurityGroup.

        :return: The security_tags of this NSXSecurityGroup.
        :rtype: list[Reference]
        """
        return self._security_tags

    @security_tags.setter
    def security_tags(self, security_tags):
        """
        Sets the security_tags of this NSXSecurityGroup.

        :param security_tags: The security_tags of this NSXSecurityGroup.
        :type: list[Reference]
        """

        self._security_tags = security_tags

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NSXSecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
