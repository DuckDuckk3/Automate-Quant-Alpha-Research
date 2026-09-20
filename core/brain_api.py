import logging

class BrainAPIClient:
    def __init__(self, session):
        self.session = session
        self.base_url = "https://api.worldquantbrain.com"
        self.logger = logging.getLogger(__name__)

    def get_auth_status(self):
        url = f"{self.base_url}/authentication"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    
    def get_datasets(self, instrument_type="EQUITY", region="USA", delay=1, universe="TOP3000"):
        url = f"{self.base_url}/data-sets"
        params = {
            "instrumentType": instrument_type,
            "region": region,
            "delay": delay,
            "universe": universe
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json().get("results", [])

    def get_datafields(self, dataset_id, search_kw=None):
        url = f"{self.base_url}/data-fields"
        params = {
            "dataset.id": dataset_id,
            "limit": 50
        }
        if search_kw:
            params["search"] = search_kw
            
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json().get("results", [])