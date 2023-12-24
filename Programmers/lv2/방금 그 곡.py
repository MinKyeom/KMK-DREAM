# 내 풀이
def solution(m, musicinfos):
    from collections import deque

    mu = musicinfos

    result = []

    # 멜로디 모양 변형

    melody_check = deque(list(m))

    new_mel = []

    while melody_check:
        a = melody_check.popleft()

        if a == "#":
            b = new_mel.pop()
            b = b.lower()
            c = b + a
            new_mel.append(c)
        else:
            new_mel.append(a)

    m = "".join(new_mel)

    # 주어진 가사 변형

    for k in mu:
        t = k.split(",")

        time_start = t[0].split(":")
        time_start = int(time_start[0]) * 60 + int(time_start[1])

        time_finish = t[1].split(":")
        time_finish = int(time_finish[0]) * 60 + int(time_finish[1])

        run_time = time_finish - time_start  # 시작 할 때 첫 소절 나옴

        check_mel = deque(list(t[3]))
        new_check = []

        # 비교할 가사 모양 변형
        while check_mel:
            i = check_mel.popleft()

            if i == "#":
                j = new_check.pop()
                j = j.lower()
                h = j + i
                new_check.append(h)
            else:
                new_check.append(i)

        # print(new_check)

        if len(new_check) > run_time:
            new_check = new_check[0:run_time]

        elif len(new_check) == run_time:
            new_check = new_check

        else:
            count = 0
            num = len(new_check)
            while len(new_check) <= run_time:
                if count == 0:
                    new_check += [new_check[0]]
                else:
                    k = count % num
                    new_check += [new_check[k]]
                count += 1

        t[3] = "".join(new_check)
        t += [run_time]

        if m in t[3]:
            result.append(t)

    if len(result) == 0:
        return "(None)"

    result.sort(key=lambda x: (-int(x[-1])))

    return result[0][2]

# 다른 사람 풀이

def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]