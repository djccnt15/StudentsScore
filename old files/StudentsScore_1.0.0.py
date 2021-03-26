import pandas as pd

# 학생 수 입력
print('학생 수를 입력하세요:')
stu_num = int(input())
while stu_num <= 0:
    print('\n학생은 1명 이상이어야 합니다. 학생 수를 입력하세요:')
    stu_num = int(input())

# 점수 입력 반복용 함수
def score_input(x):
    print('%s 점수를 입력하세요.' %(x))
    score = int(input())
    while score > 100 or score < 0:
        print('\n점수는 0~100점으로 입력해주세요.')
        print('%s 점수를 입력하세요:' %(x))
        score = int(input())
    scores.append(score)

# 학생 데이터 입력
students = []
stu_index = 0
sub_k = ['언어1', '수학', '과학']
for i in range(stu_num):
    print('\n학생 이름을 입력하세요:')
    stu_name = str(input())

    print('학번을 입력하세요:')
    stu_id = int(input())

    students.append([stu_name, stu_id])

    scores = []
    for i in sub_k:
        score_input(i) # 점수 입력 함수

    students[stu_index].extend(scores)
    stu_index += 1

labels = ['Name', 'ID', 'Lng1', 'Math', 'Sci']
stu_df = pd.DataFrame(students, columns=labels) # 입력된 데이터로 데이터프레임 생성

stu_sum = stu_df.iloc[:, :2] # 모든 학생의 총점 및 평균 데이터프레임
stu_sum['Total'] = stu_df['Lng1'] + stu_df['Math'] + stu_df['Sci']
stu_sum['Avg'] = round(stu_sum['Total']/3, 2)

# 등급 부여 함수
def grade(x):
    g = []
    for row in stu_df[x]:
        if row >= 90: g.append('A')
        elif row >= 80: g.append('B')
        elif row >= 70: g.append('C')
        elif row >= 60: g.append('D')
        else: g.append('F')
    stu_grade['%s_grade' %(x)] = g

stu_grade = stu_df.iloc[:, :2] # 총점 및 각 등급 점수에 대한 등급 데이터프레임
stu_grade['Total'] = stu_sum['Total']
sub = ['Lng1', 'Math', 'Sci']
for i in sub:
    grade(i)
# print(stu_grade)

prt1 = '''\n기능을 선택하세요.
1. 모든 학생의 모든 정보 출력
2. 모든 학생의 총점 및 평균 점수 출력
3. 총점 및 각 등급 점수에 대한 등급 출력
4. 종료'''

print(prt1)
func = str(input())

# 출력 기능 선택
while True:
    if func == '1': print(stu_df)
    elif func == '2': print(stu_sum)
    elif func == '3': print(stu_grade)
    elif func == '4': break

    print(prt1)
    func = str(input())
