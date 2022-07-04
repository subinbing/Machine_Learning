import pandas as pd

# data 생성하기
data1 = {"A" : ["A0", "A1", "A2", "A3"],
             "B" : ["B0", "B1", "B2", "B3"],
             "C" : ["C0", "C1", "C2", "C3"],
             "D" : ["D0", "D1", "D2", "D3"]
             }

# data 생성하기
data2 = {"B" : ["B2", "B3", "B6", "B7"],
             "D" : ["D2", "D3", "D6", "D7"],
             "F" : ["F0", "F1", "F2", "F3"]
             }

# DataFrame 생성하기
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 두 개의 데이터 연결
df3 = pd.concat([df1, df2], axis = 0)

# df 출력
print(df3)
