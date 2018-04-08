def solve(cameron_activities, jamie_activities):
    activities = []
    for act in cameron_activities:
        act.append(0)
        activities.append(act)
    for act in jamie_activities:
        act.append(1)
        activities.append(act)
    activities.sort(key=lambda x: x[0])
    desired_cameron_times = []
    desired_jamie_times = []
    forced_exchange_count = 0
    forced_cameron_time = 0
    forced_jamie_time = 0
    for i, act in enumerate(activities):
        assignee = act[2]
        prev_act = activities[i - 1]
        prev_assignee = prev_act[2]
        act_time = act[1] - act[0]
        interval_time = act[0] - prev_act[1]
        if interval_time < 0:
            interval_time = interval_time + 1440
        if assignee == 0:
            forced_jamie_time += act_time
        elif assignee == 1:
            forced_cameron_time += act_time
        if assignee != prev_assignee:
            forced_exchange_count += 1
        elif assignee == 0:
            desired_jamie_times.append(interval_time)
        elif assignee == 1:
            desired_cameron_times.append(interval_time)
    desired_cameron_times.sort()
    desired_jamie_times.sort()
    free_cameron_time = 720 - forced_cameron_time
    free_jamie_time = 720 - forced_jamie_time
    accepted_desired_cameron_times = []
    accepted_desired_jamie_times = []
    for time in desired_cameron_times:
        if free_cameron_time < time:
            break
        accepted_desired_cameron_times.append(time)
        free_cameron_time -= time
    for time in desired_jamie_times:
        if free_jamie_time < time:
            break
        accepted_desired_jamie_times.append(time)
        free_jamie_time -= time
    exchange_count = forced_exchange_count + (len(desired_cameron_times) - len(accepted_desired_cameron_times)) * 2 + (len(desired_jamie_times) - len(accepted_desired_jamie_times)) * 2
    return exchange_count


n_tests = int(input())

for i in range(n_tests):
    n_cameron_activities, n_jamie_activities = [int(x) for x in input().split()]
    cameron_activities = []
    for j in range(n_cameron_activities):
        cameron_activities.append([int(x) for x in input().split()])
    jamie_activities = []
    for j in range(n_jamie_activities):
        jamie_activities.append([int(x) for x in input().split()])
    ans = solve(cameron_activities, jamie_activities)
