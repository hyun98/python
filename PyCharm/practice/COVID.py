# 중국에서 한 사람이 코로나에 걸렸다
# 사람의 평균적인 1일 밀접 접촉자 수는 0~5명으로 가정한다.
# 밀접 접촉한 사람이 코로나에 감염될 확률은 90퍼센트 라고 가정한다.
# 치사율을 3% 라 가정한다.
# 감염자는 사망하지 않으면 14일 후 완치된다.

from random import*
day = 0
health_people = 7000000000
infected_people = 1
death_people = 0
day_record = []
rescue_people =0
while(1):
    new_infected = 0
    if infected_people>3500000000:
        print("인류의 절반은 {0}일 만에 코로나에 걸리게 되고 인류는 멸망합니다.")
    day_pass = int(input("하루가 지나갑니다. 1을 입력하세요. "))
    day += day_pass

    for k in range(1, infected_people+1):
        if randint(1, 100) <= 3:
            death_people += 1
            infected_people -= 1

    for i in range(1, infected_people+1):
         meet = randint(0, 5)
         for j in range(meet):
               if randint(1, 10) > 1:
                   new_infected += 1

    infected_people += new_infected
    day_record.append(new_infected)

    if day >= 14:
        rescue_people = day_record[0+(day-14)]
        infected_people -= rescue_people

    print("------{0}일차------".format(day))
    print("현재 확진자는 {0}명 입니다.".format(infected_people))
    print('확진자는 {0}명 증가했습니다.'.format(new_infected))
    print("금일 완치자는 {0}명이고, 총 사망자는 {1}명 입니다.".format(rescue_people, death_people))