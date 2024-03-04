import pytest
import taskingai
from taskingai.tool import bulk_create_actions, get_action, update_action, delete_action, run_action, list_actions, ActionAuthentication, ActionAuthenticationType
from test.common.logger import logger
from test.config import *


@pytest.mark.test_sync
class TestAction:
    action_list = ['action_id', "operation_id", 'name', 'description', "url", "method", "path_param_schema",
                   "query_param_schema", "body_param_schema", "body_type", "function_def", 'authentication',
                   'openapi_schema', 'created_timestamp', 'updated_timestamp']
    action_keys = set(action_list)
    action_authentication = ['type', 'secret', 'content']
    action_authentication_keys = set(action_authentication)
    action_openapi_schema = ['openapi', 'info', 'servers', 'paths', 'components', 'security']
    action_openapi_schema_keys = set(action_openapi_schema)
    schema = {
                                "openapi_schema": {
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
                                                "description": "Get temperature for a specific location 123",
                                                "operationId": "GetCurrentWeather123",
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
                                    }

                                },
                                "authentication": {
                                    "type": "bearer",
                                    "secret": "ASD213dfslkfa12"
                                }
                            }

    @pytest.mark.run(order=11)
    def test_bulk_create_actions(self):

        # Create an action.
        for i in range(2):
            res = bulk_create_actions(**self.schema)
            for action in res:
                action_dict = vars(action)
                logger.info(action_dict)
                pytest.assume(action_dict.keys() == self.action_keys)
                pytest.assume(action_dict["openapi_schema"].keys() == self.action_openapi_schema_keys)
                for key in self.schema["openapi_schema"].keys():
                    pytest.assume(action_dict["openapi_schema"][key] == self.schema["openapi_schema"][key])
                    assert set(vars(action_dict.get("authentication")).keys()).issubset(TestAction.action_authentication_keys)

    @pytest.mark.run(order=12)
    def test_list_actions(self):

        # List actions.

        nums_limit = 1
        res = list_actions(limit=nums_limit)
        logger.info(res)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].action_id
        after_res = list_actions(limit=nums_limit, after=after_id)
        logger.info(after_res)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = list_actions(limit=nums_limit * 2)
        logger.info(twice_nums_list)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].action_id
        before_res = list_actions(limit=nums_limit, before=before_id)
        logger.info(before_res)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=13)
    def test_get_action(self, action_id):

        # Get an action.

        res = get_action(action_id=action_id)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.action_keys)
        logger.info(res_dict["openapi_schema"].keys())
        pytest.assume(res_dict["openapi_schema"].keys() == self.action_openapi_schema_keys)
        pytest.assume(res_dict["action_id"] == action_id)
        pytest.assume(vars(res_dict["authentication"]).keys() == self.action_authentication_keys)

    @pytest.mark.run(order=14)
    def test_update_action(self, action_id):

        # Update an action.

        update_schema = {
                        "openapi_schema": {
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
                                        "description": "Get fact about a number",
                                        "operationId": "get_number_fact",
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
                    }
        res = update_action(action_id=action_id, **update_schema)
        res_dict = vars(res)
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.action_keys)
        for key in update_schema.keys():
            if key != "authentication":
                for k, v in update_schema[key].items():
                    pytest.assume(res_dict[key][k] == v)
                assert set(res_dict.get(key).keys()).issubset(getattr(TestAction, f"action_{key}_keys"))
            else:
                assert set(vars(res_dict.get(key)).keys()).issubset(getattr(TestAction, f"action_{key}_keys"))
                for k, v in update_schema[key].items():
                    if k == "type":
                        pytest.assume(vars(res_dict[key])[k] == v)
                    else:
                        pytest.assume("*" in vars(res_dict[key])[k])

    @pytest.mark.run(order=15)
    def test_run_action(self, action_id):

        # Run an action.

        parameters = {
                "number": 42
        }
        res = run_action(action_id=action_id, parameters=parameters)
        logger.info(f'async run action{res}')
        pytest.assume(res['status'] == 200)
        pytest.assume(res["data"])

    @pytest.mark.run(order=80)
    def test_delete_action(self):

        # List actions.

        actions = list_actions(limit=100)
        old_nums = len(actions)

        for index, action in enumerate(actions):
            action_id = action.action_id

            # Delete an action.

            delete_action(action_id=action_id)

            if index == old_nums-1:
                new_actions = list_actions(limit=100)
                new_nums = len(new_actions)
                pytest.assume(new_nums == 0)
