x = int(input())        # 주어질 수의 개수를 입력받음.
num_list = []       # 숫자들의 리스트를 생성
for i in range(x):      # x만큼 반복하여 num_list에 항목들을 추가
    num_list.append(int(input())) 
num_list1 = sorted(num_list)        # num_list를 정렬
for i in range(len(num_list)):      # 요소들을 하나씩 출력
    print(num_list1[i])
