# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MetricsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_metrics(self, entity_id, metric, interval, start, end, **kwargs):
        """
        Get metric points for an entity
        Get metric points for an entity for an entity id and metric for a given time interval. Maximum number of metrics point returned by API is 300. In case the interval and time period combination have more than 300 metrics points, client should break the time period to multiple batches to get all the metrics points.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metrics(entity_id, metric, interval, start, end, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: entity type (required)
        :param str metric: metric name (required)
        :param int interval: metric points interval (required)
        :param int start: start time for query in epoch seconds (required)
        :param int end: end time for query in epoch seconds (required)
        :return: MetricResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_metrics_with_http_info(entity_id, metric, interval, start, end, **kwargs)
        else:
            (data) = self.get_metrics_with_http_info(entity_id, metric, interval, start, end, **kwargs)
            return data

    def get_metrics_with_http_info(self, entity_id, metric, interval, start, end, **kwargs):
        """
        Get metric points for an entity
        Get metric points for an entity for an entity id and metric for a given time interval. Maximum number of metrics point returned by API is 300. In case the interval and time period combination have more than 300 metrics points, client should break the time period to multiple batches to get all the metrics points.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_metrics_with_http_info(entity_id, metric, interval, start, end, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: entity type (required)
        :param str metric: metric name (required)
        :param int interval: metric points interval (required)
        :param int start: start time for query in epoch seconds (required)
        :param int end: end time for query in epoch seconds (required)
        :return: MetricResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'metric', 'interval', 'start', 'end']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_metrics`")
        # verify the required parameter 'metric' is set
        if ('metric' not in params) or (params['metric'] is None):
            raise ValueError("Missing the required parameter `metric` when calling `get_metrics`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_metrics`")
        # verify the required parameter 'start' is set
        if ('start' not in params) or (params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_metrics`")
        # verify the required parameter 'end' is set
        if ('end' not in params) or (params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `get_metrics`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'entity_id' in params:
            query_params.append(('entity_id', params['entity_id']))
        if 'metric' in params:
            query_params.append(('metric', params['metric']))
        if 'interval' in params:
            query_params.append(('interval', params['interval']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'end' in params:
            query_params.append(('end', params['end']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/metrics', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MetricResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
