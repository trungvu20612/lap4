from graphviz import Digraph

# Tạo đối tượng đồ thị
erd = Digraph("ERD", filename="phone_store_erd", format="png")
erd.attr(rankdir="LR", size="12")

# Thực thể (Entities)
entities = {
    "Sản phẩm (Điện thoại)": ["Mã sản phẩm", "Tên sản phẩm", "Mã loại", "Mã thương hiệu", "Mã đơn hàng"],
    "Loại sản phẩm": ["Mã loại", "Tên loại"],
    "Thương hiệu": ["Mã thương hiệu", "Tên thương hiệu"],
    "Dịch vụ": ["Mô tả về dịch vụ", "Giá dịch vụ", "Tên dịch vụ"],
    "Người dùng (Khách hàng)": ["Mã người dùng", "Tên đăng nhập", "Họ và tên", "Mật khẩu", "Trạng thái", "Địa chỉ", "Loại người dùng", "Số điện thoại"],
    "Đơn hàng": ["Mã đơn hàng", "Ngày đặt", "Trạng thái", "Tổng tiền", "Mã người dùng", "Mã đơn vị vận chuyển"],
    "Chương trình giảm giá": ["Mã giảm giá", "Tổng tiền giảm giá", "Hạn sử dụng", "Tình trạng sử dụng"],
    "Đơn vị vận chuyển": ["Mã đơn vị vận chuyển", "Tên đơn vị vận chuyển"]
}

# Thêm thực thể vào đồ thị
for entity, attributes in entities.items():
    label = f"{entity}|" + "|".join(attributes)
    erd.node(entity, label=label, shape="record")

# Mối quan hệ (Relationships)
relationships = [
    ("Sản phẩm (Điện thoại)", "Loại sản phẩm", "Có loại"),
    ("Sản phẩm (Điện thoại)", "Thương hiệu", "Thuộc thương hiệu"),
    ("Sản phẩm (Điện thoại)", "Đơn hàng", "Được đặt trong"),
    ("Người dùng (Khách hàng)", "Đơn hàng", "Đặt"),
    ("Đơn hàng", "Đơn vị vận chuyển", "Được vận chuyển bởi"),
    ("Đơn hàng", "Chương trình giảm giá", "Áp dụng giảm giá")
]

# Thêm quan hệ vào đồ thị
for entity1, entity2, relation in relationships:
    erd.edge(entity1, entity2, label=relation)

# Xuất hình ảnh
erd_path = "/mnt/data/phone_store_erd.png"
erd.render(filename=erd_path, format="png", cleanup=True)
erd_path
