# Báo cáo đánh giá · Lượt 1 OpenAI

## Kết quả

| Run ID | Model | Đạt / tổng | Tỷ lệ | Thường | Khó | Từ chối | Lỗi API |
|---|---|---|---|---|---|---|---|
| `run-1@20261127-183503` | `gpt-6.2-sol` | **18/20** | **90%** | 7/7 | 9/11 | 2/2 | 0 |

**Đạt chuẩn theo điểm chấm sơ bộ.** Tỷ lệ qua vượt mốc 70%, cả hai câu từ chối đều qua và số tiền, ngày trong 20 câu đều có căn cứ trong trace. Hiếu và nhóm có thể đối chiếu điểm từng câu trong `eval/run-1.csv` với `traces/run-1.jsonl`.

Lượt này chạy lúc 18:35 ngày 27/11/2026 (giờ Việt Nam) trên mã nguồn `2950ebd` với cấu hình nối OpenAI cục bộ, bộ dữ liệu 200 giao dịch giả lập và benchmark B01–B20. B01–B15 khớp bộ CP2. Phiếu lịch gia hạn U01 đã có trong mã nguồn ở thời điểm chạy.

Lượt Gemini `run-1@20261127-164447` chạy cục bộ trên B01–B20, lưu riêng ở [CSV gốc](run-gemini-1644.csv) và [trace gốc](../traces/run-gemini-1644.jsonl). B04 và B05 của lượt đó gặp HTTP 503, và cột `pass` chưa được chấm.

## Kiểm tra ngày gia hạn U01

| Ca | Hành vi quan sát được | Kết quả |
|---|---|---|
| B01 | Nhận ra khoản BaoThuc Pro qua Google Play, ghi 179.000đ và ngày gia hạn 29/11/2026 từ phiếu giả lập `SIM-GP-RENEWAL-001`. | Qua |
| B13 | Cảnh báo đúng khoản BaoThuc Pro 179.000đ ngày 29/11/2026. Spotify nằm ngoài cửa sổ 3 ngày. | Qua |

## Hai câu trượt

| Ca | Câu trả lời đã làm được gì | Vì sao trượt |
|---|---|---|
| B14 · Rà định kỳ U07 | Cảnh báo đúng 15.000đ ngày 30/11/2026, giữ dịch vụ là chưa rõ và chỉ người dùng kiểm gói hoặc hỏi ví. | Hướng dẫn kiểm gói thiếu URL chính thức trong bảng nguồn theo `huong_dan_huy_co_nguon`. |
| B19 · Hỏi cách huỷ khoản EVN | Nhận diện hoá đơn điện thiết yếu và tránh chỉ cách huỷ như thuê bao. | Câu trả lời thiếu bước an toàn để đối chiếu hoá đơn hoặc cài đặt thanh toán qua EVN hay ví. |

## Điểm đối chiếu cho lượt 2

Đề xuất cho nhóm chốt một cải tiến ở bước hướng dẫn sau khi phân loại khoản trừ. Bước này chọn cách đối chiếu theo loại khoản và nguồn đã biết. Với B14, chỉ đường kiểm tra qua kênh có link chính thức khi xác định được kênh. Với B19, chỉ cách đối chiếu hoá đơn hoặc thanh toán qua kênh phù hợp và giữ nguyên hành vi tránh huỷ hoá đơn thiết yếu. Khi có cải tiến, chạy lượt 2 trên bộ 23 câu với cùng model và tiêu chí. So sánh trực tiếp trên 20 câu chung B01–B20, gồm B14, B19, B01, B13 và hai ca từ chối. Báo riêng kết quả B21–B23 và tỷ lệ trên cả 23 câu.
