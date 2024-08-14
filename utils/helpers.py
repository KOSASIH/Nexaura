import requests
import logging
import time
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

def make_api_request(endpoint: str, method: str = 'GET', data: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Make an API request to the specified endpoint.

    Args:
        endpoint (str): The API endpoint to request.
        method (str, optional): The HTTP method to use. Defaults to 'GET'.
        data (Dict[str, Any], optional): The data to send with the request. Defaults to None.

    Returns:
        Dict[str, Any]: The response from the API.
    """
    url = f'{API_ENDPOINT}{endpoint}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.request(method, url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def retry_on_failure(func: callable, max_retries: int = MAX_RETRIES, timeout: int = TIMEOUT) -> callable:
    """
    Decorator to retry a function on failure.

    Args:
        func (callable): The function to retry.
        max_retries (int, optional): The maximum number of retries. Defaults to MAX_RETRIES.
        timeout (int, optional): The timeout between retries. Defaults to TIMEOUT.

    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        for i in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f'Error on attempt {i+1}: {e}')
                time.sleep(timeout)
        raise Exception(f'Max retries exceeded: {max_retries}')
    return wrapper

def parse_json_file(file_path: str) -> Dict[str, Any]:
    """
    Parse a JSON file and return its contents.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: The contents of the JSON file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def flatten_list(list_of_lists: List[List[Any]]) -> List[Any]:
    """
    Flatten a list of lists into a single list.

    Args:
        list_of_lists (List[List[Any]]): The list of lists to flatten.

    Returns:
        List[Any]: The flattened list.
    """
    return [item for sublist in list_of_lists for item in sublist]
