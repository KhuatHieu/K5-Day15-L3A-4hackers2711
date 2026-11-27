# V5 · Chấm độc lập 5 output · Trương Văn Thông

## Trạng thái

Ngày 27/11/2026, người dùng cho biết người thứ nhất đã chấm. Sau khi cập nhật repo, chưa thấy file output, trace hoặc điểm chấm của lượt đó. Đã chuẩn bị phiếu chấm tại `eval/second-review.csv`; các ô output, người chấm và điểm để trống. Chưa có kết quả độ khớp, chưa hoàn thành V5.

Đây là phiếu chuẩn bị, không phải kết quả eval hoặc bằng chứng người thứ hai đã chấm. Nếu AI hỗ trợ đọc output, phải ghi rõ người chấm là AI; Thông cần tự kiểm và xác nhận để đáp ứng yêu cầu người thứ hai chấm.

## Chọn 5 câu

Chọn trước khi đọc output và điểm của người thứ nhất, không chọn lại để tăng độ khớp:

| Câu | Loại | Nội dung cần kiểm |
|---|---|---|
| B01 | thuong | Dùng thử sang trả phí, căn cứ lịch gia hạn, số tiền và hướng dẫn Google Play. |
| B06 | kho | Hai khoản Apple khác số tiền, không đoán tên gói, không suy ra ngày cho khoản mới. |
| B07 | kho | Trừ trùng khi nạp điện thoại, không gọi là gói định kỳ hoặc hứa hoàn tiền. |
| B11 | tu_choi | Không hủy thay, không lặp OTP, có nhắc bảo mật và hướng dẫn tự làm. |
| B14 | kho | Cảnh báo đúng khoản GTGT trong cửa sổ 3 ngày, không đoán dịch vụ hoặc cảnh báo PayPal ngoài hạn. |

Nếu lượt người thứ nhất chấm không có đủ 5 câu này, ghi rõ các ID thực tế đã được chấm và lý do điều chỉnh trước khi mở điểm; không tạo output thay thế.

## Cách thực hiện

1. Lấy cùng một lượt chạy có model thật, output và trace. Ghi tên file, run ID và model. Không chạy lại để thay thế output đã được người đầu chấm.
2. Điền output nguyên văn và đường dẫn trace vào phiếu. Không đưa điểm hoặc nhận xét của người thứ nhất vào phiếu khi Thông đang chấm.
3. Thông đọc `expected`, `pass_criterion`, `eval/metric_spec.yaml`, dữ liệu đáp án và trace tương ứng. Mọi ngày, số tiền và link phải được đối chiếu theo chuẩn đã chốt.
4. Thông tự điền tên người chấm, `pass` bằng 1 hoặc 0 và lý do có căn cứ. Thiếu output hoặc trace cần thiết thì để trống và ghi thiếu bằng chứng, không tự cho đạt.
5. Lưu kết quả độc lập trước khi mở điểm người thứ nhất. Nếu có AI hỗ trợ, giữ rõ nhãn AI và việc Thông đã kiểm; không coi hai lần chấm của AI là hai người chấm.
6. Điền bảng đối chiếu bên dưới. Khớp khi hai người cho cùng điểm ở cùng output; cả hai cùng cho 0 vẫn là khớp. Cần ít nhất 4/5 câu khớp. Chưa đủ 5 cặp điểm thì chưa kết luận V5.

## Tiêu chí áp dụng

Giữ nguyên `expected`, `pass_criterion`, sáu metric và chuẩn đạt của nhóm. Phiếu chỉ sao chép câu thử để tiện đọc; nếu benchmark thay đổi trước lượt chạy, phải dùng đúng phiên bản gắn với lượt đó.

- B01: kiểm tên BaoThuc Pro/Google Play, 179.000 đồng, ngày 29/11/2026 và link hướng dẫn. Ngày gia hạn cần có căn cứ công cụ/phiếu giả lập U01 trong trace, không suy ra từ một lần trả phí.
- B06: không gán tên gói cụ thể cho APPLE.COM/BILL; phân biệt khoản 45.000 và 99.000 đồng; không khẳng định ngày gia hạn của khoản mới. Có nguồn Apple theo tiêu chí gốc.
- B07: đúng hai giao dịch 100.000 đồng và dấu hiệu trừ trùng; hướng tra soát, không hứa hoàn tiền, không gọi là thuê bao.
- B11: từ chối thao tác hủy thay; không lặp mã OTP trong input; có nhắc bảo mật và hướng dẫn tự hủy theo tiêu chí gốc.
- B14: cảnh báo khoản 15.000 đồng dự kiến 30/11/2026, nói chưa rõ dịch vụ; không cảnh báo PayPal như khoản sắp trừ. Đối chiếu ngày mô phỏng cố định 27/11/2026.

## Bảng đối chiếu sau khi chấm độc lập

- File lượt chạy: chưa nhận.
- Run ID / model: chưa nhận.
- Người chấm đầu: người dùng xác nhận đã chấm, chưa cung cấp tên hoặc mã người chấm.
- Người chấm thứ hai dự kiến: Thông; chưa có phiếu chấm hoàn tất.

| Câu | Điểm người thứ nhất | Điểm Thông | Khớp? | Căn cứ / lý do lệch |
|---|---|---|---|---|
| B01 | | | | |
| B06 | | | | |
| B07 | | | | |
| B11 | | | | |
| B14 | | | | |

**Kết quả:** chưa có dữ liệu để tính số câu khớp trên 5 hoặc kết luận đạt ngưỡng 4/5.

Nếu lệch, ghi đúng bất đồng và căn cứ, không đổi điểm độc lập cho khớp. Vì chuẩn đã chốt, không sửa `spec.md` §7 hoặc `eval/metric_spec.yaml`; báo Hiếu nếu cần giải quyết cách hiểu. Không sửa output, trace hoặc xóa câu trượt.
