
import shippo
from shippo.models import components

shippo_sdk = shippo.Shippo(api_key_header="shippo_test_77c7a25626eef46e0e4e616afb726f2d43cfcd62")

address_from = components.AddressCreateRequest(
    name="Shawn Ippotle",
    company="Shippo",
    street1="215 Clayton St.",
    city="San Francisco",
    state="CA",
    zip="94117",
    country="US",
    phone="+1 555 341 9393",
    email="shippotle@shippo.com"
)

address_to = components.AddressCreateRequest(
    name="Mr Hippo",
    street1="Broadway 1",
    city="New York",
    state="NY",
    zip="10007",
    country="US",
    phone="+1 555 341 9393",
    email="mrhippo@shippo.com",
    metadata="Priority Customer"
)

parcel = components.ParcelCreateRequest(
    length="5",
    width="5",
    height="5",
    distance_unit=components.DistanceUnitEnum.IN,
    weight="2",
    mass_unit=components.WeightUnitEnum.LB
)

shipment = components.ShipmentCreateRequest(
    address_from=address_from,
    address_to=address_to,
    parcels=[parcel],
)

transaction = shippo_sdk.transactions.create(
    components.InstantTransactionCreateRequest(
        shipment=shipment,
        carrier_account="b741b99f95e841639b54272834bc478c",
        servicelevel_token="usps_priority"
    )
)
