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
---
question: "HƯỚNG DẪN LẬP HÓA ĐƠN TỪNG LẦN PHÁT SINH ĐỐI VỚI HỘ KINH DOANH THEO PHƯƠNG PHÁP KHOÁN"
keywords: ["hướng dẫn", "hoá đơn", "hộ kinh doanh", "phương pháp", "khoán"]
---
Đăng nhập vào địa chỉ https://hoadondientu.gdt.gov.vn/ , đăng nhập vào tên đăng nhập và mật khẩu đã được cấp qua email và tiến hành lập hóa đơn
Đối với Hóa đơn có giảm thuế GTGT theo Nghi Quyết 43
-	Thành tiền: ghi đầy đủ tiền hàng hóa, dịch vụ trước khi giảm = số tiền doanh thu trên hợp đồng
-	Tổng số tiền thanh toán bằng số: ghi theo số tiền thanh toán đã được giảm thuế = số tiền trên hợp đồng – số thuế GTGT được giảm theo Nghị Quyết 43
-	Ghi chú: đã giảm… (số tiền) tương ứng 20% mức tỷ lệ % để tính thuế giá trị gia tăng theo Nghị quyết số 43/2022/QH15
Lập mới Hóa đơn bán hàng (Hộ kinh doanh phương pháp khoán)
![Ảnh minh họa](images/khoan.jpg)
o	Bước 1: Vào mục Quản lý danh mục Danh mục ký hiệu hóa đơn. Bên góc phải tích chọn Hóa đơn lần phát sinh, loại hóa đơn: hóa đơn bán hàng.
Đặt 2 ký tự cuối cho Ký hiệu hóa đơn, lưu ý: 2 ký tự chữ hoa tùy chọn nhưng phải dùng thống nhất cho các lần xin cấp hóa đơn sau.
o	Bước 2: Chọn Loại hóa đơn: Hóa đơn điện tử bán hàng, nhập các thông tin bắt buộc (*) còn lại.
![Ảnh minh họa](images/khoan1.png)
o	Bước 2: Nhấn Lập hoá đơn hiển thị màn hình Hóa đơn bán hàng bao gồm các chức năng: Xem hóa đơn, Lưu tạm, Trình phê duyệt, Ký gửi, Phê duyệt, Nhập mới, Quay lại.
-	Bước 3: Nhập các thông tin vào hóa đơn
+ Nhấn Xem hóa đơn: Xem trước hóa đơn, hiển thị hóa đơn Giá trị gia tăng bao gồm các thông tin đã nhập
![Ảnh minh họa](images/khoan2.jpg)
Giao diện hóa đơn bán hàng
Nhấn X: để đóng hóa đơn
+	Nhấn Lưu tạm để thực hiện lưu tạm hóa đơn thành công. Hiển thị mẫu hóa đơn Giá trị gia tăng bao gồm chức năng Lập mới hóa đơn điện tử.
+ Nhấn lập mới hóa đơn điện tử: quay trở về màn hình Lập mới hóa đơn.
+	Nhấn Trình phê duyệt  màn hình hiển thị hộp thoại Trình phê duyệt bao gồm danh sách người phê duyệt và chức năng Trình phê duyệt/ Hủy.
![Ảnh minh họa](images/khoan3.png)
o	Chọn người phụ trách
o	Nhấn  Trình phê duyệt thì Hóa đơn được gửi sang tài khoản của người phụ trách phê duyệt. Cổng điện tử thông báo Trình phê duyệt thành công đồng thời hiển thị mẫu hóa đơn Giá trị gia tăng bao gồm chức năng Lập mới hóa đơn điện tử.
o	Nhấn  Huỷ để hủy bỏ thao tác Trình phê duyệt.
+	Nhấn Ký gửi  hiển thị màn hình Thông tin chứng thư để kí số (Hộ Kinh doanh thì không cần kí số)
![Ảnh minh họa](images/khoan4.png)
Chọn Đồng ý , xuất hộp thoại để nhập mã pin
![Ảnh minh họa](images/khoan5.png)
o	Chọn Đăng nhập (Login) -> Hóa đơn được ký gửi thành công
![Ảnh minh họa](images/khoan6.png)
Hóa đơn bán hàng đã ký gửi thành công
o	Nhấn Nhập mới  để Cổng điện tử xóa hết các thông tin đã nhập trước đó để nhập lại mới hóa đơn khác.
o	Nhấn Phê duyệt  để chuyển hóa đơn lên CQT
o	Nhấn Quay lại  để trở về màn hình Lập mới hóa đơn theo lần phát sinh
Đối với Hóa đơn có giảm thuế GTGT theo Nghị quyết số 204/2025/QH15 ngày 17 tháng 6 năm 2025 của Quốc hội về giảm thuế giá trị gia tăng 
-	Thành tiền: ghi đầy đủ tiền hàng hóa, dịch vụ trước khi giảm = số tiền doanh thu trên hợp đồng
-	Tổng số tiền thanh toán bằng số: ghi theo số tiền thanh toán đã được giảm thuế = số tiền trên hợp đồng – số thuế GTGT được giảm theo Nghị Quyết 43
-	Ghi chú: đã giảm… (số tiền) tương ứng 20% mức tỷ lệ % để tính thuế giá trị gia tăng theo Nghị quyết số 204/2025/QH15
---
question: "HƯỚNG DẪN BỔ SUNG CĂN CƯỚC CÔNG DÂN HOẶC THAY ĐỔI NƠI CƯ TRÚ TRÊN TRANG THUEDIENTU.GDT.GOV.VN"
keywords: ["hướng dẫn", "bổ sung", "căn cước công dân", "thay đổi", "nơi cư trú", "web", "thuedientu"]
---
1.	BỔ SUNG CĂN CƯỚC CÔNG DÂN
2.	THAY ĐỔI NƠI CƯ TRÚ
Cần có: thông tin cần bổ sung như ảnh Căn cước công dân (nếu bổ sung CCCD), giấy tờ xác nhận nơi cư trú như hộ khẩu,tạm trú – tạm vắng (nếu cần THAY ĐỔI NƠI CƯ TRÚ)
Các bước thực hiện:
Bước 1: Người nộp thuế đăng nhập vào trang thuedientu.gdt.gov.vn => chọn CÁ NHÂN
![Ảnh minh họa](images/cau8.jpg)

Giao diện hiện ra, chọn đăng nhập
![Ảnh minh họa](images/cau81.jpg)

=> Sau đó, nhập ID là mã số thuế và nhập mã kiểm tra
![Ảnh minh họa](images/cau82.jpg)

Tiếp tục nhập mật khẩu => nhấn Đăng nhập
![Ảnh minh họa](images/cau83.jpg)

Bước 2: Chọn Đăng ký thuế => chọn thay đổi thông tin
![Ảnh minh họa](images/cau84.jpg)

Giao diện hiện ra:
![Ảnh minh họa](images/cau85.jpg)

Kéo xuống dưới cùng, tích vào ô lấy thông tin cá nhân
![Ảnh minh họa](images/cau86.jpg)

Tất cả các thông tin tại mục: Địa chỉ nơi thường trú/Địa chỉ hiện tại sẽ được cập nhật và hiện thị đầy đủ
![Ảnh minh họa](images/cau87.jpg)
![Ảnh minh họa](images/cau88.jpg)

Sau đó, kéo lên trên cùng của trang webside => chọn Tick vào ô thay đổi thông tin (Tại đây, NNT bổ sung thông tin về căn cước công dân). Nếu vẫn không cho sửa thì ta bỏ tick và tick lại lần nữa
![Ảnh minh họa](images/cau89.jpg)

Thực hiện cập nhật thông tin vào các ô bên dưới: Số giấy tờ/Ngày cấp/Nơi cấp
![Ảnh minh họa](images/cau810.jpg)

Tiếp tục, kéo xuống dưới cùng trang webside, có ô Không nhận kết quả tại trụ sở CQT
Lưu ý: Trên tờ khai có nút tích “Không nhận kết quả tại trụ sở CQT”
-	NNT có tích chọn: “Không nhận kết quả tại trụ sở CQT” thì hình thức gửi kết quả là “Qua bưu điện”
-	NNT không có tích chọn: “Không nhận kết quả tại trụ sở CQT” thì hình thức gửi kết quả là “Điện tử”.
![Ảnh minh họa](images/cau811.jpg)

Sau đó, bấm nút tiếp tục
 
Hệ thống sẽ chuyển đến tờ khai điều chỉnh, bổ sung thông tin đăng ký thuế
![Ảnh minh họa](images/cau812.jpg)

NNT kiểm tra kỹ thông tin => Nếu đúng chọn Nộp hồ sơ đăng ký thuế, trong trường hợp muốn in hồ sơ đăng ký thuế thì bấm vào ô in hồ sơ đăng ký thuế
![Ảnh minh họa](images/cau813.jpg)
![Ảnh minh họa](images/cau814.jpg)

NNT kiểm tra kỹ thông tin => Nếu đúng chọn Nộp hồ sơ đăng ký thuế
![Ảnh minh họa](images/cau815.jpg)

NNT cần tải thông tin là ảnh chụp Căn cước công dân (nếu bổ sung CCCD), giấy tờ xác nhận nơi cư trú như hộ khẩu,tạm trú – tạm vắng (nếu cần THAY ĐỔI NƠI CƯ TRÚ)
Ví dụ ở đây thông tin ta cần bổ sung là Căn cước công dân (nếu bổ sung CCCD) => bấm tiếp tục
![Ảnh minh họa](images/cau816.jpg)
![Ảnh minh họa](images/cau817.jpg)

Nhập mã kiểm tra
![Ảnh minh họa](images/cau818.jpg)

Sẽ có 01 mã OTP được gởi về số điện thoại của chủ tài khoản => nhập mã OTP này vào
![Ảnh minh họa](images/cau819.jpg)

Sau khi nhập mã OTP và bấm tiếp tục => hệ thống sẽ báo hồ sơ thay đổi thông tin đăng ký thuế đã được gửi thành công. Vui lòng chờ xử lý!
![Ảnh minh họa](images/cau820.jpg)

Sẽ có thông báo gởi về email và số điện thoại của NNT
![Ảnh minh họa](images/cau821.jpg)

Sau khi gửi thì hồ sơ sẽ ở trạng thái chờ phê duyệt.
Có thể tra cứu thông tin trên mạng để biết đã cập nhật hay chưa Sau 3 ngày làm việc, NNT có thể liên hệ số ĐT 0236.3752167 (Gặp Thanh Xuân) nếu ở địa bàn quận Thanh Khê và số ĐT 0236.3842370 (gặp Thanh Thảo) nếu ở địa bàn quận Liên Chiểu để được hỗ trợ.
---
question: "HKD khoán không thuộc đối tượng HKD bắt buộc sử dụng HĐĐT khởi tạo từ máy tính tiền, cần hóa đơn điện tử đề giao cho khách hàng thì phải làm gì?"
keywords: ["hkd", "đối tượng", "sử dụng", "hoá đơn điện tử", "khách hàng", "", ""]
---
HKD gửi đơn theo mẫu số 06/ĐN-PSĐT Phụ lục 1A ban hành theo NĐ số 70/2025/NĐ-CP đến cơ quan thuế đề nghị cấp HĐĐT có mã của cơ quan
thuế và truy cập vào Cồng thông tin điện tử của Tổng cục Thuế để lập hóa đơn điện tử.
Lưu ý: mức thuế khoán được xác định từ đầu năm không bao gồm doanh thu và thuế do sử dụng hóa đơn. Do vậy, Hộ khoán phải nộp thuế đối với doanh thu phát sinh trên hóa đơn đó theo từng lần phát sinh. Sau khi HKD nộp thuế, cơ quan thuế cấp mã của cơ quan thuế trên hóa
đơn điện tử. Hộ kinh doanh chịu trách nhiệm về tính chính xác của các thông tin trên hóa đơn điện tử theo từng lần phát sinh được cơ quan thuế cấp mã.
Cách xác định cơ quan thuế cấp hóa đơn điện tử có mã của cơ quan thuế theo từng lần phát sinh như sau:
+ HKD có địa điểm kinh doanh cố định: nộp hồ sơ đề nghị cấp hóa đơn điện từ có mã của cơ quan thuế theo từng lần phát sinh tại Thuế cơ sở quản lý nơi hộ, cá nhân kinh doanh tiến hành hoạt động kinh doanh.
- HKD không có địa điểm kinh doanh cố định: nộp hồ sơ đề nghị cấp hóa đơn điện tử có mã của cơ quan thuế theo từng lần phát sinh tại Thuế cơ sở nơi cá nhân cư trú hoặc nơi hộ, cá nhân đăng ký kinh doanh.
HKD có thể tra cứu Thuế cơ sở theo địa bàn quản lý tại QĐ số 1378/QĐ-CT của Cục Thuế ngày 30/06/2025 quy định tên gọi, trụ sở, địa bàn quản lý của các Thuế cơ sở thuộc Thuế tỉnh, thành phố trực thuộc Trung ương.
---
question: "HKD muốn sử dụng hóa đơn điện tử kết nối máy tính tiền cần phải làm gì?"
keywords: ["hkd", "máy tính", "sử dụng", "hoá đơn điện tử", "kết nối", "", ""]
---
Cần chuẩn bị thiết bị cài đặt phần mềm xuất hóa đơn
1.Thiết bị (điện thoại di động, máy tính, máy tính bảng ... ) kết nối internet cài phần mềm tính tiền bán hàng
2. Phần mềm xuất hóa đơn điện tử, chuyển dữ liệu theo thời gian thực đến cơ quan thuế
Cần đăng ký sử dụng hóa đơn khởi tạo từ máy tính tiền với cơ quan thuế
Sau khi đã có thiết bị và phần mềm, HKD cần đăng ký sử dụng hóa đơn khởi tạo từ máy tính tiền với cơ quan thuế
HKD đăng ký và sử dụng HĐĐT khởi tạo từ máy tính tiền theo mẫu số 01/ĐKTĐ-HĐĐT Phụ lục IA ban hành kèm theo Nghị định 123/2020/NĐ-CP ngày 19/10/2020 của Chính phủ.
- Nếu là lần đầu sử dụng HĐĐT và thuộc đối tượng áp dụng HĐĐT có mã của cơ quan thuế khởi tạo từ máy tính tiền thì HKD thực hiện đăng ký qua tổ chức cung cấp dịch vụ hóa đơn điện tử.
- Nếu HKD trước đây đã thực hiện đăng ký sử dụng HĐĐT thành công và muốn đăng ký sử dụng HĐĐT có mã của cơ quan thuế khởi tạo từ máy tính tiền thì thực hiện thay đồi thông tin đăng ký sử dụng HĐĐT qua tổ chức cung cấp dịch vụ hoặc trên trang hoadondientu.gdt.gov.vn
Cá nhân có thể đăng ký và sử dụng chữ ký số miễn phí trên ứng dụng Vneid khi đã kích hoạt tài khoản định danh mức 2
Trên thị trường hiện nay có nhiều phần mềm bán hàng tích hợp xuất hóa đơn điện tử ví dụ có phần mềm chuyên chỉ xuất hóa đơn điện tử không có hoặc rất ít chức năng quản lý bán hàng, có phần mềm giúp quản lý đầy đủ như quản lý hang tồn kho, doanh thu, lợi nhuận, giá vốn, công nợ ... do vậy, HKD cần lựa chọn kỹ loại phần mềm nào phù hợp với nhu cầu, quy mô hoạt động kinh doanh cùa mình.
---
question: "QUY ĐỊNH VỀ HOA ĐƠN ĐIỆN TỬ ĐỐI VỚI HKD"
keywords: ["hkd", "quy định", "", "hoá đơn điện tử", "", "", ""]
---
Hóa đơn điện tử khởi tạo từ máy tính tiền là hóa đơn có mã của cơ quan thuế hoặc dữ liệu điện tử để người mua có thể truy xuất, kê khai thông tin hóa đơn điện tử khởi tạo từ máy tính tiền do tồ chức, cá nhân bán hàng hóa, cung cấp dịch vụ lập từ hệ thống tính tiền, dữ liệu được chuyển đến cơ quan thuế.
Một trong những điểm khác biệt lớn so với hóa đơn điện tử thông thường là hóa đơn từ máy tính tiền không yêu cầu chữ ký số của người bán.
Theo quy định, các khoản chi sử dụng hóa đơn khởi tạo từ máy tính tiền (dù là bản in, bản sao hoặc thông tin tra cứu trên Cồng thông tin của Cục Thuế) vẫn được xác định là chi phí hợp lệ khi kê khai thuế.
Hóa đơn khởi tạo từ máy tính tiền cần đảm bảo các nội dung cơ bản theo quy định, bao gồm:
-Tên, địa chỉ và mã số thuế của người bán.
-Thông tin người mua (nếu người mua yêu cầu) như tên, địa chỉ, mã định danh cá nhân, số điện thoại.
-Tên hàng hóa, dịch vụ; đơn giá; số lượng; giá thanh toán.
- Thời điểm lập hóa đơn.
- Mã của cơ quan thuế hoặc dữ liệu điện tử để người mua có thể truy xuất, kê khai thông tin hóa đơn điện tử khởi tạo từ máy tính tiền.
Người bán gửi hoá đơn điện tử cho người mua bằng hình thức điện tử (tin nhắn, thư điện tử và các hình thức khác) hoặc cung cấp đường dẫn hoặc mã QR đề người mua tra cứu, tải hoa đơn điện tử.
---
question: "Có phải tất cả các HKD bắt buộc phải sử dụng hóa đơn điện tử từ ngày 01/06/2025 không?"
keywords: ["hkd", "sử dụng", "", "01/06/2025", "", "", ""]
---
Không. Từ 01/06/2025, HKD có doanh thu từ 1 tỷ đồng/năm trờ lên, bán hàng hóa, cung cấp dịch vụ trực tiếp cho người tiêu dùng bắt buộc phải áp dụng hóa đơn khởi tạo từ máy tính tiền kết nối truyền dữ liệu với cơ quan thuế.
Hộ kinh doanh thuộc đối tượng phải sử dụng HDĐT khời tạo từ máy tính tiền nhưng không chuyến đổi, đăng ký sử dụng thì được xác định là hành vi vi phạm quy định về sử dụng hóa đơn và HKD có thể bị phạt từ 02-10 triệu đồng
Theo số liệu của cơ quan thuế, tính đến tháng 03/2025 cà nước có khoảng 37.000 hộ kinh doanh có doanh thu trên 1 tỷ đồng thuộc diện bắt buộc sử dụng hóa đơn điện tử, chiếm khoảng 1% trong số hộ kinh doanh đang quản lý
---
question: "HKD phải nộp các loại thuế nào?"
keywords: ["hkd", "thuế", "", "loại", "", "", ""]
---
![Ảnh minh họa](images/thue.png)
---
question: "Hướng dẫn hộ kinh doanh nộp thuế trên ứng dụng etax mobile?"
keywords: ["hkd", "thuế", "hướng dẫn", "ứng dụng", "etax", "nộp", "mobile"]
---
![Ảnh minh họa](images/thue1.png)
---
question: "Quy định về HKD tạm ngừng kinh doannh? Quy định về hkd chấm dứt hoạt động?"
keywords: ["hkd", "ngừng kinh doannh", "chấm dứt", "hoạt động", "", "", ""]
---
![Ảnh minh họa](images/thue2.png)
---
question: "Lợi ích kép cho doanh nghiệp và người tiêu dùng khi Nghị định số 174/2025/NĐ-CP ngày 30/6/2025 của Chính phủ có hiệu lực TỪ NGÀY 01/7/2025 ĐỀN NGÀY 31/12/2026"
keywords: ["lợi ích", "doanh nghiệp", "nghị định", "hiệu lực", "", "", ""]
---
![Ảnh minh họa](images/thue.jpg)

