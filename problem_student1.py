import pandas as pd
import numpy as np

# 난수 생성
np.random.seed(0)

# 국어, 영어, 수학, 과학 점수 랜덤 생성
random_korean = np.random.randint(1, 100, 5)
random_english = np.random.randint(1, 100, 5)
random_math = np.random.randint(1, 100, 5)
random_science = np.random.randint(1, 100, 5)

# 국어, 영어, 수학, 과학, 이름 데이터
data = {
    "국" : random_korean,
    "영" : random_english,
    "수" : random_math,
    "과" : random_science,
    "이름" : ["가수빈", "나수빈", "다수빈", "라수빈", "마수빈"]
}

# 인덱스 숫자 생성
number = '12345'

# 이름, 국어, 영어, 수학, 과학, 이름 생성
columns = ["이름", "국", "영", "수", "과"]

# data의 숫자 랜덤 생성
grade_df = pd.DataFrame(data, columns=columns, index = [i for i in number])

# 타이틀 이름과 성적표 출력
print("< A반 학생 5명의 이름, 국어, 영어, 수학, 과학 성적표 >\n")
print(grade_df)
