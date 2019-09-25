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


class Cluster(object):
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
        'total_cpus': 'int',
        'total_memory': 'int',
        'num_cpu_cores': 'int',
        'vendor_id': 'str',
        'num_hosts': 'int',
        'num_datastores': 'int',
        'nsx_manager': 'Reference',
        'vcenter_manager': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'total_cpus': 'total_cpus',
        'total_memory': 'total_memory',
        'num_cpu_cores': 'num_cpu_cores',
        'vendor_id': 'vendor_id',
        'num_hosts': 'num_hosts',
        'num_datastores': 'num_datastores',
        'nsx_manager': 'nsx_manager',
        'vcenter_manager': 'vcenter_manager'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, total_cpus=None, total_memory=None, num_cpu_cores=None, vendor_id=None, num_hosts=None, num_datastores=None, nsx_manager=None, vcenter_manager=None):
        """
        Cluster - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._total_cpus = None
        self._total_memory = None
        self._num_cpu_cores = None
        self._vendor_id = None
        self._num_hosts = None
        self._num_datastores = None
        self._nsx_manager = None
        self._vcenter_manager = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if total_cpus is not None:
          self.total_cpus = total_cpus
        if total_memory is not None:
          self.total_memory = total_memory
        if num_cpu_cores is not None:
          self.num_cpu_cores = num_cpu_cores
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if num_hosts is not None:
          self.num_hosts = num_hosts
        if num_datastores is not None:
          self.num_datastores = num_datastores
        if nsx_manager is not None:
          self.nsx_manager = nsx_manager
        if vcenter_manager is not None:
          self.vcenter_manager = vcenter_manager

    @property
    def entity_id(self):
        """
        Gets the entity_id of this Cluster.

        :return: The entity_id of this Cluster.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this Cluster.

        :param entity_id: The entity_id of this Cluster.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this Cluster.

        :return: The name of this Cluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Cluster.

        :param name: The name of this Cluster.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Cluster.

        :return: The entity_type of this Cluster.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Cluster.

        :param entity_type: The entity_type of this Cluster.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def total_cpus(self):
        """
        Gets the total_cpus of this Cluster.

        :return: The total_cpus of this Cluster.
        :rtype: int
        """
        return self._total_cpus

    @total_cpus.setter
    def total_cpus(self, total_cpus):
        """
        Sets the total_cpus of this Cluster.

        :param total_cpus: The total_cpus of this Cluster.
        :type: int
        """

        self._total_cpus = total_cpus

    @property
    def total_memory(self):
        """
        Gets the total_memory of this Cluster.

        :return: The total_memory of this Cluster.
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """
        Sets the total_memory of this Cluster.

        :param total_memory: The total_memory of this Cluster.
        :type: int
        """

        self._total_memory = total_memory

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this Cluster.

        :return: The num_cpu_cores of this Cluster.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this Cluster.

        :param num_cpu_cores: The num_cpu_cores of this Cluster.
        :type: int
        """

        self._num_cpu_cores = num_cpu_cores

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this Cluster.

        :return: The vendor_id of this Cluster.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this Cluster.

        :param vendor_id: The vendor_id of this Cluster.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def num_hosts(self):
        """
        Gets the num_hosts of this Cluster.

        :return: The num_hosts of this Cluster.
        :rtype: int
        """
        return self._num_hosts

    @num_hosts.setter
    def num_hosts(self, num_hosts):
        """
        Sets the num_hosts of this Cluster.

        :param num_hosts: The num_hosts of this Cluster.
        :type: int
        """

        self._num_hosts = num_hosts

    @property
    def num_datastores(self):
        """
        Gets the num_datastores of this Cluster.

        :return: The num_datastores of this Cluster.
        :rtype: int
        """
        return self._num_datastores

    @num_datastores.setter
    def num_datastores(self, num_datastores):
        """
        Sets the num_datastores of this Cluster.

        :param num_datastores: The num_datastores of this Cluster.
        :type: int
        """

        self._num_datastores = num_datastores

    @property
    def nsx_manager(self):
        """
        Gets the nsx_manager of this Cluster.

        :return: The nsx_manager of this Cluster.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """
        Sets the nsx_manager of this Cluster.

        :param nsx_manager: The nsx_manager of this Cluster.
        :type: Reference
        """

        self._nsx_manager = nsx_manager

    @property
    def vcenter_manager(self):
        """
        Gets the vcenter_manager of this Cluster.

        :return: The vcenter_manager of this Cluster.
        :rtype: Reference
        """
        return self._vcenter_manager

    @vcenter_manager.setter
    def vcenter_manager(self, vcenter_manager):
        """
        Sets the vcenter_manager of this Cluster.

        :param vcenter_manager: The vcenter_manager of this Cluster.
        :type: Reference
        """

        self._vcenter_manager = vcenter_manager

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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
