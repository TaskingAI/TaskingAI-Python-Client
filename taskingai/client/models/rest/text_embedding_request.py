# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six

class TextEmbeddingRequest(object):
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
        'model_id': 'object',
        'input': 'object'
    }

    attribute_map = {
        'model_id': 'model_id',
        'input': 'input'
    }

    def __init__(self, model_id=None, input=None):  # noqa: E501
        """TextEmbeddingRequest - a model defined in Swagger"""  # noqa: E501
        self._model_id = None
        self._input = None
        self.discriminator = None
        self.model_id = model_id
        self.input = input

    @property
    def model_id(self):
        """Gets the model_id of this TextEmbeddingRequest.  # noqa: E501

        The text embedding model id.  # noqa: E501

        :return: The model_id of this TextEmbeddingRequest.  # noqa: E501
        :rtype: object
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this TextEmbeddingRequest.

        The text embedding model id.  # noqa: E501

        :param model_id: The model_id of this TextEmbeddingRequest.  # noqa: E501
        :type: object
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def input(self):
        """Gets the input of this TextEmbeddingRequest.  # noqa: E501

        The input text or a list of input texts.  # noqa: E501

        :return: The input of this TextEmbeddingRequest.  # noqa: E501
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TextEmbeddingRequest.

        The input text or a list of input texts.  # noqa: E501

        :param input: The input of this TextEmbeddingRequest.  # noqa: E501
        :type: object
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

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
        if issubclass(TextEmbeddingRequest, dict):
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
        if not isinstance(other, TextEmbeddingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other