#### 가로 연결 ####
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

# 국어, 영어, 수학, 과학, 이름 데이터
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

# 이름, 국어, 영어, 수학, 과학 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국_A", "영", "수_A", "과"]
grade_df_A = pd.DataFrame(data_A, columns=columns, index = [i for i in number])

# 이름, 국어, 체육, 수학, 음악 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국", "체", "수", "음"]
grade_df_B = pd.DataFrame(data_B, columns=columns, index = [i for i in number])

# 가로 합치기 pd.concat([grade_df_A, grade_df_B], axis=1)
pd.concat([grade_df_A, grade_df_B], axis=1)





#### 세로 연결 ####
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

# 국어, 영어, 수학, 과학, 이름 데이터
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

# 이름, 국어, 영어, 수학, 과학 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국", "영", "수", "과"]
grade_df_A = pd.DataFrame(data_A, columns=columns, index = [i for i in number])

# 타이틀 이름과, 성적표 출력
print("< A반 학생 5명의 성적표 > \n")
print(grade_df_A)

# 이름, 국어, 체육, 수학, 음악 생성 + data의 숫자 랜덤 생성
columns = ["이름", "국", "체", "수", "음"]
grade_df_B = pd.DataFrame(data_B, columns=columns, index = [i for i in number])

# 타이틀 이름과, 성적표 출력
print("\n")
print("< B반 학생 5명의 성적표 > \n")
print(grade_df_B)

print("\n")
# 세로 합치기 pd.concat([grade_df_A, grade_df_B], axis=0)
pd.concat([grade_df_A, grade_df_B], axis=0)
