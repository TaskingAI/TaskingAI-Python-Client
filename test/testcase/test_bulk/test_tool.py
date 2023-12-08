import allure
import pytest

from taskingai.tool import a_create_function, a_list_functions, a_get_function, a_update_function, a_delete_function, a_bulk_create_actions, a_get_action, a_update_action, a_delete_action, a_run_action, a_list_actions
from test.common.logger import logger
from test.testcase.test_async.base import Base


# @allure.epic("test_bulk_tool")
# @allure.feature("test_function")
# @pytest.mark.bulk
# class TestFunction(Base):
#
#     function_list = ['object', 'function_id', 'name', 'description', 'parameters', 'created_timestamp']
#     function_keys = set(function_list)
#     function_parameters = ['type', 'properties', 'required']
#     function_parameters_keys = set(function_parameters)
#     nums = 100
#
#     @pytest.mark.run(order=0)
#     @allure.story("test_bulk_create_function")
#     @pytest.mark.parametrize("num", (x+1 for x in range(nums)))
#     @pytest.mark.asyncio
#     async def test_bulk_create_function(self, num):
#
#         # Create a function.
#         name = f"test{num}"
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
#
#
#     @pytest.mark.run(order=1)
#     @allure.story("test_a_list_functions")
#     @pytest.mark.asyncio
#     async def test_a_list_functions(self):
#         # List functions.
#         limit_num = 20
#         res = await a_list_functions(limit=limit_num)
#         pytest.assume(0 <= len(res) <= limit_num)
#         before_id = after_id = res[-1].function_id
#         before_res = await a_list_functions(limit=limit_num, before=before_id)
#         logger.info(before_res)
#         pytest.assume(len(before_res) <= limit_num)
#         pytest.assume(before_res[0].function_id == res[0].function_id)
#         after_res = await a_list_functions(limit=limit_num, after=after_id)
#         logger.info(after_res)
#         pytest.assume(len(after_res) <= limit_num)

#
#     @pytest.mark.run(order=37)
#     @allure.story("test_a_delete_function")
#     @pytest.mark.asyncio
#     async def test_a_delete_function(self):
#         while True:
#             # List functions.
#
#             functions = await a_list_functions()
#             old_nums = len(functions)
#             if old_nums == 0:
#                 break
#             for index, function in enumerate(functions):
#                 function_id = function.function_id
#                 # Delete a function.
#                 await a_delete_function(function_id=function_id)
#                 new_functions = await a_list_functions()
#                 function_ids = [function.function_id for function in new_functions]
#                 pytest.assume(function_id not in function_ids)


@allure.epic("test_bulk_tool")
@allure.feature("test_action")
@pytest.mark.bulk
class TestAction(Base):

    action_list = ['object', 'action_id', 'authentication', 'schema', 'created_timestamp']
    action_keys = set(action_list)
    action_schema = ['openapi', 'info', 'servers', 'paths', 'components', 'security']
    action_schema_keys = set(action_schema)
    nums = 100
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Numbers API",
            "version": "1.0.0",
            "description": "API for fetching interesting number facts"
        },
        "servers": [
            {
                "url": "http://numbersapi.com"
            }
        ],
        "paths": {
            "/{number}": {
                "get":
                {
                    "summary": "Get fact about a number",
                    "parameters": [
                        {
                            "name": "number",
                            "in": "path",
                            "required": True,
                            "description": "The number to get the fact for",
                            "schema": {
                                "type": "integer"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "A fact about the number",
                            "content": {
                                "text/plain": {
                                    "schema": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    @pytest.mark.run(order=4)
    @allure.story("test_a_bulk_create_actions")
    @pytest.mark.parametrize("num", (x+1 for x in range(nums)))
    @pytest.mark.asyncio
    async def test_a_bulk_create_actions(self, num):
        # Create an action.
        res = await a_bulk_create_actions(schema=self.schema)
        for action in res:
            action_dict = action.to_dict()
            logger.info(action_dict)
            pytest.assume(action_dict.keys() == self.action_keys)
            pytest.assume(action_dict["schema"].keys() == self.action_schema_keys)
            for key, value in self.schema.items():
                pytest.assume(action_dict["schema"][key] == self.schema[key])
            # Get an action.
            action_id = action_dict["action_id"]
            get_res = await a_get_action(action_id=action_id)
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.action_keys)
            pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
            for key, value in self.schema.items():
                pytest.assume(action_dict["schema"][key] == self.schema[key])


    @pytest.mark.run(order=6)
    @allure.story("test_a_list_actions")
    @pytest.mark.asyncio
    async def test_a_list_actions(self):
        # List actions.
        limit_num = 20
        res = await a_list_actions(limit=limit_num)
        pytest.assume(0 <= len(res) == limit_num)
        before_id = after_id = res[-1].action_id
        before_res = await a_list_actions(limit=limit_num, before=before_id)
        pytest.assume(len(before_res) <= limit_num)
        pytest.assume(before_res[0].action_id == res[0].action_id)
        after_res = await a_list_actions(limit=limit_num, after=after_id)
        pytest.assume(len(after_res) <= limit_num)
        limit_twice_res = await a_list_actions(limit=limit_num * 2)
        pytest.assume(after_res[-1].action_id == limit_twice_res[-1].action_id)

    @pytest.mark.run(order=40)
    @allure.story("test_bulk_delete_action")
    @pytest.mark.asyncio
    async def test_bulk_delete_action(self):
        while True:
            # List actions.
            actions = await a_list_actions()
            old_nums = len(actions)
            if old_nums == 0:
                break
            for index, action in enumerate(actions):
                action_id = action.action_id
                # Delete an action.
                await a_delete_action(action_id=action_id)
                new_actions = await a_list_actions()
                action_ids = [action.action_id for action in new_actions]
                pytest.assume(action_id not in action_ids)






