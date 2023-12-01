import allure
import pytest

from taskingai.tool import a_create_function, a_list_functions, a_get_function, a_update_function, a_delete_function, a_bulk_create_actions, a_get_action, a_update_action, a_delete_action, a_run_action, a_list_actions
from test.common.logger import logger
from test.testcase.test_async.base import Base

@allure.epic("test_tool")
@allure.feature("test_function")
@pytest.mark.a_sync
class TestFunction(Base):

    function_list = ['object', 'function_id', 'name', 'description', 'parameters', 'created_timestamp']
    function_keys = set(function_list)
    function_parameters = ['type', 'properties', 'required']
    function_parameters_keys = set(function_parameters)

    @pytest.mark.run(order=0)
    @allure.story("test_a_create_function")
    @pytest.mark.asyncio
    async def test_a_create_function(self):
        # List functions.
        old_res = await a_list_functions()
        old_nums = len(old_res)
        # Create a function.
        name = "test"
        description = "test for function"
        parameters = {
                            "type": "object",
                            "properties": {
                                "a": {
                                    "type": "number",
                                    "description": "First number."
                                },
                                "b": {
                                    "type": "number",
                                    "description": "Second number."
                                }
                            },
                            "required": ["a", "b"]
                        }

        res = await a_create_function(name=name, description=description, parameters=parameters)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.function_keys)
        pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        pytest.assume(res_dict["parameters"] == parameters)
        # Get a function.
        get_res = await a_get_function(function_id=res_dict["function_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.function_keys)
        pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)
        pytest.assume(get_res_dict["parameters"] == parameters)
        # List functions.
        new_res = await a_list_functions()
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @pytest.mark.run(order=1)
    @allure.story("test_a_list_functions")
    @pytest.mark.asyncio
    async def test_a_list_functions(self):
        # List functions.
        res = await a_list_functions()
        assert len(res) >= 0

    @pytest.mark.run(order=2)
    @allure.story("test_a_get_function")
    @pytest.mark.asyncio
    async def test_a_get_function(self, a_function_id):
        # Get a function.
        if not Base.function_id:
            Base.function_id = await a_function_id
        res = await a_get_function(function_id=self.function_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.function_keys)
        pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)

    @pytest.mark.run(order=3)
    @allure.story("test_a_update_function")
    @pytest.mark.asyncio
    async def test_a_update_function(self):
        # Update a function.
        name = "test"
        description = "test for function"
        parameters = {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                }
            },
            "required": ["name"]
        }
        res = await a_update_function(function_id=self.function_id, name=name, description=description, parameters=parameters)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.function_keys)
        pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        pytest.assume(res_dict["parameters"] == parameters)
        # Get a function.
        get_res = await a_get_function(function_id=self.function_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.function_keys)
        pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)
        pytest.assume(get_res_dict["parameters"] == parameters)

    @pytest.mark.run(order=37)
    @allure.story("test_a_delete_function")
    @pytest.mark.asyncio
    async def test_a_delete_function(self):
        # List functions.
        functions = await a_list_functions()
        old_nums = len(functions)

        for index, function in enumerate(functions):
            function_id = function.function_id
            # Delete a function.
            await a_delete_function(function_id=function_id)
            new_functions = await a_list_functions()
            function_ids = [function.function_id for function in new_functions]
            pytest.assume(function_id not in function_ids)
            new_nums = len(new_functions)
            assert new_nums == old_nums - 1 - index


@allure.epic("test_tool")
@allure.feature("test_action")
@pytest.mark.a_sync
class TestAction(Base):

    action_list = ['object', 'action_id', 'authentication', 'schema', 'created_timestamp']
    action_keys = set(action_list)
    action_schema = ['openapi', 'info', 'servers', 'paths', 'components', 'security']
    action_schema_keys = set(action_schema)
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
                "get": {
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
    @pytest.mark.asyncio
    async def test_a_bulk_create_actions(self):
        # List actions.
        old_res = await a_list_actions()
        old_nums = len(old_res)
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
        # List actions.
        new_res = await a_list_actions()
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @pytest.mark.run(order=5)
    @allure.story("test_a_run_action")
    @pytest.mark.asyncio
    async def test_a_run_action(self, a_action_id):
        # Run an action.
        if not Base.action_id:
            Base.action_id = await a_action_id
        parameters = {"number": 42}
        res = await a_run_action(action_id=self.action_id, parameters=parameters)
        pytest.assume(res['status'] == 200)
        pytest.assume(res["data"])

    @pytest.mark.run(order=6)
    @allure.story("test_a_list_actions")
    @pytest.mark.asyncio
    async def test_a_list_actions(self):
        # List actions.
        res = await a_list_actions()
        assert len(res) >= 0

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
        self.schema["paths"]["/{number}"]["get"]["summary"] = "Get fun fact about a number)"
        res = await a_update_action(action_id=self.action_id, schema=self.schema)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.action_keys)
        # pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(res_dict["schema"] == self.schema)
        # Get an action.
        get_res = await a_get_action(action_id=self.action_id)
        get_res_dict = get_res.to_dict()
        logger.info(get_res_dict)
        pytest.assume(get_res_dict.keys() == self.action_keys)
        # pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(get_res_dict["schema"]["paths"]["/{number}"]["get"]["summary"] == self.schema["paths"]["/{number}"]["get"]["summary"])

    @pytest.mark.run(order=40)
    @allure.story("test_a_delete_action")
    @pytest.mark.asyncio
    async def test_a_delete_action(self):
        # List actions.
        actions = await a_list_actions()
        old_nums = len(actions)

        for index, action in enumerate(actions):
            action_id = action.action_id
            # Delete an action.
            await a_delete_action(action_id=action_id)
            new_actions = await a_list_actions()
            action_ids = [action.action_id for action in new_actions]
            pytest.assume(action_id not in action_ids)
            new_nums = len(new_actions)
            assert new_nums == old_nums - 1 - index




