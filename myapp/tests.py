import unittest
from unittest import mock
from google.oauth2.credentials import Credentials
from google.ads.google_ads.client import GoogleAdsClient
from management.commands import google_ads


class TestGoogleAds(unittest.TestCase):
    @mock.patch('google.auth.default')
    def test_get_google_ads_client(self, mock_default):
        # Set up the mock to return a test credentials object
        mock_credentials = mock.MagicMock(spec=Credentials)
        mock_default.return_value = (mock_credentials, 'test-project-id')

        # Call the function to create the Google Ads API client
        client = google_ads.get_google_ads_client()

        # Check that the client is an instance of GoogleAdsClient
        self.assertIsInstance(client, GoogleAdsClient)

        # Check that the client was created with the expected credentials
        self.assertIs(client.credentials, mock_credentials)
