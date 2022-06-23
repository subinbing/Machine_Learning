import pandas as pd
import numpy as np

# 난수 생성
np.random.seed(0)

# 국어, 체육, 수학, 음악 점수 랜덤 생성
random_korean = np.random.randint(1, 100, 5)
random_physical = np.random.randint(1, 100, 5)
random_math = np.random.randint(1, 100, 5)
random_music = np.random.randint(1, 100, 5)

# 국어, 체육, 수학, 음악, 이름 데이터
data = {
    "국" : random_korean,
    "체" : random_physical,
    "수" : random_math,
    "음" : random_music,
    "이름" : ["바수빈", "사수빈", "아수빈", "자수빈", "차수빈"]
}

# 인덱스 숫자 생성
number = '12345'

# 이름, 국어, 체육, 수학, 음악, 이름 생성
columns = ["이름", "국", "체", "수", "음"]

# data의 숫자 랜덤 생성
grade_df = pd.DataFrame(data, columns=columns, index = [i for i in number])

# 타이틀 이름과 성적표 출력
print("< B반 학생 5명의 이름, 국어, 체육, 수학, 음악 성적표 >\n")
print(grade_df)
