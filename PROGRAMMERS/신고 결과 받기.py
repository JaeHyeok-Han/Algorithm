def solution(id_list, report, k):
    user_list = {}
    ben_count = {}
    report = list(set(report))
    for ele in report:
        user1, user2 = ele.split(' ')
        if user1 in user_list:
            user_list[user1].append(user2)
        else:
            user_list[user1] = [user2]
        if user2 in ben_count:
            ben_count[user2] += 1
        else:
            ben_count[user2] = 1

    real_ben_list = [user for user in ben_count if ben_count[user] >= k]

    def check_ben(user):
        if user not in user_list:
            return 0
        else:
            return len(list(set(user_list[user]) & set(real_ben_list)))

    return list(map(check_ben, id_list))


print(
    solution([
        "muzi",
        "frodo",
        "apeach",
        "neo"
    ], [
        "muzi frodo",
        "apeach frodo",
        "frodo neo",
        "muzi neo",
        "apeach muzi"
    ], 2))
