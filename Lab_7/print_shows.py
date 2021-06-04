def print_shows(show_list):
    show_list_endtime = []
    jobs_selected = []
    for (event, start_time, duration) in show_list:
        show_list_endtime.append((event, start_time, start_time+duration))
    sorted_endtimes = sorted(show_list_endtime, key=lambda x: x[2])
    last = 0
    for j in range(0, len(sorted_endtimes)):
        if sorted_endtimes[j][1] >= last:
            jobs_selected.append(sorted_endtimes[j])
            last = sorted_endtimes[j][2]
    # print result, keep it seperate for cleanliness
    for (show, start_time, endtime) in jobs_selected:
        print("{} {} {}".format(show, start_time, endtime))

print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4),
    ('h', 8, 3)])
