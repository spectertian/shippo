
import shippo
from shippo.models import components
#
shippo_sdk = shippo.Shippo(api_key_header="shippo_test_77c7a25626eef46e0e4e616afb726f2d43cfcd62")

address_from = components.AddressCreateRequest(
    name="Shawn Ippotle",
    street1="215 Clayton St.",
    city="San Francisco",
    state="CA",
    zip="94117",
    country="US"
)

address_to = components.AddressCreateRequest(
    name="Mr Hippo",
    street1="Broadway 1",
    city="New York",
    state="NY",
    zip="10007",
    country="US"
)

# validation = shippo_sdk.addresses.validate(address=address_to)
# if validation.validation_results.is_valid:
#     # 使用验证后的地址
#     validated_address = validation.validation_results
# else:
#     # 处理无效地址
#     print(validation.validation_results)

parcel = components.ParcelCreateRequest(
    length="5",
    width="5",
    height="5",
    distance_unit=components.DistanceUnitEnum.IN,
    weight="2",
    mass_unit=components.WeightUnitEnum.LB
)

shipment = shippo_sdk.shipments.create(
    components.ShipmentCreateRequest(
        address_from=address_from,
        address_to=address_to,
        parcels=[parcel],
        async_=False
    )
)



# Get the first rate in the rates results.
# Customize this based on your business logic.
rate = shipment.rates[0]
# Purchase the desired rate.
transaction = shippo_sdk.transactions.create(
    components.TransactionCreateRequest(
        rate=rate.object_id,
        label_file_type=components.LabelFileTypeEnum.PDF,
        async_=False
    )
)

# Retrieve label url and tracking number or error message
if transaction.status == "SUCCESS":
    print(transaction.label_url)
    print(transaction.tracking_number)
else:
    print("xxx")
    print(transaction.messages)
    print(transaction.messages.ResponseMessage)
