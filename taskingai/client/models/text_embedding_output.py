# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six

class TextEmbeddingOutput(object):
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
        'index': 'object',
        'embedding': 'object'
    }

    attribute_map = {
        'index': 'index',
        'embedding': 'embedding'
    }

    def __init__(self, index=None, embedding=None):  # noqa: E501
        """TextEmbeddingOutput - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._embedding = None
        self.discriminator = None
        self.index = index
        self.embedding = embedding

    @property
    def index(self):
        """Gets the index of this TextEmbeddingOutput.  # noqa: E501

        The index of the embedding output.  # noqa: E501

        :return: The index of this TextEmbeddingOutput.  # noqa: E501
        :rtype: object
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TextEmbeddingOutput.

        The index of the embedding output.  # noqa: E501

        :param index: The index of this TextEmbeddingOutput.  # noqa: E501
        :type: object
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def embedding(self):
        """Gets the embedding of this TextEmbeddingOutput.  # noqa: E501

        The embedding vector.  # noqa: E501

        :return: The embedding of this TextEmbeddingOutput.  # noqa: E501
        :rtype: object
        """
        return self._embedding

    @embedding.setter
    def embedding(self, embedding):
        """Sets the embedding of this TextEmbeddingOutput.

        The embedding vector.  # noqa: E501

        :param embedding: The embedding of this TextEmbeddingOutput.  # noqa: E501
        :type: object
        """
        if embedding is None:
            raise ValueError("Invalid value for `embedding`, must not be `None`")  # noqa: E501

        self._embedding = embedding

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
        if issubclass(TextEmbeddingOutput, dict):
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
        if not isinstance(other, TextEmbeddingOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
