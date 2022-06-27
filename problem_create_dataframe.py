import pandas as pd

# data 생성하기
data = {"A" : ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7"],
            "B" : ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7"],
            "C" : ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7"],
            "D" : ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7"],
            "F" : ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7"],
            "key" : ["K0", "K1", "K2", "K3", "K4", "K5", "K6", "K7"]
            }

# DataFrame 생성하기
df = pd.DataFrame(data)

# df_1, df_2, df_3, df_4
# 번호로 참조 -> iloc 사용
df_1 = df.iloc[range(0, 4), [0, 1, 2, 3]]
df_2 = df.iloc[[2, 3, 6, 7], [1, 3, 4]]
df_3 = df.iloc[range(0, 4), [0, 1, 5]]
df_4 = df.iloc[range(0, 4), [2, 3, 5]]

# df_1, df_2, df_3, df_4 각각 출력
print(df_1)
print("\n")

print(df_2)
print("\n")

print(df_3)
print("\n")

print(df_4)
