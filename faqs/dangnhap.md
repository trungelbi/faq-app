---
question: "Cách đăng nhập vào hệ thống dichvucong.gdt.gov.vn bằng tài khoản VNeID (tài khoản cá nhân)"
keywords: ["đăng nhập", "vneid", "tài khoản", "câu 1"]
---

Hướng dẫn NNT là người Việt Nam (cá nhân, cá nhân khai thay tổ chức) đăng nhập bằng tài khoản Định danh điện tử (VNeID).
- Bước 1: Người nộp thuế truy cập thành công vào Cổng thông tin điện tử (https://dichvucong.gdt.gov.vn). Chọn chức năng Đăng nhập, hệ thống hiển thị màn hình chọn loại tài khoản đăng nhập.
- Bước 2: NNT chọn Đăng nhập bằng tài khoản Định danh điện tử.
![Ảnh minh họa](images/dangnhap.png)
- Bước 3: NNT nhập tên đăng nhập/mật khẩu nhấn Đăng nhập, hệ thống hiển thị màn hình nhập mã xác nhận đăng nhập.
![Ảnh minh họa](images/dangnhap1.png)
![Ảnh minh họa](images/dangnhap2.png)
- Bước 4: Nhập mã xác nhận, nhấn Xác nhận, hệ thống VNeID kiểm tra: 
1. Trường hợp NNT được định danh với vai trò Cá nhân và Tổ chức, sẽ hiển thị màn hình chọn Loại tài khoản “Cá nhân”, “Tổ chức” 
2. Trường hợp NNT được định danh với vai trò Cá nhân, sẽ không hiển thị màn hình chọn loại tài khoản.
![Ảnh minh họa](images/dangnhap3.png)
---
question: "Cách đăng nhập vào hệ thống dichvucong.gdt.gov.vn bằng tài khoản VNeID (cá nhân không có mã số thuế)"
keywords: ["đăng nhập", "chưa có", "mã số thuế", "không có", "vneid"]
---

- Hệ thống hiển thị cảnh báo “Bạn phải đăng ký thuế để sử dụng số định danh cá nhân kê khai và nộp thuế”.  
![Ảnh minh họa](images/dangnhap4.png)
- Nhấn Đăng ký, hệ thống hiển thị danh sách các TTHC đăng ký thuế lần đầu dành cho cá nhân:
- 1.007565 - Đăng ký thuế lần đầu đối với người nộp thuế là hộ gia đình, cá nhân có hoạt động sản xuất, kinh doanh không thuộc đối tượng đăng ký kinh doanh qua cơ quan đăng ký kinh doanh.
- 1.010241 - Đăng ký thuế lần đầu đối với người nộp thuế là cá nhân có thu nhập thuộc diện chịu thuế thu nhập cá nhân hoặc có nghĩa vụ với ngân sách nhà nước (trừ cá nhân kinh doanh) - Trường hợp cá nhân đăng ký thuế trực tiếp với cơ quan thuế.
---
question: "Cách đăng nhập vào hệ thống dichvucong.gdt.gov.vn bằng tài khoản VNeID (tài khoản tổ chức)"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---

+	Tại màn hình chọn Loại tài khoản, chọn đăng nhập với vai trò Tổ chức. Hệ thống Bộ Công An trả thông tin MST gắn với Định danh điện tử và Danh sách quyền (Quản trị hoặc Thành viên)
- Hệ thống TTHC kiểm tra thông tin tài khoản Thuế điện tử gắn với thông tin MST:
+	Có tài khoản Thuế điện tử ở trạng thái Hoạt động: Hệ thống hiển thị màn hình Trang chủ
![Ảnh minh họa](images/dangnhap5.png)

+	Có tài khoản Thuế điện tử ở trạng thái Ngừng hoạt động hoặc Chưa có tài khoản Thuế điện tử: Hệ thống TTHC kiểm tra quyền gắn MST với Định danh điện tử
Nếu quyền Thành viên: Hệ thống hiển thị cảnh báo “NSD không được quyền đăng ký tài khoản Thuế điện tử”
Nếu có quyền Quản trị: Hệ thống TTHC thực hiện gọi API Đăng ký thuế của hệ thống DataHub với thông tin MST gắn với Định danh điện tử, hệ thống DataHub trả kết quả, TTHC kiểm tra “Trạng thái MST”, “Thông tin “Tên người đại diện theo pháp luật” và thực hiện kiểm tra Tên người đại diện theo pháp luật (Datahub) và Tên theo Định danh điện tử:
1. Không hợp lệ: Hệ thống hiển thị cảnh báo “NSD không được quyền đăng ký tài khoản Thuế điện tử”
2. Hợp lệ: Hệ thống TTHC kiểm tra “Trạng thái MST”
3. Nếu trạng thái = 01 - NNT ngừng hoạt động và đã hoàn thành thủ tục chấm dứt hiệu lực MST, Hệ thống hiển thị cảnh báo “ MST đang ở trạng thái ngừng hoạt động, không được phép đăng ký tài khoản Thuế điện tử”
4. Nếu trạng thái khác 01- NNT ngừng hoạt động và đã hoàn thành thủ tục chấm dứt hiệu lực MST, hệ thống hiển thị cảnh báo “Bạn phải đăng ký tài khoản giao dịch Thuế điện tử để thực hiện các thủ tục hành chính về lĩnh vực Thuế.” (NSD kích Đăng ký, hệ thống hiển thị màn hình Đăng ký tài khoản
![Ảnh minh họa](images/dangnhap6.png)
---
question: "Cách đăng nhập vào hệ thống dichvucong.gdt.gov.vn bằng tài khoản thuế điện tử (tài khoản cá nhân)"
keywords: ["đăng nhập", "cá nhân", "tài khoản", "thuế điện tử"]
---
- Hướng dẫn NNT là người nước ngoài (cá nhân/tổ chức nước ngoài) đăng nhập bằng mã số thuế.
Bước 1: Người nộp thuế truy cập thành công vào Cổng thông tin điện tử (trang thông tin https://dichvucong.gdt.gov.vn). Chọn chức năng Đăng nhập, hệ thống hiển thị màn hình chọn loại tài khoản đăng nhập.
Bước 2: NNT chọn chức năng Đăng nhập bằng tài khoản Thuế điện tử.
Bước 3: NNT nhập tên đăng nhập/mật khẩu nhấn “Đăng nhập”.
+	Hệ thống TTHC thực hiện SSO sang hệ thống iCanhan và kiểm tra thông tin tài khoản đăng ký dịch vụ như sau:
+	Kiểm tra tài khoản trên hệ thống iCanhan:
+	Không hợp lệ: Hệ thống hiển thị cảnh báo lỗi trên màn hình
+	Hợp lệ: Hệ thống kiểm tra trạng thái tài khoản trên hệ thông iCanhan
•	Ngừng hoạt động: Hệ thống hiển thị cảnh báo “Tài khoản đang ở trạng thái Ngừng hoạt động”
Hoạt động: Hệ thống đăng nhập thành công, hiển thị màn hình Trang chủ TTHC
![Ảnh minh họa](images/dangnhap7.png)

---
question: "Cách đăng nhập vào hệ thống dichvucong.gdt.gov.vn bằng tài khoản thuế điện tử (tài khoản tổ chức)"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
- Hướng dẫn NNT là người nước ngoài (cá nhân/tổ chức nước ngoài) đăng nhập bằng mã số thuế.
Bước 1: Người nộp thuế truy cập thành công vào Cổng thông tin điện tử (trang thông tin https://dichvucong.gdt.gov.vn). Chọn chức năng Đăng nhập, hệ thống hiển thị màn hình chọn loại tài khoản đăng nhập.
Bước 2: NNT chọn chức năng Đăng nhập bằng tài khoản Thuế điện tử.
Bước 3: NNT nhập tên đăng nhập/mật khẩu nhấn “Đăng nhập”.
+	Hệ thống TTHC thực hiện SSO sang hệ thống ETAX và kiểm tra thông tin tài khoản đăng ký dịch vụ như sau:
+	Kiểm tra tài khoản trên hệ thống ETAX:
+	Không hợp lệ: Hệ thống hiển thị cảnh báo lỗi trên màn hình
+	Hợp lệ: Hệ thống kiểm tra trạng thái tài khoản trên hệ thông ICanhan
•	Ngừng hoạt động: Hệ thống hiển thị cảnh báo “Tài khoản đang ở trạng thái Ngừng hoạt động”
•	Hoạt động: Hệ thống đăng nhập thành công, hiển thị màn hình Trang chủ TTHC
![Ảnh minh họa](images/dangnhap8.png)

---
question: "Hướng dẫn Kê khai tờ khai 01-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Kê khai tờ khai 02-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Kê khai tờ khai 03-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Kê khai tờ khai 04-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Kê khai tờ khai 05-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Kê khai tờ khai 06-ĐK-TCT"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Tra cứu hồ sơ trên trang Người nộp thuế"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
---
question: "Hướng dẫn Tra cứu hồ sơ trên trang Cán bộ thuế"
keywords: ["đăng nhập", "tổ chức", "tài khoản", "vneid"]
---
