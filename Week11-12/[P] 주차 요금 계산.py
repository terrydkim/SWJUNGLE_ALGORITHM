def solution(fees, records):
    answer = []
    dic = {}
    result = []
    for i in range(len(records)):
        cnt = 0
        # 시간 , 차량 번호, 상태 로 파싱
        a = records[i].split()

        if (a[2] == "IN"):
            # 딕셔너리 초기화
            if not a[1] in dic:
                dic[a[1]] = 0

            # 출입 시간 계산
            a_split_time = a[0].split(":")
            # 분으로 변환
            a_time = int(a_split_time[0])*60+int(a_split_time[1])
            for j in range(i+1, len(records)):
                b = records[j].split()
                b_split_time = b[0].split(":")
                b_time = int(b_split_time[0])*60+int(b_split_time[1])
                # 차량 번호 같고 out 일 때
                if (a[1] == b[1]):
                    if (b[2] == "OUT"):
                        cnt += 1
                        # 시간 계산
                        time = b_time - a_time
                        if time <= 0:
                            time = 0
                        break
            # out 기록이 없어서 23:59로 계산
            if cnt == 0:
                out_time = 23*60 + 59
                time = out_time - a_time
            dic[a[1]] += time

    for k, v in dic.items():
        # 기본 시간 안넘기면 기본 요금
        base = v - fees[0]
        dic[k] = fees[1]
        if base <= 0:
            continue
        else:
            if base % fees[2] != 0:
                dic[k] += fees[3]
            dic[k] += (base // fees[2])*fees[3]

    # 번호 작은 순으로 sort
    dic_sort = sorted(dic.items())
    print(dic)
    for k, v in dic_sort:
        result.append(v)

    return result
