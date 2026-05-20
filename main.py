import csv
import os
os.makedirs("data/raw", exist_ok=True)

stocks = [
    {"date": "2026-05-01", "ticker": "005930", "name": "삼성전자", "close": 70000, "volume": 1200000},
    {"date": "2026-05-02", "ticker": "005930", "name": "삼성전자", "close": 72000, "volume": 1350000},
    {"date": "2026-05-03", "ticker": "005930", "name": "삼성전자", "close": 71000, "volume": 980000}
]

with open("data/raw/samsung_prices.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["date", "ticker", "name", "close", "volume"]
    )

    writer.writeheader()
    writer.writerows(stocks)

print("주가 CSV 저장 완료")
import csv

stocks = []

with open("data/raw/samsung_prices.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stock = {
            "date": row["date"],
            "ticker": row["ticker"],
            "name": row["name"],
            "close": int(row["close"]),
            "volume": int(row["volume"])
        }

        stocks.append(stock)

print(stocks)
total_close = 0
max_close = stocks[0]["close"]
min_close = stocks[0]["close"]

for stock in stocks:
    close = stock["close"]

    total_close += close

    if close > max_close:
        max_close = close

    if close < min_close:
        min_close = close

average_close = total_close / len(stocks)

print(f"평균 종가: {average_close:,.0f}원")
print(f"최고 종가: {max_close:,}원")
print(f"최저 종가: {min_close:,}원")
import json
import os

os.makedirs("reports", exist_ok=True)

summary = {
    "ticker": "005930",
    "name": "삼성전자",
    "average_close": round(average_close, 2),
    "max_close": max_close,
    "min_close": min_close,
    "data_count": len(stocks)
}

with open("reports/samsung_summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=4)

print("분석 요약 JSON 저장 완료")
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("logs/run_log.txt", "a", encoding="utf-8") as file:
    file.write(f"[{now}] 삼성전자 데이터 {len(stocks)}건 분석 완료\n")

print("로그 저장 완료")
import pandas as pd

students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "영희", "score": 55}
]

df = pd.DataFrame(students)

print(df)
print("평균 점수:", df["score"].mean())