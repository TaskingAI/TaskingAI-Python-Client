# coding: utf-8

"""
    TaskingAI API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Message(object):
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
        'object': 'object',
        'message_id': 'object',
        'chat_id': 'object',
        'assistant_id': 'object',
        'role': 'object',
        'content': 'object',
        'metadata': 'object',
        'created_timestamp': 'object'
    }

    attribute_map = {
        'object': 'object',
        'message_id': 'message_id',
        'chat_id': 'chat_id',
        'assistant_id': 'assistant_id',
        'role': 'role',
        'content': 'content',
        'metadata': 'metadata',
        'created_timestamp': 'created_timestamp'
    }

    def __init__(self, object=None, message_id=None, chat_id=None, assistant_id=None, role=None, content=None, metadata=None, created_timestamp=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._message_id = None
        self._chat_id = None
        self._assistant_id = None
        self._role = None
        self._content = None
        self._metadata = None
        self._created_timestamp = None
        self.discriminator = None
        self.object = object
        self.message_id = message_id
        self.chat_id = chat_id
        self.assistant_id = assistant_id
        self.role = role
        self.content = content
        self.metadata = metadata
        self.created_timestamp = created_timestamp

    @property
    def object(self):
        """Gets the object of this Message.  # noqa: E501

        The object type, which is always `Message`.  # noqa: E501

        :return: The object of this Message.  # noqa: E501
        :rtype: object
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Message.

        The object type, which is always `Message`.  # noqa: E501

        :param object: The object of this Message.  # noqa: E501
        :type: object
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def message_id(self):
        """Gets the message_id of this Message.  # noqa: E501

        The message ID.  # noqa: E501

        :return: The message_id of this Message.  # noqa: E501
        :rtype: object
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this Message.

        The message ID.  # noqa: E501

        :param message_id: The message_id of this Message.  # noqa: E501
        :type: object
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def chat_id(self):
        """Gets the chat_id of this Message.  # noqa: E501

        The chat ID.  # noqa: E501

        :return: The chat_id of this Message.  # noqa: E501
        :rtype: object
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this Message.

        The chat ID.  # noqa: E501

        :param chat_id: The chat_id of this Message.  # noqa: E501
        :type: object
        """
        if chat_id is None:
            raise ValueError("Invalid value for `chat_id`, must not be `None`")  # noqa: E501

        self._chat_id = chat_id

    @property
    def assistant_id(self):
        """Gets the assistant_id of this Message.  # noqa: E501

        The assistant ID if the message is generated by an assistant.  # noqa: E501

        :return: The assistant_id of this Message.  # noqa: E501
        :rtype: object
        """
        return self._assistant_id

    @assistant_id.setter
    def assistant_id(self, assistant_id):
        """Sets the assistant_id of this Message.

        The assistant ID if the message is generated by an assistant.  # noqa: E501

        :param assistant_id: The assistant_id of this Message.  # noqa: E501
        :type: object
        """
        if assistant_id is None:
            raise ValueError("Invalid value for `assistant_id`, must not be `None`")  # noqa: E501

        self._assistant_id = assistant_id

    @property
    def role(self):
        """Gets the role of this Message.  # noqa: E501

        The role of the message. It can be `user` or `assistant`.  # noqa: E501

        :return: The role of this Message.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Message.

        The role of the message. It can be `user` or `assistant`.  # noqa: E501

        :param role: The role of this Message.  # noqa: E501
        :type: object
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501

        The message content.  # noqa: E501

        :return: The content of this Message.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.

        The message content.  # noqa: E501

        :param content: The content of this Message.  # noqa: E501
        :type: object
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def metadata(self):
        """Gets the metadata of this Message.  # noqa: E501

        The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.  # noqa: E501

        :return: The metadata of this Message.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Message.

        The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.  # noqa: E501

        :param metadata: The metadata of this Message.  # noqa: E501
        :type: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this Message.  # noqa: E501

        The timestamp when the message was created.  # noqa: E501

        :return: The created_timestamp of this Message.  # noqa: E501
        :rtype: object
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this Message.

        The timestamp when the message was created.  # noqa: E501

        :param created_timestamp: The created_timestamp of this Message.  # noqa: E501
        :type: object
        """
        if created_timestamp is None:
            raise ValueError("Invalid value for `created_timestamp`, must not be `None`")  # noqa: E501

        self._created_timestamp = created_timestamp

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
