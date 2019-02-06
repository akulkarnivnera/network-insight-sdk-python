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


class ApiError(object):
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
        'code': 'int',
        'message': 'str',
        'details': 'list[ErrorDetail]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, code=None, message=None, details=None):
        """
        ApiError - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._details = None

        if code is not None:
          self.code = code
        if message is not None:
          self.message = message
        if details is not None:
          self.details = details

    @property
    def code(self):
        """
        Gets the code of this ApiError.

        :return: The code of this ApiError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ApiError.

        :param code: The code of this ApiError.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ApiError.

        :return: The message of this ApiError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ApiError.

        :param message: The message of this ApiError.
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """
        Gets the details of this ApiError.

        :return: The details of this ApiError.
        :rtype: list[ErrorDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ApiError.

        :param details: The details of this ApiError.
        :type: list[ErrorDetail]
        """

        self._details = details

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
        if not isinstance(other, ApiError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
