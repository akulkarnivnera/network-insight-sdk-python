# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InfobloxManagerDataSourceRequest(object):
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
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'credentials': 'PasswordCredentials'
    }

    attribute_map = {
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials'
    }

    def __init__(self, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None):
        """
        InfobloxManagerDataSourceRequest - a model defined in Swagger
        """

        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._credentials = None

        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        self.proxy_id = proxy_id
        self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        self.credentials = credentials

    @property
    def ip(self):
        """
        Gets the ip of this InfobloxManagerDataSourceRequest.

        :return: The ip of this InfobloxManagerDataSourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this InfobloxManagerDataSourceRequest.

        :param ip: The ip of this InfobloxManagerDataSourceRequest.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this InfobloxManagerDataSourceRequest.

        :return: The fqdn of this InfobloxManagerDataSourceRequest.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this InfobloxManagerDataSourceRequest.

        :param fqdn: The fqdn of this InfobloxManagerDataSourceRequest.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this InfobloxManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :return: The proxy_id of this InfobloxManagerDataSourceRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this InfobloxManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this InfobloxManagerDataSourceRequest.
        :type: str
        """
        if proxy_id is None:
            raise ValueError("Invalid value for `proxy_id`, must not be `None`")

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this InfobloxManagerDataSourceRequest.

        :return: The nickname of this InfobloxManagerDataSourceRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this InfobloxManagerDataSourceRequest.

        :param nickname: The nickname of this InfobloxManagerDataSourceRequest.
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this InfobloxManagerDataSourceRequest.

        :return: The enabled of this InfobloxManagerDataSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this InfobloxManagerDataSourceRequest.

        :param enabled: The enabled of this InfobloxManagerDataSourceRequest.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this InfobloxManagerDataSourceRequest.

        :return: The notes of this InfobloxManagerDataSourceRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this InfobloxManagerDataSourceRequest.

        :param notes: The notes of this InfobloxManagerDataSourceRequest.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this InfobloxManagerDataSourceRequest.

        :return: The credentials of this InfobloxManagerDataSourceRequest.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this InfobloxManagerDataSourceRequest.

        :param credentials: The credentials of this InfobloxManagerDataSourceRequest.
        :type: PasswordCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
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
        if not isinstance(other, InfobloxManagerDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
