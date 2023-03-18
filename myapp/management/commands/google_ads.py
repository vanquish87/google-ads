import google.auth
from google.ads.google_ads.client import GoogleAdsClient


def get_google_ads_client():
    # Get the credentials for the Google Ads API client
    credentials, _ = google.auth.default()

    # Create the Google Ads API client
    client = GoogleAdsClient(credentials=credentials)

    return client


def pause_ad(client, ad_id):
    # Get the AdService client
    ad_service = client.service('AdService')

    # Create the request to pause the Ad with the given ID
    operation = ad_service.build_operation('pause', ad_id)

    # Execute the request to pause the Ad
    response = ad_service.mutate_ad(operation)

    return response


def unpause_ad(client, ad_id):
    # Get the AdService client
    ad_service = client.service('AdService')

    # Create the request to unpause the Ad with the given ID
    operation = ad_service.build_operation('unpause', ad_id)

    # Execute the request to unpause the Ad
    response = ad_service.mutate_ad(operation)

    return response


def update_ad_attributes(client, ad_id, attributes):
    # Get the AdService client
    ad_service = client.service('AdService')

    # Create the request to update the Ad with the given ID and attributes
    update = ad_service.types.Ad()
    update.resource_name = ad_service.ad_path(ad_id)
    for key, value in attributes.items():
        setattr(update, key, value)
    operation = ad_service.build_operation('update', update)

    # Execute the request to update the Ad
    response = ad_service.mutate_ad(operation)

    return response
