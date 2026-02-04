def max_meetings():
    T = int(input())

    for _ in range(T):
        N = int(input())
        meetings = []

        for i in range(N):
            s, e = map(int, input().split())
            meetings.append((s, e))

        meetings.sort(key=lambda x: x[1])

        count = 0
        last_end = -1

        for start, end in meetings:
            if start >= last_end:
                count += 1
                last_end = end

        print(count)

max_meetings()