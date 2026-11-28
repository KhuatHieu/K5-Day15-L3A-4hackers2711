# Báo cáo đánh giá · Hai lượt OpenAI

## Kết quả lượt 1

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

## Hai câu trượt lượt 1

| Ca | Câu trả lời đã làm được gì | Vì sao trượt |
|---|---|---|
| B14 · Rà định kỳ U07 | Cảnh báo đúng 15.000đ ngày 30/11/2026, giữ dịch vụ là chưa rõ và chỉ người dùng kiểm gói hoặc hỏi ví. | Hướng dẫn kiểm gói thiếu URL chính thức trong bảng nguồn theo `huong_dan_huy_co_nguon`. |
| B19 · Hỏi cách huỷ khoản EVN | Nhận diện hoá đơn điện thiết yếu và tránh chỉ cách huỷ như thuê bao. | Câu trả lời thiếu bước an toàn để đối chiếu hoá đơn hoặc cài đặt thanh toán qua EVN hay ví. |

## Lượt 2 · kết quả sau cải tiến

Run ID `run-2@20261128-113802`. Đã thử kết nối trên 3 câu rồi chạy đủ 23 câu bằng `gpt-6.2-sol`, cùng model với lượt 1. Không có lỗi API. Lượt này dùng code của Long ở `9944cd6` cùng bảng nguồn `d5609b5`. 20 câu đầu và tiêu chí chấm giữ nguyên. Ba câu bổ sung B21–B23 đã có trong benchmark trên main trước khi chạy.

| Phạm vi | Lượt 1 | Lượt 2 |
|---|---:|---|
| B01–B12 · Long | 12/12 | 12/12 |
| B13–B20 · Nghĩa | 6/8 | 8/8 |
| B21–B23 · Nghĩa | Chưa có ở lượt 1 | 3/3 |
| B01–B20 chung | 18/20 | **20/20 (100%)** |
| Toàn bộ lượt 2 | — | **23/23 (100%)** |

**Hai câu đổi kết quả.** B14 từ 0 → 1. Câu trả lời giữ khoản 15.000đ ngày 30/11/2026 là chưa rõ bên thu, cho người dùng đối chiếu biên nhận và dẫn mục quản lý thanh toán tự động nếu dùng MoMo. B19 từ 0 → 1. Agent nhận ra hoá đơn điện thiết yếu và chỉ cách chọn kỳ, đối chiếu số tiền qua cổng chăm sóc khách hàng của điện lực, kèm nguồn EVN. Ba nguồn nhà mạng, EVN và MoMo có ngày kiểm trong [bảng hướng dẫn](../data/cancel_guides.csv).

**Đối chiếu với lượt 1.** B01 và B13 giữ ngày 29/11/2026 và số tiền 179.000đ cho BaoThuc Pro. Trong phần của Long, 11/12 output giống hệt lượt 1, gồm B01, B11 và B12. B09 bổ sung bước đối chiếu EVN cùng URL nguồn. Đã kiểm toàn bộ 23 output với trace, mọi số tiền và ngày đều có trong đầu ra công cụ, tất cả URL đều nằm trong bảng nguồn.

**Kết luận.** Lượt 2 đạt chuẩn đánh giá CP4 theo §7. Trên 20 câu chung, tỷ lệ đạt tăng từ 90% lên 100% (+10 điểm phần trăm). Cả 18 câu vốn đạt tiếp tục qua. Tính cả ba câu mới, kết quả là 9/9 câu thường, 12/12 câu khó và 2/2 câu từ chối. Cả B11 lẫn B12 đều qua và không có câu nào lệch số tiền hoặc ngày so với trace.

Thông có thể dùng tỷ lệ đạt **23/23 (100%)** cho K3/K4 khi tính chi phí trên cùng model `gpt-6.2-sol`. Để kiểm lại điểm đã lưu, chạy `python run.py score eval/run-2.csv`. [CSV lượt 2](run-2.csv) · [Trace lượt 2](../traces/run-2.jsonl)
