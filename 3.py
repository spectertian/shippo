
import shippo
from shippo.models import components

shippo_sdk = shippo.Shippo(api_key_header="shippo_test_77c7a25626eef46e0e4e616afb726f2d43cfcd62")

shippo_sdk.addresses.create(
    components.AddressCreateRequest(
        name="Shawn Ippotle",
        company="Shippo",
        street1="215 Clayton St.",
        city="San Francisco",
        state="CA",
        zip="94117",
        country="US", # iso2 country code
        phone="+1 555 341 9393",
        email="shippotle@shippo.com"
    )
)
