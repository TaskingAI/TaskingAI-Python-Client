import allure
import pytest
import asyncio

from taskingai.tool import a_create_function, a_list_functions, a_get_function, a_update_function, a_delete_function, a_bulk_create_actions, a_get_action, a_update_action, a_delete_action, a_run_action, a_list_actions
from test.common.logger import logger
from test.testcase.test_async.base import Base
from test.config import sleep_time, nums
# @allure.epic("test_async_tool")
# @allure.feature("test_function")
# @pytest.mark.a_sync
# class TestFunction(Base):
#
#     function_list = ['object', 'function_id', 'name', 'description', 'parameters', 'created_timestamp']
#     function_keys = set(function_list)
#     function_parameters = ['type', 'properties', 'required']
#     function_parameters_keys = set(function_parameters)
#
#     @pytest.mark.run(order=0)
#     @allure.story("test_a_create_function")
#     @pytest.mark.parametrize("function_num", (i+1 for i in range(10)))
#     @pytest.mark.asyncio
#     async def test_a_create_function(self, function_num):
#         # List functions.
#         old_res = await a_list_functions()
#         old_nums = len(old_res)
#         # Create a function.
#         name = f"test{function_num}"
#         description = "test for function"
#         parameters = {
#                             "type": "object",
#                             "properties": {
#                                 "a": {
#                                     "type": "number",
#                                     "description": "First number."
#                                 },
#                                 "b": {
#                                     "type": "number",
#                                     "description": "Second number."
#                                 }
#                             },
#                             "required": ["a", "b"]
#                         }
#
#         res = await a_create_function(name=name, description=description, parameters=parameters)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(res_dict["name"] == name)
#         pytest.assume(res_dict["description"] == description)
#         pytest.assume(res_dict["parameters"] == parameters)
#         # Get a function.
#         get_res = await a_get_function(function_id=res_dict["function_id"])
#         get_res_dict = get_res.to_dict()
#         pytest.assume(get_res_dict.keys() == self.function_keys)
#         pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(get_res_dict["name"] == name)
#         pytest.assume(get_res_dict["description"] == description)
#         pytest.assume(get_res_dict["parameters"] == parameters)
#         # List functions.
#         new_res = await a_list_functions()
#         new_nums = len(new_res)
#         pytest.assume(new_nums == old_nums + 1)
#
#     @pytest.mark.run(order=1)
#     @allure.story("test_a_list_functions")
#     @pytest.mark.asyncio
#     async def test_a_list_functions(self):
#         # List functions.
#         nums_limit = 4
#         res = await a_list_functions(limit=nums_limit)
#         pytest.assume(len(res) == nums_limit)
#         after_id = res[-1].action_id
#         after_res = await a_list_functions(limit=nums_limit, after=after_id)
#         pytest.assume(len(after_res) == nums_limit)
#         twice_nums_list = await a_list_functions(limit=nums_limit * 2)
#         pytest.assume(len(twice_nums_list) == nums_limit * 2)
#         pytest.assume(after_res[-1] == twice_nums_list[-1])
#         pytest.assume(after_res[0] == twice_nums_list[nums_limit])
#         before_id = after_res[0].action_id
#         before_res = await a_list_functions(limit=nums_limit, before=before_id)
#         pytest.assume(len(before_res) == nums_limit)
#         pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
#         pytest.assume(before_res[0] == twice_nums_list[0])
#
#     @pytest.mark.run(order=2)
#     @allure.story("test_a_get_function")
#     @pytest.mark.asyncio
#     async def test_a_get_function(self, a_function_id):
#         # Get a function.
#         if not Base.function_id:
#             Base.function_id = await a_function_id
#         res = await a_get_function(function_id=self.function_id)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#
#     @pytest.mark.run(order=3)
#     @allure.story("test_a_update_function")
#     @pytest.mark.asyncio
#     async def test_a_update_function(self):
#         # Update a function.
#         name = "test"
#         description = "test for function"
#         parameters = {
#             "type": "object",
#             "properties": {
#                 "name": {
#                     "type": "string"
#                 }
#             },
#             "required": ["name"]
#         }
#         res = await a_update_function(function_id=self.function_id, name=name, description=description, parameters=parameters)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(res_dict["name"] == name)
#         pytest.assume(res_dict["description"] == description)
#         pytest.assume(res_dict["parameters"] == parameters)
#         # Get a function.
#         get_res = await a_get_function(function_id=self.function_id)
#         get_res_dict = get_res.to_dict()
#         pytest.assume(get_res_dict.keys() == self.function_keys)
#         pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(get_res_dict["name"] == name)
#         pytest.assume(get_res_dict["description"] == description)
#         pytest.assume(get_res_dict["parameters"] == parameters)
#
#     @pytest.mark.run(order=37)
#     @allure.story("test_a_delete_function")
#     @pytest.mark.asyncio
#     async def test_a_delete_function(self):
#         # List functions.
#         functions = await a_list_functions(limit=100)
#         old_nums = len(functions)
#
#         for index, function in enumerate(functions):
#             function_id = function.function_id
#             # Delete a function.
#             await a_delete_function(function_id=function_id)
#             new_functions = await a_list_functions()
#             function_ids = [function.function_id for function in new_functions]
#             pytest.assume(function_id not in function_ids)
#             new_nums = len(new_functions)
#             pytest.assume(new_nums == old_nums - 1 - index)


@allure.epic("test_async_tool")
@allure.feature("test_action")
@pytest.mark.a_sync
class TestAction(Base):

    action_list = ['object', 'action_id', 'name', 'description', 'authentication', 'schema', 'created_timestamp']
    action_keys = set(action_list)
    action_schema = ['openapi', 'info', 'servers', 'paths', 'components', 'security']
    action_schema_keys = set(action_schema)
    schema = {
        "openapi": "3.1.0",
        "info": {
            "title": "Get weather data",
            "description": "Retrieves current weather data for a location.",
            "version": "v1.0.0"
        },
        "servers": [
            {
             "url": "https://weather.example.com"
            }
        ],
        "paths": {
            "/location": {
                "get": {
                    "description": "Get temperature for a specific location",
                    "operationId": "GetCurrentWeather",
                    "parameters": [
                        {
                            "name": "location",
                            "in": "query",
                            "description": "The city and state to retrieve the weather for",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "deprecated": False
                },
                "post": {
                    "description": "UPDATE temperature for a specific location",
                    "operationId": "UpdateCurrentWeather",
                    "requestBody": {
                         "required": True,
                         "content":{
                             "application/json":{
                                 "schema":{
                                     "$ref":"#/componeents/schemas/ActionCreateRequest"
                                 }
                             }
                         }
                    },
                    "deprecated": False
                }
            }
        },
        "components": {
            "schemas": {}
        },
        "security": []
           }

    @pytest.mark.run(order=4)
    @allure.story("test_a_bulk_create_actions")
    @pytest.mark.parametrize("async_action_num", nums)
    @pytest.mark.asyncio
    async def test_a_bulk_create_actions(self, async_action_num):
        # List actions.
        old_res = await a_list_actions(limit=100)
        old_nums = len(old_res)
        # Create an action.
        res = await a_bulk_create_actions(schema=self.schema)
        for action in res:
            action_dict = action.to_dict()
            logger.info(action_dict)
            pytest.assume(action_dict.keys() == self.action_keys)
            pytest.assume(action_dict["schema"].keys() == self.action_schema_keys)
            # for key, value in self.schema.items():
            for key in action_dict["schema"].keys():
                if key == "paths":
                    if action_dict["schema"][key]["/location"] == "get":
                        pytest.assume(action_dict["schema"][key]["/location"]["get"] == self.schema["paths"]["/location"]["get"])
                    elif action_dict["schema"][key]["/location"] == "post":
                        pytest.assume(action_dict["schema"][key]["/location"]["post"] == self.schema["paths"]["/location"]["post"])
                else:
                    pytest.assume(action_dict["schema"][key] == self.schema[key])
            # Get an action.
            action_id = action_dict["action_id"]
            get_res = await a_get_action(action_id=action_id)
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.action_keys)
            pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
            # for key, value in self.schema.items():
            for key in action_dict["schema"].keys():
                if key == "paths":
                    if action_dict["schema"][key]["/location"] == "get":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["get"] == self.schema["paths"]["/location"]["get"])
                    elif action_dict["schema"][key]["/location"] == "post":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["post"] == self.schema["paths"]["/location"][
                                "post"])
                else:
                    pytest.assume(action_dict["schema"][key] == self.schema[key])
        # List actions.
        new_res = await a_list_actions(limit=100)
        new_nums = len(new_res)
        res_num = len(res)
        pytest.assume(new_nums == old_nums + res_num)

    @pytest.mark.run(order=5)
    @allure.story("test_a_run_action")
    @pytest.mark.asyncio
    async def test_a_run_action(self, a_action_id):
        # Run an action.
        if not Base.action_id:
            Base.action_id = await a_action_id
        parameters = {"location": "beijing"}
        res = await a_run_action(action_id=self.action_id, parameters=parameters)
        logger.info(f'async run action{res}')
        pytest.assume(res['status'] == 400)
        pytest.assume(res["error"])

    @pytest.mark.run(order=6)
    @allure.story("test_a_list_actions")
    @pytest.mark.asyncio
    async def test_a_list_actions(self):
        # List actions.
        nums_limit = 4
        res = await a_list_actions(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].action_id
        after_res = await a_list_actions(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = await a_list_actions(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].action_id
        before_res = await a_list_actions(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit-1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=7)
    @allure.story("test_a_get_action")
    @pytest.mark.asyncio
    async def test_a_get_action(self):
        # Get an action.
        res = await a_get_action(action_id=self.action_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.action_keys)
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)

    @pytest.mark.run(order=39)
    @allure.story("test_a_update_action")
    @pytest.mark.asyncio
    async def test_a_update_action(self):
        # Update an action.
        update_schema = {
                            "openapi": "3.1.0",
                            "info": {
                                "title": "Get weather data",
                                "description": "Retrieves current weather data for a location.",
                                "version": "v1.0.0"
                            },
                            "servers": [
                                {
                                "url": "https://weather.example.com"
                                }
                            ],
                            "paths": {
                                "/location": {
                                    "get": {
                                        "description": "Get temperature for a specific location by get method",
                                        "operationId": "GetCurrentWeather",
                                        "parameters": [
                                            {
                                                "name": "location",
                                                "in": "query",
                                                "description": "The city and state to retrieve the weather for",
                                                "required": True,
                                                "schema": {
                                                    "type": "string"
                                                }
                                            }
                                        ],
                                        "deprecated": False
                                    }

                                }
                            },
                            "components": {
                                "schemas": {}
                            },
                            "security": []
           }

        res = await a_update_action(action_id=self.action_id, schema=update_schema)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.action_keys)
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(res_dict["schema"] == update_schema)
        # for key in res_dict["schema"].keys():
        #     pytest.assume(res_dict["schema"][key] == update_schema[key])
        # Get an action.
        get_res = await a_get_action(action_id=self.action_id)
        get_res_dict = get_res.to_dict()
        logger.info(get_res_dict)
        pytest.assume(get_res_dict.keys() == self.action_keys)
        pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(res_dict["schema"] == update_schema)
        # for key in res_dict["schema"].keys():
        #     pytest.assume(res_dict["schema"][key] == update_schema[key])
        # pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)


    @pytest.mark.run(order=40)
    @allure.story("test_a_delete_action")
    @pytest.mark.asyncio
    async def test_a_delete_action(self):
        # List actions.
        actions = await a_list_actions(limit=100)
        old_nums = len(actions)

        for index, action in enumerate(actions):
            action_id = action.action_id
            # Delete an action.
            await a_delete_action(action_id=action_id)
            await asyncio.sleep(sleep_time)
            new_actions = await a_list_actions()
            action_ids = [action.action_id for action in new_actions]
            pytest.assume(action_id not in action_ids)
            new_nums = len(new_actions)
            pytest.assume(new_nums == old_nums - 1 - index)




