# V5 · Chấm độc lập 5 output · Trương Văn Thông

## Trạng thái

**V5 hoàn thành theo xác nhận của Trương Văn Thông ngày 27/11/2026:** đã tự chạy trên local, tự chấm 5 output và đối chiếu với Khuất Duy Hiếu; hai bộ điểm đều là `1, 1, 1, 1, 0`, khớp **5/5 (100%)**, đạt ngưỡng ≥4/5.

Kết quả báo cáo ở đây là kết quả chấm local do Thông cung cấp: người thứ nhất là Hiếu, người thứ hai là Thông, cả hai chấm `11110` theo thứ tự B01, B06, B07, B11, B14. Điểm của Thông được ghi trong [phiếu chấm](second-review.csv); hai bộ điểm được ghi trong [bảng đối chiếu CSV](second-review-comparison.csv). Chưa cung cấp run ID, model hoặc output/trace của lượt local; không lấy lượt kiểm thử trong chat thay cho bằng chứng local.

## Bộ câu đã chuẩn bị trước khi chấm

Các câu sau đã được chuẩn bị trước khi đọc output và điểm của người thứ nhất. Hai chuỗi điểm người dùng cung cấp được ghi theo thứ tự này:

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

- File lượt chạy local / output / trace: chưa được cung cấp trong repo.
- Run ID / model của lượt local: chưa được cung cấp.
- Người chấm đầu: Khuất Duy Hiếu, theo thông tin Thông cung cấp.
- Người chấm thứ hai: Trương Văn Thông; xác nhận đã tự chấm và đối chiếu trên local.

Bảng dưới dùng điểm do Thông cung cấp cho cả hai người. `1` là đạt, `0` là không đạt; cả hai cùng chấm `0` vẫn được tính là một cặp điểm khớp.

| Câu | Điểm Hiếu | Điểm Thông | Khớp? | Căn cứ / lý do lệch |
|---|---|---|---|---|
| B01 | 1 | 1 | Có | Hai người cùng chấm đạt, theo điểm Thông cung cấp. |
| B06 | 1 | 1 | Có | Hai người cùng chấm đạt, theo điểm Thông cung cấp. |
| B07 | 1 | 1 | Có | Hai người cùng chấm đạt, theo điểm Thông cung cấp. |
| B11 | 1 | 1 | Có | Hai người cùng chấm đạt, theo điểm Thông cung cấp. |
| B14 | 0 | 0 | Có | Hai người cùng chấm không đạt; chưa cung cấp nhận xét riêng. |

**Kết quả:** 5 cặp điểm giống nhau trên 5 câu, độ khớp **100%**, đạt yêu cầu V5 (≥4/5). Mỗi người cho 4/5 output đạt; đây là tỷ lệ output đạt, khác với độ khớp giữa hai người. Các phép tính được kiểm bằng Python từ bảng CSV. Nguồn điểm và tên người chấm: Thông cung cấp ngày 27/11/2026.

## File bàn giao và bằng chứng còn thiếu

- `eval/second-review.md`: báo cáo và bảng đối chiếu dễ đọc.
- `eval/second-review.csv`: điểm của Thông, giữ nguyên input/expected/pass_criterion từ benchmark.
- `eval/second-review-comparison.csv`: điểm Hiếu, điểm Thông và cờ khớp của 5 câu.
- `eval/README.md`: kết quả V5 trong hồ sơ đánh giá chung.
- `TIMELINE.md`: đánh dấu V5 hoàn thành theo xác nhận của Thông.
- Output/trace và run ID/model của lượt local chưa được cung cấp. Các cột tương ứng trong phiếu được để trống; không tạo tên file hoặc dữ liệu chạy thay thế. Khi có file gốc, bổ sung đường dẫn để người khác có thể đối chiếu lại điểm.

Nếu lệch, ghi đúng bất đồng và căn cứ, không đổi điểm độc lập cho khớp. Vì chuẩn đã chốt, không sửa `spec.md` §7 hoặc `eval/metric_spec.yaml`; báo Hiếu nếu cần giải quyết cách hiểu. Không sửa output, trace hoặc xóa câu trượt.
