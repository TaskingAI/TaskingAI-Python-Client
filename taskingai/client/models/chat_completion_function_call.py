# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six

class ChatCompletionFunctionCall(object):
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
        'arguments': 'object',
        'name': 'object'
    }

    attribute_map = {
        'arguments': 'arguments',
        'name': 'name'
    }

    def __init__(self, arguments=None, name=None):  # noqa: E501
        """ChatCompletionFunctionCall - a model defined in Swagger"""  # noqa: E501
        self._arguments = None
        self._name = None
        self.discriminator = None
        self.arguments = arguments
        self.name = name

    @property
    def arguments(self):
        """Gets the arguments of this ChatCompletionFunctionCall.  # noqa: E501


        :return: The arguments of this ChatCompletionFunctionCall.  # noqa: E501
        :rtype: object
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ChatCompletionFunctionCall.


        :param arguments: The arguments of this ChatCompletionFunctionCall.  # noqa: E501
        :type: object
        """
        if arguments is None:
            raise ValueError("Invalid value for `arguments`, must not be `None`")  # noqa: E501

        self._arguments = arguments

    @property
    def name(self):
        """Gets the name of this ChatCompletionFunctionCall.  # noqa: E501


        :return: The name of this ChatCompletionFunctionCall.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChatCompletionFunctionCall.


        :param name: The name of this ChatCompletionFunctionCall.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(ChatCompletionFunctionCall, dict):
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
        if not isinstance(other, ChatCompletionFunctionCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
