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


class AggregationRequest(object):
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
        'entity_type': 'AllEntityType',
        'filter': 'str',
        'aggregations': 'list[Aggregation]',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'filter': 'filter',
        'aggregations': 'aggregations',
        'time_range': 'time_range'
    }

    def __init__(self, entity_type=None, filter=None, aggregations=None, time_range=None):
        """
        AggregationRequest - a model defined in Swagger
        """

        self._entity_type = None
        self._filter = None
        self._aggregations = None
        self._time_range = None

        if entity_type is not None:
          self.entity_type = entity_type
        if filter is not None:
          self.filter = filter
        if aggregations is not None:
          self.aggregations = aggregations
        if time_range is not None:
          self.time_range = time_range

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AggregationRequest.

        :return: The entity_type of this AggregationRequest.
        :rtype: AllEntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AggregationRequest.

        :param entity_type: The entity_type of this AggregationRequest.
        :type: AllEntityType
        """

        self._entity_type = entity_type

    @property
    def filter(self):
        """
        Gets the filter of this AggregationRequest.
        query filter

        :return: The filter of this AggregationRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this AggregationRequest.
        query filter

        :param filter: The filter of this AggregationRequest.
        :type: str
        """

        self._filter = filter

    @property
    def aggregations(self):
        """
        Gets the aggregations of this AggregationRequest.

        :return: The aggregations of this AggregationRequest.
        :rtype: list[Aggregation]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """
        Sets the aggregations of this AggregationRequest.

        :param aggregations: The aggregations of this AggregationRequest.
        :type: list[Aggregation]
        """

        self._aggregations = aggregations

    @property
    def time_range(self):
        """
        Gets the time_range of this AggregationRequest.

        :return: The time_range of this AggregationRequest.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this AggregationRequest.

        :param time_range: The time_range of this AggregationRequest.
        :type: TimeRange
        """

        self._time_range = time_range

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
        if not isinstance(other, AggregationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
