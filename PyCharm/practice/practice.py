# url1="http://naver.com"
# url2="http://daum.net"
# url3="http://google.co.kr"
#
# def pw_creator(url):
#     url=url.replace("http://", "")
#     url=url[:url.index('.')]
#     password=url[:3]+str(len(url))+str(url.count('e'))+"!"
#     print("{0}의 비밀번호는 {1}입니다.".format(url,password))
#
# pw_creator(input("url을 복사해서 넣으시오"))
#
subway=["유재석","조세호","박명수"]
# subway.append("하하")
# print(subway)
# subway.insert(1,"정형돈")
# print(subway)
# print(subway.pop())

from random import*
st=range(1,21)
st=list(st)
#print(type(st))
shuffle(st)
print("--당첨자 발표--")
print("치킨 당첨자 :",st.pop())
print("커피 당첨자 :",sample(st,3))
print("--축하합니다--")

#다른 방법
winner=sample(st,4)
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
