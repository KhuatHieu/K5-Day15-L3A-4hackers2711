# Chi phí khi dùng thật

> Báo cáo do `python cost/build_estimate.py cost/simulate-1.csv` tạo từ CSV thật và cấu hình hiện tại.
> Chưa thay thế kết quả CP4 với đúng model và tỉ lệ đạt lượt 2.

## 1. Đầu vào và giả định

- Model thực đo: `gemini-3.1-flash-lite`; seed 42; 50 phiên, mỗi phiên một lượt hỏi.
- Đầu vào được lấy mẫu từ benchmark loại `thuong` và `kho`, không phải lưu lượng khách hàng thật. Phiên được code xử lý mà không cần AI có chi phí model bằng 0; phiên cần nhiều lần gọi được cộng đủ usage. Trung bình bỏ phiên lỗi theo khung, còn tổng usage bên dưới giữ cả phần đo được trong phiên lỗi.
- Persona từ khảo sát tạm, câu 4: ít 12/33 (gộp 0 và không nhớ), vừa 13/33, nhiều 8/33. Câu 3: 23 Có, 5 Không, 5 Không chắc liên kết tự động.
- Tần suất 1/4/12 phiên/người/tháng **(tự ước tính)**; khảo sát chưa đo nhu cầu dùng sản phẩm. Chưa chốt mẫu ngoài nhóm và hai dòng trùng.
- MoMo công bố hơn 30 triệu người dùng: [thông cáo MoMo](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-dong-hanh-ngay-tai-chinh-so-2026-khang-dinh-8835), xem 27/11/2026. Lấy nền 30 triệu, giả định tiếp cận 0,01% / 0,1% / 1% → 3.000 / 30.000 / 300.000 lượt **(tự ước tính)**. Không phải khách hàng đã có; không cộng ZaloPay.
- Giá [Google Standard trả phí](https://ai.google.dev/gemini-api/docs/pricing), xem 27/11/2026: Flash-Lite $0,25 vào / $1,50 ra; Pro Preview $2 vào / $12 ra trên một triệu token (prompt ≤200k). Token ra gồm thinking. Pro chỉ so sánh giá trên token Flash-Lite, chưa chạy Pro để đo token hoặc chất lượng.
- Chỉ báo cáo bằng **USD**, không quy đổi tiền Việt. Chỉ tính tiền model; chưa gồm hosting, lưu trữ, gửi cảnh báo, thuế và công người duyệt.

## 2. Kết quả đo và bảng do khung sinh

- Run ID: `simulate-1@20261127-215058`. CSV: [simulate-1.csv](simulate-1.csv); trace: [simulate-1.jsonl](../traces/simulate-1.jsonl).
- Phiên không lỗi API: **49/50**; phiên lỗi: **1/50**. Đây là khả năng chạy, không phải tỉ lệ đạt chất lượng.
- Tổng usage tất cả phiên (kể cả phần gọi thành công trong phiên lỗi): **15941 token vào, 1390 token ra**; quy theo giá trả phí Flash-Lite: **$0.0061**. Request lỗi không trả usage nên chưa biết có phát sinh tiền ngoài phần đo được hay không.
- Trung bình mỗi phiên không lỗi: **$0.00012**. Chi phí trên là quy đổi theo bảng giá, không phải hoá đơn thực tế nếu đang dùng free tier.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (3.000 người) | Chi phí / tháng — cơ sở (30.000 người) | Chi phí / tháng — cao (300.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00012 | — | — | $1.97 | $19.68 | $196.78 | $0.00066 |
| gemini-3.1-pro-preview (vào 2.0 · ra 12.0 $/1M) | $0.00099 | — | — | $15.74 | $157.42 | $1,574.22 | $0.0052 |

### Phép tính K1 chi tiết (USD)

Giá Flash-Lite: USD vào = token vào × 0.25 / 1.000.000; USD ra = token ra × 1.5 / 1.000.000; chi phí phiên = USD vào + USD ra.

- Toàn bộ 50 phiên: tiền token vào **$0.00398525**, tiền token ra **$0.002085**, tổng **$0.00607025**.
- 49 phiên không lỗi API có tổng **$0.00607025** → trung bình **$0.0001238827 / phiên**.
- Trung bình trên mọi phiên, kể cả lỗi: **$0.000121405 / lượt thử**. Phiên timeout không trả usage không được coi là miễn phí đã xác nhận; đây chỉ là phần token đo được.
- Đã đối chiếu tổng token và run ID giữa CSV với trace; có 50 mã phiên duy nhất. Bảng [chi phí từng phiên](session-costs-simulate-1.csv) có đủ 50 dòng, gồm phiên lỗi.

| Nhóm | Phiên không lỗi / tổng | Token vào / ra (phiên không lỗi) | Tổng USD không lỗi | USD / phiên không lỗi | Tỉ lệ người | Phiên/người/tháng (tự ước tính) |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22/23 | 6022 / 524 | $0.0022915 | $0.0001041591 | 36.363636% | 1 |
| dung_vua | 18/18 | 6748 / 582 | $0.00256 | $0.0001422222 | 39.393939% | 4 |
| dung_nhieu | 9/9 | 3171 / 284 | $0.00121875 | $0.0001354167 | 24.242424% | 12 |

Công thức cho mỗi kịch bản và nhóm j:

```text
Người nhóm j = tổng người × share_j / tổng share
Phiên nhóm j/tháng = người nhóm j × phiên/người/tháng_j
USD nhóm j/tháng = phiên nhóm j/tháng × USD/phiên không lỗi_j
USD toàn kịch bản/tháng = tổng USD nhóm j/tháng
```

Tỉ lệ persona được giữ nguyên giữa ba quy mô. Các số người và phiên lẻ là kỳ vọng của mô hình, không phải đếm người thực tế. Không nhân chi phí bình quân chung với tần suất chung, vì từng nhóm có chi phí/phiên khác nhau.

| Kịch bản | Người (tự ước tính) | Phiên/tháng kỳ vọng (tự ước tính) | USD ít | USD vừa | USD nhiều | Tổng USD/tháng Flash-Lite | Tính giá Pro trên cùng token |
|---|---:|---:|---:|---:|---:|---:|---:|
| thấp | 3000 | 14545.454545 | $0.1136280992 | $0.6723232323 | $1.1818181818 | **$1.9677695133** | $15.7421561065 |
| cơ sở | 30000 | 145454.545455 | $1.1362809917 | $6.7232323232 | $11.8181818182 | **$19.6776951331** | $157.4215610652 |
| cao | 300000 | 1454545.454545 | $11.3628099174 | $67.2323232323 | $118.1818181818 | **$196.7769513315** | $1574.215610652 |

Bảng [phân rã kịch bản](scenario-costs-simulate-1.csv) giữ đầy đủ số trước làm tròn. Pro có cả hai đơn giá bằng 8 lần Flash-Lite nên cột so sánh bằng chi phí Flash-Lite × 8; đây không phải chi phí Pro đã đo.

**K1 hoàn thành:** đã mô phỏng ít nhất 50 phiên, lưu CSV và trace, tính chi phí bằng usage API, có ba kịch bản quy mô và phép tính tái lập. Chi phí/task thành công phụ thuộc eval lượt 2 cùng model ở K4, chưa thể dùng số phiên không lỗi API làm tỉ lệ đạt chất lượng.

## 3. Độ nhạy và so với impact

Chi phí/task thành công = chi phí/phiên ÷ tỉ lệ đạt cùng model. Chưa có eval đã chấm cho Flash-Lite; không dùng 18/20 của gpt-6.2-sol. Bảng dưới chỉ là giả định **(tự ước tính)**, chưa gồm retry:

| Tỉ lệ đạt giả định | Chi phí / task thành công Flash-Lite |
|---|---:|
| 70% | $0.00018 |
| 90% | $0.00014 |
| 100% | $0.00012 |

- Chi phí model / người / tháng theo persona: **$0.00066**. Nếu toàn bộ tần suất giả định tăng gấp đôi, chi phí tháng cũng tăng gấp đôi.
- Impact tạm tham chiếu `spec.md` §2, chưa quy đổi tiền tệ để so sánh trực tiếp. Đây là tổn thất ước tính từ khảo sát, không phải số tiền sản phẩm chắc chắn tiết kiệm được.
- **Đáng thử tiếp về tiền model** vì chi phí model / phiên thấp; chưa kết luận hiệu quả kinh doanh trước khi có chất lượng cùng model, chi phí vận hành và dữ liệu khảo sát chốt. Các lỗi quota có thể làm người dùng lỡ cảnh báo.

## 4. K0 và cách chạy lại

K0: `simulate-try@20261127-214818`, 10 phiên, 8 không lỗi và 2 lỗi HTTP 429. Usage tổng 7.798 vào / 685 ra; xem [bằng chứng K0](k0-check.json). K0 dùng cấu hình cũ 1/3/5 lượt, chỉ kiểm luồng; bảng chính dùng lượt đầy đủ một lượt/phiên.

```powershell
$env:MODEL_NAME = 'gemini-3.1-flash-lite'
python run.py check
python run.py simulate --wait 4
python cost/build_estimate.py cost/simulate-N.csv
```

Giữ đúng cấu hình `cost/personas.yaml` khi tái lập báo cáo của lượt này. Không chạy lại `--try` nếu muốn giữ nguyên file thử cũ. Lượt đủ tiếp theo tự tăng số N. Không sửa file CSV/trace đã chạy; log lỗi trước đó giữ riêng và được gitignore. Bản summary gốc có quy đổi tiền Việt do cấu hình tại thời điểm chạy; báo cáo này chỉ bỏ phần hiển thị quy đổi theo yêu cầu, không sửa dữ liệu đo hay giá USD.

- SHA-256 CSV: `dbfa4e9619773f6cace3f9182b43c4853b63a9a46bacefb6ed677f8c01581d1f`.
- SHA-256 personas.yaml: `6b8c825d409ec8f5d75b7ce7f9a8254d5c0ac426f503dadfe04acb6378fd0bf4`.
