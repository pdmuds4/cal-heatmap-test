import random, json
from datetime import datetime, timedelta

num_data = 10  # 10個のデータを生成する例
data_list = []

for _ in range(200):
    # ランダムな日付を生成（過去1年分の日付）
    end_date = datetime(2023,12,31)
    start_date = end_date - timedelta(days=365)
    random_date = start_date + timedelta(days=random.randint(0, 365))
    formatted_date = random_date.strftime('%Y-%m-%d')

    # ランダムな整数を生成
    random_count = random.randint(1, 10)

    # JSONデータを生成し、リストに追加
    data = {
        'date': formatted_date,
        'count': random_count
    }
    data_list.append(data)

with open('data.json', 'w') as f:
    json.dump(data_list, f, indent=2)

#print(datetime.now())