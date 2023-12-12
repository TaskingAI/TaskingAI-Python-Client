import pytest

from taskingai.tool import bulk_create_actions, get_action, update_action, delete_action, run_action, list_actions
from test.common.logger import logger


@pytest.mark.test_sync
class TestAction:

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
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/componeents/schemas/ActionCreateRequest"
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
    def test_bulk_create_actions(self):

        # List actions.

        old_res = list_actions(limit=100)
        old_nums = len(old_res)
        for x in range(2):

            # Create an action.

            res = bulk_create_actions(schema=self.schema)
            for action in res:
                action_dict = action.to_dict()
                logger.info(action_dict)
                pytest.assume(action_dict.keys() == self.action_keys)
                pytest.assume(action_dict["schema"].keys() == self.action_schema_keys)

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

                # Get an action.

                action_id = action_dict["action_id"]
                get_res = get_action(action_id=action_id)
                get_res_dict = get_res.to_dict()
                pytest.assume(get_res_dict.keys() == self.action_keys)
                pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)

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

            new_res = list_actions(limit=100)
            new_nums = len(new_res)
            res_num = len(res)
            pytest.assume(new_nums == old_nums + res_num + 2*x)

    @pytest.mark.run(order=5)
    def test_run_action(self, action_id):

        # Run an action.

        parameters = {
                      "parameters": {"location": "tokyo"}
                     }
        res = run_action(action_id=action_id, parameters=parameters)
        logger.info(f'async run action{res}')
        pytest.assume(res['status'] == 400)
        pytest.assume(res["error"])

    @pytest.mark.run(order=6)
    def test_list_actions(self):

        # List actions.

        nums_limit = 2
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

    @pytest.mark.run(order=7)
    def test_get_action(self, action_id):

        # Get an action.

        res = get_action(action_id=action_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.action_keys)
        logger.info(res_dict["schema"].keys())
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)

    @pytest.mark.run(order=39)
    def test_update_action(self, action_id):

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
        res = update_action(action_id=action_id, schema=update_schema)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.action_keys)
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(res_dict["schema"] == update_schema)

        # Get an action.

        get_res = get_action(action_id=action_id)
        get_res_dict = get_res.to_dict()
        logger.info(get_res_dict)
        pytest.assume(get_res_dict.keys() == self.action_keys)

        pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(get_res_dict["schema"] == update_schema)

    @pytest.mark.run(order=40)
    def test_delete_action(self):

        # List actions.

        actions = list_actions(limit=100)
        old_nums = len(actions)

        for index, action in enumerate(actions):
            action_id = action.action_id

            # Delete an action.

            delete_action(action_id=action_id)
            new_actions = list_actions(limit=100)
            action_ids = [action.action_id for action in new_actions]
            pytest.assume(action_id not in action_ids)
            new_nums = len(new_actions)
            pytest.assume(new_nums == old_nums - 1 - index)




