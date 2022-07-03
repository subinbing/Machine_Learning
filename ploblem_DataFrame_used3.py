import pandas as pd

# data 생성
data = {"A" : ["A0", "A2", "A3", "NaN"],
            "B" : ["B0", "B1", "B2", "B3", "NaN"],
            "key" : ["K0", "K4", "K2", "K3", "K1"],
            "C" : ["C0", "NaN", "C2", "C3", "C4"],
            "D" : ["D0", "NaN", "D2", "D3", "D1"]
            }

# DataFrame 생성
df = pd.DataFrame(data)

# 이름으로 참조 -> loc 사용
df_3 = df/loc[range(0, 5), ["A", "B", "key", "C", "D"]]

# df 출력
print(df_3)
