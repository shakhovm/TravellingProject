import requests
import json


def get_tickets_json(url, params, path):
    """
    :param url: str
    :param path: str
    :return: None

    Create the json with tickets

    """

    text = requests.get(url, params=params)
    text = text.text
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(json.loads(text), file, indent=4)


if __name__ == "__main__":
    url = "https://www.omio.com/GoEuroAPI/rest/api/v5/results"
    params = {
                 'direction': 'outbound',
                 'easy': '0',
                 'eoff': 'on',
                 'exclude_offsite_bus_results': True,
                 'include_segment_positions': True,
                 'search_id': 1342261648,
                 'sort_by': 'updateTime',
                 'sort_variants': 'onsiteDepartureTime, outboundDepartureTime, outboundPrice, price, smart, traveltime',
                 'spl_tren': 'v1',
                 'updated_since': 0,
                 'use_recommendation': True,
                 'use_stats': True
    }
    get_tickets_json(url, params, "goeuro.json")
