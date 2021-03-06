
"""
Note: 

Data was taken from Wikipedia: https://vi.wikipedia.org/wiki/T%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam?oldformat=true
With reviews from General Statistics Office: https://danhmuchanhchinh.gso.gov.vn/

General Statistics Office should always be the official source!

"Thành phố Hồ Chí Minh" is referred in this file as 
                        Hồ Chí Minh in Vietnamese and
                        Ho Chi Minh in English
Rationale: Uniform pattern between provinces/ municipalities

Informal cases:
Bà Rịa - Vũng Tàu: Vũng Tàu or Bà Rịa | Vung Tau/ Ba Ria
Thừa Thiên - Huế: Thừa Thiên or Huế   | Thua Thien/ Hue

Always check date of data retrieve
"""

# Date accessed March 6th, 2021
# This value should also match the tag on git commit
__DATA__VERSION = 202103

# Vietnam Adminstrative level 0: Provinces name in Vietnamese by alphabetical order
# ADM0
VIETNAM_ADM0_ALPHABETICALLY = ["An Giang", "Bà Rịa - Vũng Tàu",
                                "Bạc Liêu", "Bắc Giang",
                                "Bắc Kạn", "Bắc Ninh",
                                "Bến Tre", "Bình Dương",
                                "Bình Định", "Bình Phước",
                                "Bình Thuận", "Cà Mau",
                                "Cao Bằng", "Cần Thơ",
                                "Đà Nẵng", "Đắk Lắk",
                                "Đắk Nông", "Điện Biên",
                                "Đồng Nai", "Đồng Tháp",
                                "Gia Lai", "Hà Giang",
                                "Hà Nam", "Hà Nội",
                                "Hà Tĩnh", "Hải Dương",
                                "Hải Phòng", "Hậu Giang",
                                "Hòa Bình", "Hồ Chí Minh",
                                "Hưng Yên", "Khánh Hòa",
                                "Kiên Giang", "Kon Tum",
                                "Lai Châu", "Lạng Sơn",
                                "Lào Cai", "Lâm Đồng",
                                "Long An", "Nam Định",
                                "Nghệ An", "Ninh Bình",
                                "Ninh Thuận", "Phú Thọ",
                                "Phú Yên", "Quảng Bình",
                                "Quảng Nam", "Quảng Ngãi",
                                "Quảng Ninh", "Quảng Trị",
                                "Sóc Trăng", "Sơn La",
                                "Tây Ninh", "Thái Bình",
                                "Thái Nguyên", "Thanh Hóa",
                                "Thừa Thiên Huế", "Tiền Giang",
                                "Trà Vinh", "Tuyên Quang",
                                "Vĩnh Long", "Vĩnh Phúc",
                                "Yên Bái"
]

# Vietnam Adminstrative level 0: Provinces by alphabetical order
# ADM0
VIETNAM_ADM0_NO_DIACRITICS = {
    "An Giang"          : "An Giang",
    "Bà Rịa - Vũng Tàu" : "Ba Ria - Vung Tau",
    "Bạc Liêu"          : "Bac Lieu",
    "Bắc Giang"         : "Bac Giang",
    "Bắc Kạn"           : "Bac Kan",
    "Bắc Ninh"          : "Bac Ninh",
    "Bến Tre"           : "Ben Tre",
    "Bình Dương"        : "Binh Duong",
    "Bình Định"         : "Binh Dinh",
    "Bình Phước"        : "Binh Phuoc",
    "Bình Thuận"        : "Binh Thuan",
    "Cà Mau"            : "Ca Mau",
    "Cao Bằng"          : "Cao Bang",
    "Cần Thơ"           : "Can Tho",
    "Đà Nẵng"           : "Da Nang",
    "Đắk Lắk"           : "Dak Lak",
    "Đắk Nông"          : "Dak Nong",
    "Điện Biên"         : "Dien Bien",
    "Đồng Nai"          : "Dong Nai",
    "Đồng Tháp"         : "Dong Thap",
    "Gia Lai"           : "Gia Lai",
    "Hà Giang"          : "Ha Giang",
    "Hà Nam"            : "Ha Nam",
    "Hà Nội"            : "Ha Noi",
    "Hà Tĩnh"           : "Ha Tinh",
    "Hải Dương"         : "Hai Duong",
    "Hải Phòng"         : "Hai Phong",
    "Hậu Giang"         : "Hau Giang",
    "Hòa Bình"          : "Hoa Binh",
    "Hồ Chí Minh"       : "Ho Chi Minh",
    "Hưng Yên"          : "Hung Yen",
    "Khánh Hòa"         : "Khanh Hoa",
    "Kiên Giang"        : "Kien Giang",
    "Kon Tum"           : "Kon Tum",
    "Lai Châu"          : "Lai Chau",
    "Lạng Sơn"          : "Lang Son",
    "Lào Cai"           : "Lao Cai",
    "Lâm Đồng"          : "Lam Dong",
    "Long An"           : "Long An",
    "Nam Định"          : "Nam Đinh",
    "Nghệ An"           : "Nghe An",
    "Ninh Bình"         : "Ninh Binh",
    "Ninh Thuận"        : "Ninh Thuan",
    "Phú Thọ"           : "Phu Tho",
    "Phú Yên"           : "Phu Yen",
    "Quảng Bình"        : "Quang Binh",
    "Quảng Nam"         : "Quang Nam",
    "Quảng Ngãi"        : "Quang Ngai",
    "Quảng Ninh"        : "Quang Ninh",
    "Quảng Trị"         : "Quang Tri",
    "Sóc Trăng"         : "Soc Trang",
    "Sơn La"            : "Son La",
    "Tây Ninh"          : "Tay Ninh",
    "Thái Bình"         : "Thai Binh",
    "Thái Nguyên"       : "Thai Nguyen",
    "Thanh Hóa"         : "Thanh Hoa",
    "Thừa Thiên Huế"    : "Thua Thien Hue",
    "Tiền Giang"        : "Tien Giang",
    "Trà Vinh"          : "Tra Vinh",
    "Tuyên Quang"       : "Tuyen Quang",
    "Vĩnh Long"         : "Vinh Long",
    "Vĩnh Phúc"         : "Vinh Phúc",
    "Yên Bái"           : "Yen Bai",
}


VIETNAM_ADM0_NORTHWEST = [
    "Điện Biên",
    "Hòa Bình",
    "Lai Châu",
    "Lào Cai",
    "Sơn La",
    "Yên Bái",
]


VIETNAM_ADM0_NORTHEAST = [
    "Bắc Giang",
    "Bắc Kạn",
    "Cao Bằng",
    "Hà Giang",
    "Lạng Sơn",
    "Phú Thọ",
    "Quảng Ninh",
    "Thái Nguyên",
    "Tuyên Quang",
]


VIETNAM_ADM0_HONG_RIVER_DELTA = [
    "Bắc Ninh",
    "Hà Nam",
    "Hà Nội",
    "Hải Dương",
    "Hải Phòng",
    "Hưng Yên",
    "Nam Định",
    "Ninh Bình",
    "Thái Bình",
    "Vĩnh Phúc",
]


VIETNAM_ADM0_NORTH_CENTRAL_COAST = [
    "Hà Tĩnh",
    "Nghệ An",
    "Quảng Bình",
    "Quảng Trị",
    "Thanh Hóa",
    "Thừa Thiên Huế",
]


VIETNAM_ADM0_SOUTH_CENTRAL_COAST = [
    "Bình Định",
    "Bình Thuận",
    "Đà Nẵng",
    "Khánh Hòa",
    "Ninh Thuận",
    "Phú Yên",
    "Quảng Nam",
    "Quảng Ngãi",
]


VIETNAM_ADM0_CENTRAL_HIGHLANDS = [
    "Đắk Lắk",
    "Đắk Nông",
    "Gia Lai",
    "Kon Tum",
    "Lâm Đồng",
]


VIETNAM_ADM0_SOUTHEAST = [
    "Bà Rịa - Vũng Tàu",
    "Bình Dương",
    "Bình Phước",
    "Đồng Nai",
    "Hồ Chí Minh",
    "Tây Ninh",
]


VIETNAM_ADM0_MEKONG_RIVER_DELTA = [
    "An Giang",
    "Bạc Liêu",
    "Bến Tre",
    "Cà Mau",
    "Cần Thơ",
    "Đồng Tháp",
    "Hậu Giang",
    "Kiên Giang",
    "Long An",
    "Sóc Trăng",
    "Tiền Giang",
    "Trà Vinh",
    "Vĩnh Long",
]


# Source: https://www.wikiwand.com/vi/Mi%E1%BB%81n_Vi%E1%BB%87t_Nam
VIETNAM_ADM0_REGIONS = {
    "northwest"             : VIETNAM_ADM0_NORTHWEST,
    "northeast"             : VIETNAM_ADM0_NORTHEAST,
    "hong_river_delta"      : VIETNAM_ADM0_HONG_RIVER_DELTA,
    "north_central_coast"   : VIETNAM_ADM0_NORTH_CENTRAL_COAST,
    "south_central_coast"   : VIETNAM_ADM0_SOUTH_CENTRAL_COAST,
    "central_highlands"     : VIETNAM_ADM0_CENTRAL_HIGHLANDS,
    "southeast"             : VIETNAM_ADM0_SOUTHEAST,
    "mekong_river_delta"    : VIETNAM_ADM0_MEKONG_RIVER_DELTA,
}


VIETNAM_ADM0_MACRO_REGIONS = {
    "north"   : VIETNAM_ADM0_NORTHWEST + VIETNAM_ADM0_NORTHEAST + VIETNAM_ADM0_HONG_RIVER_DELTA,
    "central" : VIETNAM_ADM0_NORTH_CENTRAL_COAST + VIETNAM_ADM0_SOUTH_CENTRAL_COAST + VIETNAM_ADM0_CENTRAL_HIGHLANDS,
    "south"   : VIETNAM_ADM0_SOUTHEAST + VIETNAM_ADM0_MEKONG_RIVER_DELTA,
}