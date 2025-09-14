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
question: "Cách tạo mã số thuế cá nhân - mẫu 05/DK"
keywords: ["mã số thuế", "cá nhân", "05"]
---
Hướng dẫn NNT kê khai tờ khai đăng ký thuế (dùng cho cá nhân) mẫu số 05-ĐK-TCT đáp ứng Thông tư số 86/2024/TT-BTC ngày 23/12/2024 của Bộ trưởng Bộ Tài chính
Bước 1: Chọn TTHC
NSD chọn chức năng “Thủ tục hành chính”, hệ thống hiển thị màn hình như sau:
![Ảnh minh họa](images/05dk.png)
- Mô tả các thông tin hiển thị trên màn hình:
![Ảnh minh họa](images/05dk1.png)
- NSD nhập điều kiện tìm kiếm, nhấn “Tìm kiếm, hệ thống hiển thị màn hình kết quả theo điều kiện tìm kiếm
Bước 2: Hệ thống hiển thị màn hình các hồ sơ cần chuẩn bị (MH1)
- NSD chọn Nộp hồ sơ đối với mã TTHC 1.010241 để thực hiện khai báo tờ khai 05-ĐK-TCT > Hệ thống hiển thị màn hình thông báo các hồ sơ cần chuẩn bị.
![Ảnh minh họa](images/05dk2.png)
Bước 3: Nhấn “Tiếp tục”, hệ thống hiển thị màn hình chọn đối tượng (MH2)
![Ảnh minh họa](images/05dk3.png)
Bước 4: Nhấn “Tiếp tục”, hiển thị màn hình thông tin cá nhân đăng ký thuế (MH3)
![Ảnh minh họa](images/05dk4.png)
- Mô tả các thông tin hiển thị trên màn hình:
![Ảnh minh họa](images/05dk5.png)
Bước 5: Nhấn “Tiếp tục”, hiển thị màn hình thông tin địa chỉ cá nhân (MH4)
![Ảnh minh họa](images/05dk6.png)
- Mô tả các thông tin hiển thị trên màn hình:
![Ảnh minh họa](images/05dk7.png)
Bước 6: Nhấn “Tiếp tục”, hiển thị màn hình Hồ sơ (MH5)
![Ảnh minh họa](images/05dk8.png)
- Mô tả các thông tin hiển thị trên màn hình:
![Ảnh minh họa](images/05dk9.png)
Bước 7: Nhấn “Nộp hồ sơ”, hiển thị màn hình nhập mã OTP (MH6)
![Ảnh minh họa](images/05dk10.png)
- Mô tả các thông tin hiển thị trên màn hình:
![Ảnh minh họa](images/05dk11.png)
Bước 8: Hiển thị màn hình kết quả nộp tờ khai
![Ảnh minh họa](images/05dk12.png)
-	Mã hồ sơ: NNT sử dụng mã hồ sơ này để tra cứu hồ sơ đã nộp thành công tại chức năng “Tra cứu hồ sơ”.
---
---
question: "CÁCH NỘP THUẾ ĐIỆN TỬ QUA ỨNG DỤNG ETAX MOBILE"
keywords: ["thuế điện tử", "ứng dụng", "etax", "mobile"]
---
1.	Tải ứng dụng về và cài đặt trên điện thoại
![Ảnh minh họa](images/mobile.png)
2.  Đăng nhập
Cách 1: đăng nhập bằng tài khoản thuế điện tử
Mã số thuế: Nhập số CCCD. 
Mật khẩu: Nhập mật khẩu đã được cấp, nếu quên thì bấm Quên mật khẩu để tạo lại.
Nếu chưa có tài khoản thì bấm Đăng ký. Liên hệ bộ phận 1 cửa cơ quan thuế để duyệt tài khoản
Cách 2: Đăng nhập bằng tài khoản định danh: bấm ô Đăng nhập bằng tài khoản định danh màu trắng. Nhập các thông tin nếu hệ thống yêu cầu, bấm chia sẻ thông tin để chuyển tự động qua đăng nhập app eTax.
![Ảnh minh họa](images/mobile1.png)

3. Liên kết ngân hàng: bước này chỉ thực hiện 1 lần, các lần nộp thuế sau không làm.
![Ảnh minh họa](images/mobile2.png)

4. Nộp thuế/Nộp thuế thay
Nếu nộp thuế cho bản thân thì chọn  Nộp Thuế/Tra cứu/Nộp tất cả. Kiểm tra từng nội dung khoản nộp, sau đó nộp theo thứ tự thanh toán đã hiển thị sẵn. Tích chọn biểu tượng ngân hàng đã đăng ký, bấm Tiếp tục, xác thực OTP. Hệ thống báo nộp thuế thành công thì bấm chọn “ Tiếp tục nộp thuế” để thực hiện nộp các khoản tiếp theo.
![Ảnh minh họa](images/mobile3.png)

Nếu nộp thay cho người khác thì chọn: Nộp thuế thay, ô mã số thuế người được nộp thay: nhập số căn cước công dân người được nộp thuế thay.
![Ảnh minh họa](images/mobile4.png)

Lưu ý: Trường hợp Tạo mã QR code của giấy nộp tiền để quét thanh toán, thì dùng chức năng Quét mã QR để nộp thuế trên eTax Mobile để nộp chứ không phải quét từ app ngân hàng
5. Tra cứu chứng từ
Vào Nhóm chức năng nộp thuế/Tra cứu chứng từ nộp thuế
Chỉ nhập khoảng thời gian, không cần nhập mã tra cứu.

---
question: "HƯỚNG DẪN CHÍNH SÁCH THUẾ CHO DOANH NGHIỆP MỚI THÀNH LẬP"
keywords: ["chính sách", "thuế", "doanh nghiệp", "thành lập"]
---
I/ THỦ TỤC KÊ KHAI THUẾ, NỘP THUẾ
1.	Phần mềm hỗ trợ kê khai thuế (HTKK)
DN thường xuyên cập nhật phần mềm hỗ trợ kê khai thuế hiện hành (hiện đang sử dụng phiên bản HTKK mới nhất) sử dụng để kê khai và nộp hồ sơ khai thuế đến cơ quan thuế quản lý trực tiếp. Phần mềm hỗ trợ kê khai thuế được cung cấp miễn phí tại trang thông tin điện tử Cục Thuế TP. Đà Nẵng: http://danang.gdt.gov.vn (banner Hỗ trợ kê khai thuế).
2.	Khai thuế điện tử, Nộp thuế điện tử:
DN thực hiện nộp hồ sơ khai thuế qua mạng internet và nộp tiền thuế điện tử tại website: http://thuedientu.gdt.gov.vn
* Thời hạn nộp thuế: Thời hạn nộp tiền thuế vào ngân sách nhà nước (NSNN) là thời hạn nộp hồ sơ khai thuế.
3.	Khai thuế và lệ phí Môn bài
3.0.	Chính phủ vừa ban hành Nghị định số 22/2020/NĐ-CP sửa đổi Nghị định 139/2016/NĐ-CP quy định về lệ phí môn bài, có hiệu lực từ ngày 25/2/2020.
Theo đó, nghị định mới bổ sung đối tượng được miễn lệ phí môn bài trong năm đầu thành lập hoặc ra hoạt động sản xuất, kinh doanh (từ 1/1 đến 31/12), bao gồm: tổ chức thành lập mới (được cấp mã số thuế mới, mã số doanh nghiệp mới); hộ gia đình, cá nhân, nhóm cá nhân lần đầu ra hoạt động sản xuất, kinh doanh; chi nhánh, văn phòng đại diện, địa điểm kinh doanh do 2 đối tượng trên thành lập trong thời gian được miễn lệ phí môn bài.
 
Doanh nghiệp nhỏ và vừa chuyển đổi từ hộ kinh doanh được miễn lệ phí môn bài trong thời hạn 3 năm, kể từ ngày cấp giấy chứng nhận đăng ký doanh nghiệp lần đầu.
3.1.	Khai Lệ phí môn bài: Khai lệ phí môn bài một lần khi người nộp lệ phí mới ra hoạt động kinh doanh, chậm nhất là ngày cuối cùng của tháng bắt đầu hoạt động sản xuất kinh doanh (SXKD). Trường hợp người nộp lệ phí mới thành lập cơ sở kinh doanh nhưng chưa hoạt động SXKD thì khai Lệ phí môn bài trong thời hạn 30 ngày, kể từ ngày được cấp giấy chứng nhận đăng ký kinh doanh hoặc ngày cấp giấy chứng nhận đăng ký đầu tư và đăng ký thuế.
Ví dụ: DN A đăng ký hoạt động kinh doanh từ ngày 06/3/2018 thì thời hạn nộp tờ khai lệ phí Môn bài và nộp tiền lệ phí Môn bài năm 2018 chậm nhất là ngày 31/3/2018.
Đối với các đối tượng được miễn lệ phí môn bài năm đầu tiên theo Nghị định số 22/2020/NĐ-CP sửa đổi Nghị định 139/2016/NĐ-CP thì thực hiện nộp hồ sơ khai lệ phí môn bài chậm nhất là ngày 30 tháng 01 năm sau năm thành lập hoặc bắt đầu hoạt động sản xuất, kinh doanh.
 
3.2.	Khai thuế Giá trị gia tăng (GTGT), thuế thu nhập cá nhân (TNCN)
-	Phương pháp tính thuế GTGT: Theo Điều 12, điều 13 Thông tư 219/2013/TT- BTC ngày 31 tháng 12 năm 2013 hướng dẫn thi hành Luật thuế giá trị gia tăng và Nghị định số 209/2013/NĐ-CP ngày 18/12/2013 của Chính phủ quy định chi tiết và hướng dẫn thi hành một số điều luật thuế giá trị gia tăng và Thông tư 93/2017/TT- BTC ngày 19 tháng 9 năm 2017 sửa đổi, bổ sung khoản 3, khoản 4 điều 12 Thông tư số 219/2013/TT-BTC ngày 31/12/2013 (đã được sửa đổi, bổ sung tại thông tư số 119/2014/TT-BTC ngày 25/8/2014) và bãi bỏ khoản 7 điều 11 Thông tư số 156/2013/TT-BTC ngày 06/11/2013 của Bộ Tài chính.
-	Kỳ khai thuế GTGT, thuế TNCN:
1.	Tiêu chí khai thuế theo quý
a)	Khai thuế giá trị gia tăng theo quý áp dụng đối với:
a.1)	Người nộp thuế thuộc diện khai thuế giá trị gia tăng theo tháng được quy định tại điểm a khoản 1 Điều 8 Nghị định số 126/2020/NĐ-CP nếu có tổng doanh thu bán hàng hoá và cung cấp dịch vụ của năm trước liền kề từ 50 tỷ đồng trở xuống thì được khai thuế giá trị gia tăng theo quý. Doanh thu bán hàng hóa, cung cấp dịch vụ được xác định là tổng doanh thu trên các tờ khai thuế giá trị gia tăng của các kỳ tính thuế trong năm dương lịch.
Trường hợp người nộp thuế thực hiện khai thuế tập trung tại trụ sở chính cho đơn vị phụ thuộc, địa điểm kinh doanh thì doanh thu bán hàng hóa, cung cấp dịch vụ bao gồm cả doanh thu của đơn vị phụ thuộc, địa điểm kinh doanh.
a.2)	Trường hợp người nộp thuế mới bắt đầu hoạt động, kinh doanh thì được lựa chọn khai thuế giá trị gia tăng theo quý. Sau khi sản xuất kinh doanh đủ 12 tháng thì từ năm dương lịch liền kề tiếp theo năm đã đủ 12 tháng sẽ căn cứ theo mức doanh thu của năm dương lịch trước liền kề (đủ 12 tháng) để thực hiện khai thuế giá trị gia tăng theo kỳ tính thuế tháng hoặc quý.
b)	Khai thuế thu nhập cá nhân theo quý như sau:
b.1)	Người nộp thuế thuộc diện khai thuế thu nhập cá nhân theo tháng được quy định tại điểm a khoản 1 Điều 8 Nghị định số 126/2020/NĐ-CP nếu đủ điều kiện khai thuế giá trị gia tăng theo quý thì được lựa chọn khai thuế thu nhập cá nhân theo quý.
b.2)	Việc khai thuế theo quý được xác định một lần kể từ quý đầu tiên phát sinh nghĩa vụ khai thuế và được áp dụng ổn định trong cả năm dương lịch.
2.	Người nộp thuế có trách nhiệm tự xác định thuộc đối tượng khai thuế theo quý để thực hiện khai thuế theo quy định.
a)	Người nộp thuế đáp ứng tiêu chí khai thuế theo quý được lựa chọn khai thuế theo tháng hoặc quý ổn định trọn năm dương lịch.
b)	Trường hợp người nộp thuế đang thực hiện khai thuế theo tháng nếu đủ điều kiện khai thuế theo quý và lựa chọn chuyển sang khai thuế theo quý thì gửi văn bản đề nghị quy định tại Phụ lục I ban hành kèm theo Nghị định số 126/2020/NĐ-CP đề nghị thay đổi kỳ tính thuế đến cơ quan thuế quản lý trực tiếp chậm nhất là 31 tháng 01 của năm bắt đầu khai thuế theo quý, Nếu sau thời hạn này người nộp thuế không gửi văn bản đến cơ quan thuế thì người nộp thuế tiếp tục thực hiện khai thuế theo tháng ổn định trọn năm dương lịch.
 
c)	Trường hợp người nộp thuế tự phát hiện không đủ điều kiện khai thuế theo quý thì người nộp thuế phải thực hiện khai thuế theo tháng kể từ tháng đầu của quý tiếp theo. Người nộp thuế không phải nộp lại hồ sơ khai thuế theo tháng của các quý trước đó nhưng phải nộp Bản xác định số tiền thuế phải nộp theo tháng tăng thêm so với số đã kê khai theo quý quy định tại Phụ lục I ban hành kèm theo Nghị định này và phải tính tiền chậm nộp theo quy định.
d)	Trường hợp cơ quan thuế phát hiện người nộp thuế không đủ điều kiện khai thuế theo quý thì cơ quan thuế phải xác định lại số tiền thuế phải nộp theo tháng tăng thêm so với số người nộp thuế đã kê khai và phải tính tiền chậm nộp theo quy định. Người nộp thuế phải thực hiện khai thuế theo tháng kể từ thời điểm nhận được văn bản của cơ quan thuế.

Thời hạn nộp hồ sơ khai thuế tháng: Chậm nhất là ngày thứ 20 của tháng tiếp theo tháng phát sinh nghĩa vụ thuế.
Thời hạn nộp hồ sơ khai thuế quý: chậm nhất là ngày kết thúc của tháng đầu tiên thuộc quý tiếp theo quý phát sinh nghĩa vụ thuế.
 
3.3.	Khai thuế Tiêu thụ đặc biệt (TTĐB):
Thuế TTĐB được khai theo tháng (nếu có)
Thời hạn nộp hồ sơ khai thuế: Chậm nhất là ngày thứ 20 của tháng tiếp theo tháng phát sinh nghĩa vụ thuế.
Ví dụ: DN C bắt đầu hoạt động từ tháng 3/2017 (kinh doanh dịch vụ vũ trường, mát-xa, ka-ra-ô-kê;…) thì thời hạn nộp hồ sơ khai thuế và nộp tiền thuế TTĐB tháng 3/2017 chậm nhất là ngày 20/4/2017.
3.4.	Thuế Thu nhập doanh nghiệp (TNDN):
-	Nộp tiền thuế Thu nhập doanh nghiệp (TNDN) tạm tính theo quý: Căn cứ kết quả SXKD, DN tự xác định số thuế TNDN tạm nộp của quý và nộp vào NSNN chậm nhất là ngày thứ 30 của tháng đầu tiên của quý tiếp theo quý phát sinh nghĩa vụ thuế. DN không phải nộp tờ khai thuế TNDN tạm tính quý.
- Khai quyết toán thuế TNDN năm: Chậm nhất là ngày cuối cùng của tháng thứ 3 kể từ ngày kết thúc năm dương lịch hoặc năm tài chính đối với hồ sơ quyết toán thuế năm, DN nộp hồ sơ khai quyết toán thuế năm, gồm:
+ Hồ sơ quyết toán thuế TNDN năm gồm: Báo cáo tài chính, Tờ khai quyết toán thuế TNDN và các phụ lục đính kèm;
3.5.	Hồ sơ quyết toán thuế TNCN gồm: Tờ khai quyết toán thuế TNCN và các phụ lục đính kèm.
 
3.6.	Hồ sơ khai thuế khác (nếu có): Thực hiện theo hướng dẫn tại Nghị định số 126/2020/NĐ-CP ngày 19/10/2020 của Chính phủ quy định chi tiết một số điều của Luật Quản lý thuế.
II/ SỬ DỤNG HÓA ĐƠN
Doanh  nghiệp thực hiện đăng ký hóa đơn điện tử và sử dụng theo quy định tại Thông tư 32/2025/TT-BTC.
III/ THAY ĐỔI, BỔ SUNG THÔNG TIN ĐĂNG KÝ THUẾ
1.	Đối với DN:
Trường hợp DN, đơn vị trực thuộc của DN thay đổi địa chỉ trụ sở kinh doanh dẫn đến thay đổi cơ quan thuế quản lý, trước khi đăng ký thay đổi thông tin với cơ quan đăng ký kinh doanh, DN phải thông báo thay đổi thông tin (Mẫu số 08-MST Thông tư số 105/2020/TT-BTC) và thực hiện các thủ tục liên quan về thuế với cơ quan thuế quản lý trực tiếp
2.	Đối với tổ chức kinh tế, tổ chức khác (như Văn phòng luật sư, Hợp tác xã,…): Khi có thay đổi một trong các thông tin trên tờ khai đăng ký thuế, bảng kê kèm theo tờ khai đăng ký thuế phải thực hiện thủ tục thay đổi thông tin đăng ký thuế với cơ quan thuế quản lý trực tiếp trong thời hạn 10 (mười) ngày làm việc kể từ ngày phát sinh thông tin thay đổi. (Mẫu số 08-MST Thông tư số 105/2020/TT-BTC).

IV/ THÔNG BÁO PHƯƠNG PHÁP TRÍCH KHẤU HAO TÀI SẢN CỐ ĐỊNH
Doanh nghiệp phải thực hiện thông báo phương pháp trích khấu hao TSCĐ mà doanh nghiệp lựa chọn áp dụng với cơ quan thuế trực tiếp quản lý trước khi thực hiện trích khấu hao. Việc xác định khoản khấu hao TSCĐ được trừ khi xác định thu nhập chịu thuế TNDN thực hiện theo quy định về trích khấu hao TSCĐ và pháp luật thuế TNDN hiện hành.


Ngoài ra, DN tìm hiểu, nghiên cứu các chính sách pháp luật khác có liên quan như Luật doanh nghiệp, Luật kế toán, Luật thương mại,...

