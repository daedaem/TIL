# 무작위로 뽑기 위해서 random 이라는 걸 쓸건데.
# 이 random은 그냥 쓸 수 없고 어딘가에서 가져와야 한다.
# 불러오는 방법은 import를 사용한다.
import random

# lunch라고 하는 변수에 점심메뉴 3가지를 담아보자.
# 점심메뉴 추천 받습니다.

# 리스트를 만들때 중요한건 대괄호
# 그 안에 담긴 요소들 -> 문자열이라면, 각 요소들 전부 ""
# 쉼표로 구분 해준다.
lunch = ['짜장','돈가스','냉면']

# lunch 전체출력
print(lunch)
# lucnh 중에 3번째 요소 출력
# 항상 0부터 시작이기 때문에 세번째 요소는 2라고 입력
print(lunch[2])

# lunch가 가지고 있는 값중 하나를 무작위로 골라서
# menu라고 하는 변수에 담는다.
menu = random.choice(lunch)
print(menu)