import pandas as pd

# data 생성
data = {"A" : ["A0", "A1", "A2", "A3"],
            "B" : ["B0", "B1", "B2", "B3"],
            "C" : ["C0", "C1", "C2", "C3"],
            "D" : ["D0", "D1", "D2", "D3"],
            "F" : ["F0", "F1", "F2", "F3"],
            "key" : ["K0", "K1", "K2", "K3"]
            }

# DataFrame 생성
df = pd.DataFrame(data)

# 이름으로 참조 -> loc 사용
df = df.loc[range(0, 4), ["A", "B", "C", "D", "B", "D", "F"]]

# df 출력
print(df)
