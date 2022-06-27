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

# 국어, 영어, 수학, 과학, 국어, 체육, 수학, 음악, 이름 데이터
data_A = {
    "국" : random_korean,
    "영" : random_english,
    "수" : random_math,
    "과" : random_science,
    "이름" : ["가수빈", "나수빈", "다수빈", "라수빈", "마수빈"]
}

data_B = {
    "국" : random_korean,
    "체" : random_physical,
    "수" : random_math,
    "음" : random_music,
    "이름" : ["바수빈", "사수빈", "아수빈", "자수빈", "차수빈"]
}

# 인덱스 숫자 생성
number = '12345'

# 이름, 국어, 영어, 수학, 과학 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국", "영", "수", "과"]
df1 = pd.DataFrame(data_A, columns=columns, index = [i for i in number])

# 타이틀 이름과 성적표 출력
print("< A반 학생 5명의 성적표 >\n")
print(df1)

# 이름, 국어, 체육, 수학, 음악 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국", "체", "수", "음"]
df2 = pd.DataFrame(data_B, columns=columns, index = [i for i in number])

# 타이틀 이름과 성적표 출력
print("\n")
print("< B반 학생 5명의 성적표 >\n")
print(df2)

# 두 데이터 중복하여 출력
print("\n")
print("< A, B반 중복 >\n")
df3 = pd.merge(df1, df2, on=None, how = "outer")
print(df3)

# 이름으로 그룹화하여 grouped_name에 대입 후 출력
print("\n")
print("< A, B반 중복한 것을 이름으로 그룹화 한 표 >\n")
grouped_name = df3.groupby("이름")
mean_df = grouped_name.mean()
print(mean_df)

