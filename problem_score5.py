import pandas as pd
import numpy as np

# 난수 생성
np.random.seed(0)

# 국어, 영어, 수학, 과학, 국어 체육, 수학, 음악 점수 랜덤 생성
random_korean_1 = np.random.randint(1, 100, 5)
random_english = np.random.randint(1, 100, 5)
random_math_1 = np.random.randint(1, 100, 5)
random_science = np.random.randint(1, 100, 5)

random_korean_2 = np.random.randint(1, 100, 5)
random_physical = np.random.randint(1, 100, 5)
random_math_2 = np.random.randint(1, 100, 5)
random_music = np.random.randint(1, 100, 5)

# 국어, 영어, 수학, 과학, 국어, 체육, 수학, 음악 데이터
data_A = {
    "국_A" : random_korean,
    "영" : random_english,
    "수_A" : random_math,
    "과" : random_science,
    "이름" : ["가수빈", "나수빈", "다수빈", "라수빈", "마수빈"]
}

data_B = {
    "국_B" : random_korean,
    "체" : random_physical,
    "수_B" : random_math,
    "음" : random_music,
    "이름" : ["바수빈", "사수빈", "아수빈", "자수빈", "차수빈"]
}

# 인덱스 숫자 생성
number = '12345'

# 국어, 영어, 수학, 과학 생성 + data의 숫자 랜덤 생성
columns1 = ["국_A", "영", "수_A", "과"]
df1 = pd.DataFrame(data_A, columns=columns, index = [i for i in number])

# 국어, 체육, 수학, 음악 생성 + data의 숫자 랜덤 생성
columns2 = ["국", "체", "수", "음"]
df2 = pd.DataFrame(data_B, columns=columns, index = [i for i in number])

# Dataframe을 생성하고 열을 추가
df1 = pd.DataFrame()
df2 = pd.DataFrame()

for column in columns1:
    df1[column] = np.random.choice(range(1, 101), 5)
df1.index = range(1, 6)

for column in columns2:
    df2[column] = np.random.choice(range(1, 101), 5)
df2.index = range(1, 6)

# df의 각 행에 대해 행 뒤의 차이를 계산한 DataFrame을 df1, 2_diff에 대입
df1_diff = df1.diff(-1, axis = 0)
df2_diff = df2.diff(-1, axis = 0)

# df1, 2와 df1,2_diff의 내용을 비교해서 처리 결과를 확인
print(df1)
print(df1_diff)
print("\n")
print(df2)
print(df2_diff)

# df의 각 행에 대해 행 뒤의 차이를 계산한 DataFrame을 df1,2_diff에 대입
df1_diff = df1.diff(-1, axis = 0)
df2_diff = df2.diff(-1, axis = 0)

# df1, 2와 df1,2_diff의 내용을 비교해서 처리 결과를 확인
print(df1)
print(df1_diff)
print("\n")
print(df2)
print(df2_diff)

# df의 각 행에 대해 행 뒤의 차이를 계산한 DataFrame을 df1,2_diff에 대입
df1_diff = df1.diff(-1, axis = 1)
df2_diff = df2.diff(-1, axis = 1)

# df1, 2와 df1,2_diff의 내용을 비교해서 처리 결과를 확인
print(df1)
print(df1_diff)
print("\n")
print(df2)
print(df2_diff)
