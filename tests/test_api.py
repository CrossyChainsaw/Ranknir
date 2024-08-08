import unittest
import json
from Ranknir.modules.api import request_clan_data_from_dadabase, request_server_data_from_dadabase
from Ranknir.modules.data_management import ServerIDs

class APITestCase(unittest.IsolatedAsyncioTestCase):

    async def test_request_clan_data_from_dadabase(self):
        """Tests if `request_clan_data_from_dadabase(id: int)` returns a valid dict of json data"""
        # Arrange
        test_server_id = ServerIDs.TEST_SERVER_ID
        # Act
        data = await request_clan_data_from_dadabase(test_server_id)
        # Assert
        self.assertIsInstance(data, dict)

    async def test_request_server_data_from_dadabase(self):
        """Tests if `request_server_data_from_dadabase(id: int)` returns a valid dict of json data"""
        # Arrange
        test_server_id = ServerIDs.TEST_SERVER_ID
        # Act
        data = await request_server_data_from_dadabase(test_server_id)
        # Assert
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()

# python -m unittest Ranknir/tests/test_api.py