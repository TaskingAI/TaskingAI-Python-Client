# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six

class ActionCreateResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'status': 'object',
        'data': 'object'
    }

    attribute_map = {
        'status': 'status',
        'data': 'data'
    }

    def __init__(self, status=None, data=None):  # noqa: E501
        """ActionCreateResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._data = None
        self.discriminator = None
        self.status = status
        self.data = data

    @property
    def status(self):
        """Gets the status of this ActionCreateResponse.  # noqa: E501

        The response status.  # noqa: E501

        :return: The status of this ActionCreateResponse.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActionCreateResponse.

        The response status.  # noqa: E501

        :param status: The status of this ActionCreateResponse.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def data(self):
        """Gets the data of this ActionCreateResponse.  # noqa: E501

        The created actions.  # noqa: E501

        :return: The data of this ActionCreateResponse.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ActionCreateResponse.

        The created actions.  # noqa: E501

        :param data: The data of this ActionCreateResponse.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ActionCreateResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
