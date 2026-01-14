class Solution:
    def separateSquares(self, squares):
        events = []

        for x, y, l in squares:
            events.append((y, 1, x, x + l))       # entering
            events.append((y + l, -1, x, x + l))  # leaving

        events.sort()
        active = []
        prev_y = events[0][0]
        slabs = []  # (y_start, y_end, area)

        def union_x_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    total += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            total += cur_r - cur_l
            return total

        for y, typ, x1, x2 in events:
            if y > prev_y:
                width = union_x_length(active)
                area = width * (y - prev_y)
                slabs.append((prev_y, y, area))
                prev_y = y

            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

        total_area = sum(a for _, _, a in slabs)
        half = total_area / 2

        acc = 0
        for y1, y2, area in slabs:
            if acc + area >= half:
                return y1 + (half - acc) / (area / (y2 - y1))
            acc += area

        return slabs[-1][1]
