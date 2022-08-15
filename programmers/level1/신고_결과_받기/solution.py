def solution(id_list, report, k):
    answer = []

    # d = dict.fromkeys(id_list, [])s
    report_detail = {}
    report_mail_count = {}
    for id in id_list:
        report_detail.setdefault(id, [])
        report_mail_count.setdefault(id, 0)

    for r in report:
        rd = r.split(" ")
        reporter = rd[0]
        reported = rd[1]

        l = report_detail.setdefault(reporter, [])
        l.append(reported)

        report_detail[reporter] = list(set(l))

    # print(report_detail)

    r_list = []
    for v in report_detail.values():
        r_list.extend(v)

    # print(r_list)

    # report_count = {}
    # for key in report_detail.keys():
    #     count = report_count.setdefault(key, 0)
    #     reporteds = report_detail[key]

    #     for reported in reporteds:
    #         total_count = r_list.count(reported)
    #         if total_count >= k:
    #             count += 1

    #     report_count[key] = count

    # answer = list(report_count.values())

    for key in report_mail_count.keys():
        l = report_detail.get(key)
        for i in l:
            count = r_list.count(i)
            if count >= k:
                report_mail_count[key] = report_mail_count.get(key) + 1

    answer = list(report_mail_count.values())

    return answer


if __name__ == "__main__":
    print(
        solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2,
        )
    )

    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
