import pandas as pd

# 점수 입력 반복용 함수
def score_input(x):
    print('%s 점수를 입력하세요.' %(x))
    score = input()
    while True:
        try:
            if type(int(score)) == int:
                score = int(score)
                while score > 100 or score < 0:
                    print('\n점수는 0~100 사이의 숫자만 가능합니다. %s 점수를 입력하세요:' %(x))
                    score = int(input())
                scores.append(score)
                break
        except: print('\n점수는 숫자로 입력하세요. %s 점수를 입력하세요.:' %(x))
        score = input()

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

# 학생 수 입력
print('학생 수를 입력하세요:')
stu_num = input()
while True:
    try:
        if type(int(stu_num)) == int:
            stu_num = int(stu_num)
            while stu_num <= 0:
                print('\n학생은 1명 이상이어야 합니다. 학생 수를 입력하세요:')
                stu_num = int(input())
            break
    except: print('\n학생 수는 정수여야 합니다. 학생 수를 입력하세요:')
    stu_num = input()

# 학생 데이터 입력
students = []
stu_index = 0
for i in range(stu_num):
    print('\n%s번 학생 이름을 입력하세요:' %(i+1))
    stu_name = str(input())

    print('학번을 입력하세요:')
    stu_id = input()
    while True:
        try:
            if type(int(stu_id)) == int: break
        except: print('\n학번은 숫자여야 합니다. 학번을 입력하세요:')
        stu_id = input()

    students.append([stu_name, stu_id])

    scores = []
    for i in ['언어1', '수학', '과학']:
        score_input(i) # 점수 입력 함수

    students[stu_index].extend(scores)
    stu_index += 1

labels = ['Name', 'ID', 'Lng1', 'Math', 'Sci']
stu_df = pd.DataFrame(students, columns=labels) # 입력된 데이터로 데이터프레임 생성
stu_df['Total'] = stu_df['Lng1'] + stu_df['Math'] + stu_df['Sci']
stu_df['Avg'] = round(stu_df['Total']/3, 2)

# 각 과목 점수에 대한 등급 데이터프레임
stu_grade = stu_df.loc[:, ['Name', 'ID']]
for i in ['Lng1', 'Math', 'Sci']:
    grade(i)

# 출력 기능 선택
prt1 = '''\n기능을 선택하세요.
1. 모든 학생의 모든 정보 출력
2. 모든 학생의 총점 및 평균 점수 출력
3. 각 등급 점수에 대한 등급 출력
4. 학생 정보 수정
5. 종료\n'''

print(prt1)
func = str(input())
while True:
    if func == '1': print(stu_df.loc[:, ['Name', 'ID', 'Lng1', 'Math', 'Sci']])
    elif func == '2': print(stu_df.loc[:, ['Name', 'ID', 'Total', 'Avg']])
    elif func == '3': print(stu_grade)
    elif func == '4': print('work in progress')
    elif func == '5': break
    print(prt1)
    func = str(input())
