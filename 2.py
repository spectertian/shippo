import shippo
import time

# 使用测试API密钥
shippo.api_key = "shippo_test_77c7a25626eef46e0e4e616afb726f2d43cfcd62"

def create_shipment():
    # 创建发件人地址
    address_from = shippo.Addresses.create(
        name="Ms Hippo",
        company="Shippo",
        street1="215 Clayton St.",
        city="San Francisco",
        state="CA",
        zip="94117",
        country="US",
        phone="+1 555 341 9393",
        email="ms-hippo@goshippo.com"
    )

    # 创建收件人地址
    address_to = shippo.Addresses.create(
        name="Mr Hippo",
        company="Shippo",
        street1="965 Mission St.",
        city="San Francisco",
        state="CA",
        zip="94105",
        country="US",
        phone="+1 555 341 9393",
        email="mr-hippo@goshippo.com"
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

    # 创建shipment
    shipment = shippo.Shipment.create(
        address_from=address_from,
        address_to=address_to,
        parcels=[parcel],
        **{"async": False}  # 使用字典解包来传递 'async' 参数
    )

    return shipment

def create_label(shipment):
    # 选择最便宜的运输方式
    rate = shipment.rates_list[0]

    # 创建交易（即购买运输标签）
    transaction = shippo.Transaction.create(
        rate=rate.object_id,
        label_file_type="PDF",
        **{"async": False}  # 使用字典解包来传递 'async' 参数
    )

    return transaction

def main():
    # 创建shipment
    print("Creating shipment...")
    shipment = create_shipment()
    print("Shipment created successfully.")

    # 创建运输标签
    print("Creating shipping label...")
    transaction = create_label(shipment)

    # 检查交易状态
    if transaction.status == "SUCCESS":
        print("Label created successfully.")
        print(f"Tracking Number: {transaction.tracking_number}")
        print(f"Label URL: {transaction.label_url}")
    else:
        print("Label creation failed.")
        print(f"Error message: {transaction.messages}")

if __name__ == "__main__":
    main()