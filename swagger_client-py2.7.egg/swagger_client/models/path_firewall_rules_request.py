# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PathFirewallRulesRequest(object):
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
        'source_ip_address': 'str',
        'destination_ip_address': 'str',
        'port': 'int',
        'protocol': 'str',
        'time': 'int'
    }

    attribute_map = {
        'source_ip_address': 'source_ip_address',
        'destination_ip_address': 'destination_ip_address',
        'port': 'port',
        'protocol': 'protocol',
        'time': 'time'
    }

    def __init__(self, source_ip_address=None, destination_ip_address=None, port=None, protocol=None, time=None):
        """
        PathFirewallRulesRequest - a model defined in Swagger
        """

        self._source_ip_address = None
        self._destination_ip_address = None
        self._port = None
        self._protocol = None
        self._time = None

        if source_ip_address is not None:
          self.source_ip_address = source_ip_address
        if destination_ip_address is not None:
          self.destination_ip_address = destination_ip_address
        if port is not None:
          self.port = port
        if protocol is not None:
          self.protocol = protocol
        if time is not None:
          self.time = time

    @property
    def source_ip_address(self):
        """
        Gets the source_ip_address of this PathFirewallRulesRequest.

        :return: The source_ip_address of this PathFirewallRulesRequest.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """
        Sets the source_ip_address of this PathFirewallRulesRequest.

        :param source_ip_address: The source_ip_address of this PathFirewallRulesRequest.
        :type: str
        """

        self._source_ip_address = source_ip_address

    @property
    def destination_ip_address(self):
        """
        Gets the destination_ip_address of this PathFirewallRulesRequest.

        :return: The destination_ip_address of this PathFirewallRulesRequest.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """
        Sets the destination_ip_address of this PathFirewallRulesRequest.

        :param destination_ip_address: The destination_ip_address of this PathFirewallRulesRequest.
        :type: str
        """

        self._destination_ip_address = destination_ip_address

    @property
    def port(self):
        """
        Gets the port of this PathFirewallRulesRequest.

        :return: The port of this PathFirewallRulesRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this PathFirewallRulesRequest.

        :param port: The port of this PathFirewallRulesRequest.
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this PathFirewallRulesRequest.

        :return: The protocol of this PathFirewallRulesRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this PathFirewallRulesRequest.

        :param protocol: The protocol of this PathFirewallRulesRequest.
        :type: str
        """

        self._protocol = protocol

    @property
    def time(self):
        """
        Gets the time of this PathFirewallRulesRequest.

        :return: The time of this PathFirewallRulesRequest.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this PathFirewallRulesRequest.

        :param time: The time of this PathFirewallRulesRequest.
        :type: int
        """

        self._time = time

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
        if not isinstance(other, PathFirewallRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other