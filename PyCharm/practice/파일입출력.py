# sc=open("score.txt","w",encoding="utf8")  #  encoding="utf8" : 한글문자 오류해결
# print("수학 점수는 0점",file=sc)
# print("영어점수는 50점",file=sc)
# sc.close()
#
# sc=open("score.txt",'a',encoding="utf8")
# sc.write("과학점수는 80점\n")
# sc.write("코딩점수는 100점\n")
# sc.close()

# sc=open("score.txt","r",encoding="utf8")
# #print(sc.read())
# print(sc.readline()) # 한 줄만 읽고 커서를 다음줄로 이동.
# sc.close

# sc=open("score.txt",'r',encoding="utf8")
# while(1):
#     line=sc.readline()
#     if not line:
#         break
#     print(line,end="")
# sc.close()

sc=open("score.txt",'r',encoding="utf8")
lines=sc.readlines()  # 리스트 형태로 저장함
for line in lines:
    print(line,end="")

import pickle
# profile_file = open("profile.pickle",'wb')
# profile={"이름":"조현우", "나이":23, "취미":['축구','게임','코딩']}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file=open("profile.pickle",'rb')
profile=pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile.pickle",'rb') as profile_file:
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
with open("study.txt",'r',encoding="utf8") as study_file:
    print(study_file.read())

#Quiz
# for i in range(1,51):
#     with open("{0}주차.txt".format(i),'w',encoding="utf8") as report:
#         report.write("-{0}주차 주간보고-\n". format(i))
#         report.write("부서 : \n이름 : \n업무 요약 : ")