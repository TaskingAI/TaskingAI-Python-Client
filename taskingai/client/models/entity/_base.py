# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from pydantic import BaseModel


class TaskingaiBaseModel(BaseModel):

    def to_dict(self):
        """Returns the model properties as a dict"""
        return self.model_dump()

    def to_str(self):
        """Returns the string representation of the model"""
        return self.model_dump_json()


