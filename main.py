import requests
import time
import os


class Authorizer:
    """
    Obtains and saves OAuth access token from amadeus API.
    Client info and token is saved locally.
    """
    def __init__(self):
        # Get client info
        with open("clientinfo.txt", "r") as f:
            self.client_id, self.client_secret = [k.strip("\n") for k in f.readlines()]
        self.url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Get token
        self.token = self.get_token()

    def get_token(self) -> str:
        """
        Obtains and returns local token. If local token is expired, get_new_token() is called.

        :return: currently active token.
        """

        def get_timestamp_from_filename(filename: str) -> int:
            """
            Obtains timestamp from the local .tok filename

            :param filename: .tok filename which includes the token
            :return: timestamp from the filename
            """
            return int(filename.split('.')[0])

        token_files = sorted([k for k in os.listdir() if k[-4:] == '.tok'])
        try:
            most_recent_token_file = token_files[-1]
        except IndexError: # no token files
            return self.get_new_token()

        if int(time.time()) - get_timestamp_from_filename(most_recent_token_file) > 1730: # expired token
            os.remove(most_recent_token_file)
            return self.get_new_token()
        else: # fresh token exists :D
            with open(most_recent_token_file) as f:
                token = f.read()
            return token

    def get_new_token(self) -> str:
        """
        Requests a new access token from Amadeus API, then saves it locally.

        :return: newly obtained access token
        """
        oauth_headers = {"content-type": "application/x-www-form-urlencoded"}
        oauth_data = f"grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}"
        oauth_response = requests.post(self.url, data=oauth_data, headers=oauth_headers)
        access_token = oauth_response.json()['access_token']

        with open(f"{int(time.time())}.tok", 'w') as f:
            f.write(access_token)

        return access_token


class Explorer:
    """
    An "explorer" of destinations with a free set of dates and a maximum price threshold. Akin to Google Flight's
    explore.
    """
    def __init__(self, authorizer: Authorizer):
        self.url = "https://test.api.amadeus.com/v1/shopping/flight-destinations?"
        self.params = {}
        self.authorizer = authorizer

    def example(self):
        """
        An example explorer instance. Searches flights out of NYC with a maxPrice of 500 USD.

        :return: List of results in the format of:

        [
            {
                'type': 'flight-destination',
                'origin': 'JFK',
                'destination': 'MCO',
                'departureDate': '2024-10-29',
                'returnDate': '2024-10-30',
                'price': {'total': '67.95'}
            },
            {
                'type': 'flight-destination',
                'origin': 'LGA',
                'destination': 'FLL',
                'departureDate': '2025-01-14',
                'returnDate': '2025-01-15',
                'price': {'total': '83.99'}
            }, ...
        ]
        """
        headers = {"Authorization": "Bearer " + self.authorizer.token}
        ex_params = {"origin": "NYC",
                     "maxPrice": "500"}
        res = requests.get(self.url, headers=headers, params=ex_params)
        # todo: check for bad responses; if bad response is due to auth token, get a new token
        if res:
            _json = res.json()
            _itinerary_list = _json['data']
            _itinerary_parseable_list = [{k: v for k, v in i.items() if k != 'links'} for i in _itinerary_list]
            return _itinerary_parseable_list
        else:
            print(res.json())
            return None


class Searcher:
    """
    Accepts search parameters and returns search results.
    """
    def __init__(self):
        pass


if __name__ == "__main__":
    auth = Authorizer()
    expl = Explorer(auth)
    explore_list = expl.example()
    print(explore_list)
    pass