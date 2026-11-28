# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ 1.000 review 1★, 7 ví dụ. Người kiểm khớp 87/100 trong mẫu phân tầng (mục 3b) | [Cách đếm và kiểm nhãn](data-mining.md) |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ **3/3** người ngoài nhóm (P1, P2, P3). P4 là thành viên nhóm nên không tính | `evidence/interviews/P1.md`, `P2.md`, `P3.md`, `P4.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ **tạm**: 34 phản hồi, 33 người dùng ví / thẻ (bản xuất 18:10 27/11). **30 người hỏi miệng, 4 người tự điền** (xem cách thu ở `questions.md`). Số chốt 09:30 28/11. ⚠ còn kiểm: có thành viên nhóm không, câu 11 trùng ở dòng 26/30 | `evidence/survey/results.csv`, `count.py` |

## 2. Số chính

- Đào data (review 1★ MoMo + ZaloPay, Google Play, 18/10–26/11/2026): khoản trừ tự động **147/1000 (14,7%)** — ZaloPay 110/500 (22,0%), MoMo 37/500 (7,4%); trong 147: không biết ai trừ **57 (38,8%)**, đã liên hệ không xong 26 (17,7%), trách nhầm ví 22 (15,0%). So sánh: giao dịch lỗi 167/1000, lỗi kỹ thuật 387/1000. Người kiểm khớp **87/100** trong mẫu phân tầng (28/33 gói đăng ký ẩn, 28/30 tự trừ không rõ, 31/37 nhãn khác). Người kiểm từng thấy nhãn trong lần thử, nên độ khớp có thể cao hơn so với lượt kiểm hoàn toàn độc lập.
- Phỏng vấn (ngoài nhóm): **3/3** người kể được một lần cụ thể · P1 ~2 lần / 6 tháng, P2 ~2–3 lần / tháng, P3 1 lần trong tháng · mỗi lần mất **~10–15 phút** để tìm ra khoản gì / chỗ huỷ · P1 phát hiện sau ~2 tuần (250k, không đòi lại được), P2 bị trừ 2 kỳ (~99k / kỳ) mới phát hiện, P3 thấy "Google Play" trên thông báo ví (59k) nhưng không biết app nào, phải tra email.
- Khảo sát (**tạm**, n = 33 người dùng ví / thẻ, `python evidence/survey/count.py`):
  - Câu 4: **21/33 (64%)** có ≥1 lần trong 3 tháng thấy khoản trừ tự động không nhận ra (hỏi miệng 18/29 · tự điền 3/4).
  - Trong 21 người đó: **14/21** phát hiện sau ≥1 tuần **hoặc** mất ≥15 phút (sau ≥1 tuần 7/21 · mất ≥15 phút 10/21). **Cả 14 người đều thuộc nhóm hỏi miệng**, 3 người tự điền đều phát hiện ngay và mất 5–15 phút.
  - Câu 5: dùng thử chuyển sang trả phí 8 · gói tự gia hạn quên 6 · dịch vụ không nhớ đã đăng ký 3 · giao dịch lỗi 2 · phí ví 1 · vẫn không biết 1.
  - Câu 9: phần lớn 50k–500k (17/21), 1 người trên 500k.
  - Câu 10: **23/33** không biết hoặc chỉ biết một phần ngày bị trừ tiếp theo.
  - Hạn chế: 30/34 phản hồi là hỏi miệng, người hỏi là thành viên nhóm, mẫu là người quen / ngồi gần.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | người dùng MoMo + thẻ Visa | có (qua thẻ, biết app nhưng quên ngày và khó huỷ) | ~2 lần / 6 tháng | ~15 phút tìm chỗ huỷ, phát hiện sau ~2 tuần | không có cách nhắc |
| P2 | nhân viên văn phòng dùng MoMo | có (tên trên lịch sử khó hiểu) | ~2–3 lần | ~15 phút tra Google + email | tự kiểm lịch sử và gói đăng ký |
| P3 | người dùng ZaloPay có liên kết Google Play | có (biết kênh Google Play, không biết app nào) | 1 lần | ~10 phút tra email + Gói thuê bao Google Play | đợi thông báo ví rồi mới kiểm |
| P4 | thành viên nhóm (không tính) | chưa đủ dữ liệu | chưa cung cấp | chưa cung cấp | vào app kiểm tra |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Mình đăng ký dùng thử miễn phí Alarmy, nhưng sau khi hết hạn, thẻ ngân hàng bị trừ 1.086.667 đồng. Mình đã cố gắng hủy nhưng không tìm thấy gói thuê bao trên Google Play." — review `zalopay-340`, 27/10/2026, 1★
2. "cái đăng ký thì lôi ở đâu ra từ ngày 19/05/2026 rồi trừ tiền của mình vào 16/11/2026 hỏi thì không đc." — review `zalopay-089`, 18/11/2026, 1★
3. "hệ thống trừ tiền lung tung mã google từ đâu xuất hiện trừ hơn 543k…" — review `momo-147`, 12/11/2026, 1★
4. "quên tắt thành toán tự động nó tự thành toán xg muốn hoàn tiền nhắn mãi bên Zalopay mãi k rep" — review `zalopay-001`, 25/11/2026, 1★
5. "tự trừ tiền khi không đăng kí" — review `zalopay-209`, 08/11/2026, 1★
6. "Mình lên Google tìm tên giao dịch và kiểm tra email. Mất khoảng 15 phút mới biết đó là khoản gia hạn ứng dụng" — phỏng vấn `P2`, 27/11
7. "Lúc bị trừ thì mình không để ý tin nhắn, tầm 2 tuần sau kiểm tra lại sao kê thẻ mới phát hiện ra." — phỏng vấn `P1`, 27/11
8. "Bị trừ gói dùng thử app hết hạn, thấy tin nhắn trừ tiền mới biết, khó chịu vì không báo trước." — khảo sát câu 11, dòng 4 (`hoi_mieng`)
9. "Mình liên kết tới khá nhiều các dịch vụ thanh toán tự động nên khá dễ quên phải đến khi trừ rồi mới biết và note lại" — khảo sát câu 11, dòng 29 (`tu_dien`)

Thêm 2 ví dụ: `evidence/data-mining.md` mục 4.

## 4. Các nguồn có khớp nhau không

*(tạm, 18:15 27/11)* **Data** (review): khoản trừ tự động là 14,7% review 1★, và 38,8% trong số đó không biết ai trừ. **Khảo sát tạm:** 21/33 người dùng ví hoặc thẻ trong mẫu từng gặp khoản trừ không nhận ra (64%), chủ yếu do dùng thử chuyển sang trả phí hoặc gói tự gia hạn (17/21), đúng loại pain lát cắt nhắm tới.

**Khớp:** loại khoản (gói đăng ký / dùng thử) và việc mất thời gian tìm chỗ huỷ (P1, P2 đều ~15 phút).
**Lệch:** 12/21 người trong khảo sát phát hiện **ngay hôm đó**, vì có tin nhắn trừ tiền. Vướng nhiều hơn ở chỗ **không được báo trước** và **không biết ngày trừ tiếp** (23/33), hơn là ở chỗ phát hiện muộn. P1 biết là app nào, chỉ quên ngày và khó huỷ. Khoản của P1 trừ qua thẻ Visa, không qua ví. Gợi ý: giữ phần **cảnh báo trước kỳ trừ** làm lõi; phần "xác định dịch vụ" quan trọng với nhóm "không biết ai trừ" trong review.

## 5. Kết luận

Hồ sơ CP3 dùng bộ review đã kiểm nhãn làm nguồn đạt ngưỡng và dùng phỏng vấn để đối chiếu. Các kết luận về tỷ lệ và bảng impact dựa trên bản khảo sát tạm ngày 27/11. Tính lại khi có bản xuất chốt E4.

Giả thuyết ở `evidence/hypothesis.md` trong mẫu khảo sát tạm:
- **H1 đúng** (64%, ngưỡng ≥25%).
- **H2 đúng nhưng yếu** (14/21, ngưỡng ≥50%): toàn bộ đến từ nhóm hỏi miệng, và vế "mất ≥15 phút" đóng góp nhiều hơn vế "phát hiện muộn".
- **H3 đúng** (17 so với 2).
- Phỏng vấn: 3/3 người ngoài nhóm kể được một lần cụ thể. P2 và P3 không nhận ra ngay khoản trừ là app nào (đúng phần "xác định dịch vụ"); P1 biết app nhưng quên ngày trừ và khó huỷ. Cả 3 đều chỉ biết **sau khi** đã bị trừ (đúng phần "cảnh báo trước kỳ trừ").

**Điều vẫn chưa biết:** số tự điền còn ít (n=4), cần thêm ≥10 người tự điền để so với nhóm hỏi miệng. Chưa biết bao nhiêu người thật sự "không nhận ra dịch vụ" so với "biết dịch vụ nhưng quên ngày".

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |
