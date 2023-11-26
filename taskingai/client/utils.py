import inspect
import logging
from pathlib import Path
import urllib3

def check_kwargs(caller, given):
    argspec = inspect.getfullargspec(caller)
    diff = set(given).difference(argspec.args)
    if diff:
        logging.exception(caller.__name__ + ' had unexpected keyword argument(s): ' + ', '.join(diff), exc_info=False)


def get_version():
    return Path(__file__).parent.parent.joinpath('__version__').read_text().strip()


def get_user_agent():
    client_id = f'python-client-{get_version()}'
    user_agent_details = {'urllib3': urllib3.__version__}
    user_agent = '{} ({})'.format(client_id, ', '.join([f'{k}:{v}' for k, v in user_agent_details.items()]))
    return user_agent


