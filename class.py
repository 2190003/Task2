# 2190003_rkdalsdk
class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def average(self):
        result = (self.kor + self.eng + self.math) / 3
        return result

n = int(input(f'학생 수 입력(N): '))

for i in range(1, n + 1):
    kor = int(input(f'{i}번째 학생의 국어 성적 입력: '))
    eng = int(input(f'{i}번째 학생의 영어 성적 입력: '))
    math = int(input(f'{i}번째 학생의 수학 성적 입력: '))
    student = Student(kor, eng, math)
    print(f'{i}번째 학생의 평균 점수: {student.average()}')
