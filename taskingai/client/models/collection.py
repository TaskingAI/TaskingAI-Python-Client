# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Collection(object):
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
        'collection_id': 'object',
        'name': 'object',
        'description': 'object',
        'capacity': 'object',
        'num_records': 'object',
        'num_chunks': 'object',
        'configs': 'object',
        'embedding_model_id': 'object',
        'metadata': 'object',
        'created_timestamp': 'object',
        'status': 'object'
    }

    attribute_map = {
        'object': 'object',
        'collection_id': 'collection_id',
        'name': 'name',
        'description': 'description',
        'capacity': 'capacity',
        'num_records': 'num_records',
        'num_chunks': 'num_chunks',
        'configs': 'configs',
        'embedding_model_id': 'embedding_model_id',
        'metadata': 'metadata',
        'created_timestamp': 'created_timestamp',
        'status': 'status'
    }

    def __init__(self, object=None, collection_id=None, name=None, description=None, capacity=None, num_records=None, num_chunks=None, configs=None, embedding_model_id=None, metadata=None, created_timestamp=None, status=None):  # noqa: E501
        """Collection - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._collection_id = None
        self._name = None
        self._description = None
        self._capacity = None
        self._num_records = None
        self._num_chunks = None
        self._configs = None
        self._embedding_model_id = None
        self._metadata = None
        self._created_timestamp = None
        self._status = None
        self.discriminator = None
        self.object = object
        self.collection_id = collection_id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.num_records = num_records
        self.num_chunks = num_chunks
        self.configs = configs
        self.embedding_model_id = embedding_model_id
        self.metadata = metadata
        self.created_timestamp = created_timestamp
        self.status = status

    @property
    def object(self):
        """Gets the object of this Collection.  # noqa: E501

        The object type, which is always `Collection`.  # noqa: E501

        :return: The object of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Collection.

        The object type, which is always `Collection`.  # noqa: E501

        :param object: The object of this Collection.  # noqa: E501
        :type: object
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def collection_id(self):
        """Gets the collection_id of this Collection.  # noqa: E501

        The collection ID.  # noqa: E501

        :return: The collection_id of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this Collection.

        The collection ID.  # noqa: E501

        :param collection_id: The collection_id of this Collection.  # noqa: E501
        :type: object
        """
        if collection_id is None:
            raise ValueError("Invalid value for `collection_id`, must not be `None`")  # noqa: E501

        self._collection_id = collection_id

    @property
    def name(self):
        """Gets the name of this Collection.  # noqa: E501

        The collection name  # noqa: E501

        :return: The name of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Collection.

        The collection name  # noqa: E501

        :param name: The name of this Collection.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Collection.  # noqa: E501

        The collection description  # noqa: E501

        :return: The description of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Collection.

        The collection description  # noqa: E501

        :param description: The description of this Collection.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def capacity(self):
        """Gets the capacity of this Collection.  # noqa: E501

        The collection capacity. Currently only 1000 is supported and we'll provide more options in the future.  # noqa: E501

        :return: The capacity of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Collection.

        The collection capacity. Currently only 1000 is supported and we'll provide more options in the future.  # noqa: E501

        :param capacity: The capacity of this Collection.  # noqa: E501
        :type: object
        """
        if capacity is None:
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def num_records(self):
        """Gets the num_records of this Collection.  # noqa: E501

        The number of records in the collection.  # noqa: E501

        :return: The num_records of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._num_records

    @num_records.setter
    def num_records(self, num_records):
        """Sets the num_records of this Collection.

        The number of records in the collection.  # noqa: E501

        :param num_records: The num_records of this Collection.  # noqa: E501
        :type: object
        """
        if num_records is None:
            raise ValueError("Invalid value for `num_records`, must not be `None`")  # noqa: E501

        self._num_records = num_records

    @property
    def num_chunks(self):
        """Gets the num_chunks of this Collection.  # noqa: E501

        The number of chunks in the collection.  # noqa: E501

        :return: The num_chunks of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._num_chunks

    @num_chunks.setter
    def num_chunks(self, num_chunks):
        """Sets the num_chunks of this Collection.

        The number of chunks in the collection.  # noqa: E501

        :param num_chunks: The num_chunks of this Collection.  # noqa: E501
        :type: object
        """
        if num_chunks is None:
            raise ValueError("Invalid value for `num_chunks`, must not be `None`")  # noqa: E501

        self._num_chunks = num_chunks

    @property
    def configs(self):
        """Gets the configs of this Collection.  # noqa: E501

        The collection configs.  # noqa: E501

        :return: The configs of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this Collection.

        The collection configs.  # noqa: E501

        :param configs: The configs of this Collection.  # noqa: E501
        :type: object
        """
        if configs is None:
            raise ValueError("Invalid value for `configs`, must not be `None`")  # noqa: E501

        self._configs = configs

    @property
    def embedding_model_id(self):
        """Gets the embedding_model_id of this Collection.  # noqa: E501

        The ID of an available text embedding model in your project.  # noqa: E501

        :return: The embedding_model_id of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._embedding_model_id

    @embedding_model_id.setter
    def embedding_model_id(self, embedding_model_id):
        """Sets the embedding_model_id of this Collection.

        The ID of an available text embedding model in your project.  # noqa: E501

        :param embedding_model_id: The embedding_model_id of this Collection.  # noqa: E501
        :type: object
        """
        if embedding_model_id is None:
            raise ValueError("Invalid value for `embedding_model_id`, must not be `None`")  # noqa: E501

        self._embedding_model_id = embedding_model_id

    @property
    def metadata(self):
        """Gets the metadata of this Collection.  # noqa: E501

        The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.  # noqa: E501

        :return: The metadata of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Collection.

        The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.  # noqa: E501

        :param metadata: The metadata of this Collection.  # noqa: E501
        :type: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this Collection.  # noqa: E501

        The timestamp when the collection was created.  # noqa: E501

        :return: The created_timestamp of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this Collection.

        The timestamp when the collection was created.  # noqa: E501

        :param created_timestamp: The created_timestamp of this Collection.  # noqa: E501
        :type: object
        """
        if created_timestamp is None:
            raise ValueError("Invalid value for `created_timestamp`, must not be `None`")  # noqa: E501

        self._created_timestamp = created_timestamp

    @property
    def status(self):
        """Gets the status of this Collection.  # noqa: E501

        The collection status. It can be `creating`, `ready`, `deleting` or `error`.  # noqa: E501

        :return: The status of this Collection.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Collection.

        The collection status. It can be `creating`, `ready`, `deleting` or `error`.  # noqa: E501

        :param status: The status of this Collection.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(Collection, dict):
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
        if not isinstance(other, Collection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other