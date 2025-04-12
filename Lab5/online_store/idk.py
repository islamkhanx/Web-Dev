from typing import List, TypedDict
import json


class Product(TypedDict):
    image: str
    item_name: str
    description: str
    rating: float
    url: str
    likes: int
    is_active: bool
    category: str


def parse_products(
    images: List[str],
    item_names: List[str],
    ratings: List[float],
    urls: List[str],
    category: str
) -> List[Product]:
    # Validate that all arrays have the same length
    if len({len(images), len(item_names), len(ratings), len(urls)}) != 1:
        raise ValueError("All input lists must have the same length")
    
    return [
        {
            "image": image,
            "item_name": item_names[i],
            "description": "",
            "rating": ratings[i],
            "url": urls[i],
            "likes": 0,
            "is_active": True,
            "category": category
        }
        for i, image in enumerate(images)
    ]


def phones():
    somevar = "phones"

    images = [
        "https://resources.cdn-kaspi.kz/img/m/p/p49/p92/11295411.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h8a/h7d/85428766703646.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h96/h46/85558406348830.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h03/h20/85428948598814.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/p78/p1f/19792401.jpeg?format=preview-large"
    ]

    item_names = [
        "CUBOT King Kong Star 2 12 ГБ/256 ГБ черный",
        "Samsung Galaxy A35 5G 8 ГБ/256 ГБ темно-синий",
        "Samsung Galaxy A35 5G 8 ГБ/256 ГБ голубой",
        "Samsung Galaxy A55 5G 8 ГБ/128 ГБ темно-синий",
        "Poco X7 Pro 12 ГБ/512 ГБ черный"
    ]

    ratings = [5, 5, 5, 5, 4.9]

    urls = [
        "https://kaspi.kz/shop/p/cubot-king-kong-star-2-12-gb-256-gb-chernyi-130887671/?c=750000000",
        "https://kaspi.kz/shop/p/samsung-galaxy-a35-5g-8-gb-256-gb-temno-sinii-117420425/?c=750000000",
        "https://kaspi.kz/shop/p/samsung-galaxy-a35-5g-8-gb-256-gb-goluboi-117855406/?c=750000000",
        "https://kaspi.kz/shop/p/samsung-galaxy-a55-5g-8-gb-128-gb-temno-sinii-117420239/?c=750000000",
        "https://resources.cdn-kaspi.kz/img/m/p/p78/p1f/19792401.jpeg?format=preview-large"
    ]

    products = parse_products(
        images,
        item_names,
        ratings,
        urls,
        somevar
    )

    return products


def washers():
    somevar = "washers"

    images = [
        "https://resources.cdn-kaspi.kz/img/m/p/h7d/h11/82896148693022.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/p74/p25/19064471.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/hd4/h94/63804412854302.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/hb4/hbc/85539023683614.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h7a/h75/84219027259422.jpg?format=preview-large"
    ]
    item_names = [
        "Samsung WW60AG4S00CELD белый",
        "LG F2V3PS6W белый",
        "LG F2J3NS0W белый",
        "Leadbros KG60-10L21B белый",
        "LG F2V5PS0W белый"
    ]

    ratings = [4.8, 5, 5, 4.9, 5]

    urls = [
        "https://kaspi.kz/shop/p/samsung-ww60ag4s00celd-belyi-112618357/?c=750000000",
        "https://kaspi.kz/shop/p/lg-f2v3ps6w-belyi-133133391/?c=750000000",
        "https://kaspi.kz/shop/p/lg-f2j3ns0w-belyi-3601511/?c=750000000",
        "https://kaspi.kz/shop/p/leadbros-kg60-10l21b-belyi-117791405/?c=750000000",
        "https://kaspi.kz/shop/p/lg-f2v5ps0w-belyi-113958394/?c=750000000"
    ]

    products = parse_products(
        images,
        item_names,
        ratings,
        urls,
        somevar
    )

    return products


def headphones():
    somevar = "headphones"

    images = [
        "https://resources.cdn-kaspi.kz/img/m/p/hcb/h97/87309386809374.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h44/h92/85730021769246.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/ha3/h07/84108189630494.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h31/hd7/64362668556318.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/hbf/h98/63952956522526.jpg?format=preview-large",
    ]

    item_names = [
        "Apple AirPods 4 белый",
        "OEM Air pro 2 белый",
        "Apple AirPods Pro 2 with Type-C/Wireless Charging белый",
        "Apple AirPods 3 with Lightning Charging Case белый",
        "Newest M10 Newest черный",
    ]

    ratings = [5, 4.6, 5, 5, 4.1]

    urls = [
        "https://kaspi.kz/shop/p/apple-airpods-4-belyi-124333372/?c=750000000",
        "https://kaspi.kz/shop/p/oem-air-pro-2-belyi-118366664/?c=750000000",
        "https://kaspi.kz/shop/p/apple-airpods-pro-2-with-type-c-wireless-charging-belyi-113677582/?c=750000000",
        "https://kaspi.kz/shop/p/apple-airpods-3-with-lightning-charging-case-belyi-106667987/?c=750000000",
        "https://kaspi.kz/shop/p/newest-m10-newest-chernyi-102272027/?c=750000000",
    ]

    products = parse_products(
        images,
        item_names,
        ratings,
        urls,
        somevar
    )

    return products


def tablets():
    somevar = "tablets"

    images = [
        "https://resources.cdn-kaspi.kz/img/m/p/h77/h45/87311746760734.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h0b/hc4/84390016516126.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h2a/hed/86369746354206.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h5d/h3c/64865317584926.jpg?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h1c/h08/80962638282782.jpg?format=preview-large",
    ]

    item_names = [
        "AIRSTAR G2000 10 дюйм 16 Гб/512 Гб черный",
        "Samsung Galaxy Tab A9+ 5G 11 дюйм 8 Гб/128 Гб серебристый",
        "Apple iPad Air 2022 10.9 Wi-Fi 10.9 дюйм 8 Гб/64 Гб синий",
        "Apple iPad 2022 10.9 Wi-Fi 10.9 дюйм 4 Гб/64 Гб серебристый",
        "Pencil V2 белый",
    ]

    ratings = [4.1, 5, 5, 5, 4.4]

    urls = [
        "https://kaspi.kz/shop/p/airstar-g2000-10-djuim-16-gb-512-gb-chernyi-124333904/?c=750000000",
        "https://kaspi.kz/shop/p/samsung-galaxy-tab-a9-5g-11-djuim-8-gb-128-gb-serebristyi-114175605/?c=750000000",
        "https://kaspi.kz/shop/p/apple-ipad-air-2022-10-9-wi-fi-10-9-djuim-8-gb-64-gb-sinii-104235571/?c=750000000",
        "https://kaspi.kz/shop/p/apple-ipad-2022-10-9-wi-fi-10-9-djuim-4-gb-64-gb-serebristyi-107264764/?c=750000000",
        "https://kaspi.kz/shop/p/pencil-v2-belyi-110586586/?c=750000000",
    ]

    products = parse_products(
        images,
        item_names,
        ratings,
        urls,
        somevar
    )

    return products

def monitors():
    somevar = "monitors"
    
    images =[
        "https://resources.cdn-kaspi.kz/img/m/p/pb3/p48/14220046.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/hf4/h94/84370445533214.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h37/hb2/85226229727262.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h8a/h5d/85074454511646.png?format=preview-large",
        "https://resources.cdn-kaspi.kz/img/m/p/h28/hfc/83298067742750.jpg?format=preview-large",
    ]
if __name__ == "__main__":
    items = []
    items.extend(phones())
    items.extend(washers())
    items.extend(headphones())
    items.extend(tablets())

    data = json.dumps(items)
    with open("src/app/data.json", "w") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
