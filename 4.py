import shippo

# 设置API密钥
shippo.api_key = "YOUR_API_KEY"

# 创建地址
address_from = shippo.Address.create(
    name="John Doe",
    street1="123 Main St",
    city="San Francisco",
    state="CA",
    zip="94105",
    country="US"
)

address_to = shippo.Address.create(
    name="Jane Doe",
    street1="456 Oak St",
    city="New York",
    state="NY",
    zip="10001",
    country="US"
)

# 创建包裹
parcel = shippo.Parcel.create(
    length="5",
    width="5",
    height="5",
    distance_unit="in",
    weight="2",
    mass_unit="lb"
)

# 创建物流
shipment = shippo.Shipment.create(
    address_from=address_from,
    address_to=address_to,
    parcels=[parcel]
)

# 获取运输费率
rates = shipment.rates

# 创建物流标签
transaction = shippo.Transaction.create(
    rate=rates[0].object_id,
    label_file_type="PDF",
    async=False
)

# 获取跟踪信息
tracking = shippo.Track.get_status(transaction.tracking_number)

print(f"Tracking status: {tracking.tracking_status.status}")