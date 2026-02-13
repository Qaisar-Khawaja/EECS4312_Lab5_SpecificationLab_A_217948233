## Student Name: Khawaja Faiza Qaisar
## Student ID: 217948233

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""

from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    WORK_START = 9 * 60
    WORK_END = 17 * 60
    LUNCH_START = 12 * 60
    LUNCH_END = 13 * 60
    STEP = 15

    # Friday rule: meetings must NOT start after 15:00
    if day.lower() == "friday":
        latest_start = 15 * 60
    else:
        latest_start = WORK_END

    def to_minutes(time_str: str) -> int:
        h, m = map(int, time_str.split(":"))
        return h * 60 + m

    def to_str(minutes: int) -> str:
        h, m = divmod(minutes, 60)
        return f"{h:02d}:{m:02d}"

    # Filter only events for the requested day
    events_for_day = [e for e in events if e.get("day", day) == day]

    # Build busy list, clipped to work hours
    busy_times = []
    for e in events_for_day:
        start = max(to_minutes(e["start"]), WORK_START)
        end = min(to_minutes(e["end"]), WORK_END)
        if end > start:
            busy_times.append((start, end))

    # Add lunch break
    busy_times.append((LUNCH_START, LUNCH_END))

    # Merge overlapping busy periods
    busy_times.sort()
    merged_busy = []
    for start, end in busy_times:
        if not merged_busy or start >= merged_busy[-1][1]:
            merged_busy.append([start, end])
        else:
            merged_busy[-1][1] = max(merged_busy[-1][1], end)

    available_starts = []
    current_time = WORK_START

    # Before each busy block
    for start, end in merged_busy:
        while (
            current_time + meeting_duration <= start
            and current_time <= latest_start
        ):
            available_starts.append(to_str(current_time))
            current_time += STEP

        # Move to end of busy block
        current_time = end

        # Align to next STEP boundary
        if current_time % STEP != 0:
            current_time += STEP - (current_time % STEP)
        else:
            current_time += STEP

    # After last busy block
    while (
        current_time + meeting_duration <= WORK_END
        and current_time <= latest_start
    ):
        available_starts.append(to_str(current_time))
        current_time += STEP

    return available_starts









# from typing import List, Dict

# def suggest_slots(
#     events: List[Dict[str, str]],
#     meeting_duration: int,
#     day: str
# ) -> List[str]:
#     WORK_START = 9 * 60
#     WORK_END = 17 * 60
#     LUNCH_START = 12 * 60
#     LUNCH_END = 13 * 60
#     STEP = 15

#     def to_minutes(time_str: str) -> int:
#         h, m = map(int, time_str.split(":"))
#         return h * 60 + m

#     def to_str(minutes: int) -> str:
#         h, m = divmod(minutes, 60)
#         return f"{h:02d}:{m:02d}"

#     # Filter only events for the requested day
#     events_for_day = [e for e in events if e.get("day", day) == day]

#     # Build busy list, clip to work hours
#     busy_times = []
#     for e in events_for_day:
#         start = max(to_minutes(e["start"]), WORK_START)
#         end = min(to_minutes(e["end"]), WORK_END)
#         if end > start:
#             busy_times.append((start, end))
    
#     # Add lunch
#     busy_times.append((LUNCH_START, LUNCH_END))

#     # Merge overlapping busy periods
#     busy_times.sort()
#     merged_busy = []
#     for start, end in busy_times:
#         if not merged_busy or start >= merged_busy[-1][1]:
#             merged_busy.append([start, end])
#         else:
#             merged_busy[-1][1] = max(merged_busy[-1][1], end)

#     # Find available slots
#     available_starts = []
#     current_time = WORK_START

#     for start, end in merged_busy:   
#         while current_time + meeting_duration <= start:
#             available_starts.append(to_str(current_time))
#             current_time += STEP
#         # Move current_time to the end of busy period
#         current_time = end
#         # Align upward if needed
#         if current_time % STEP != 0:
#             current_time += STEP - (current_time % STEP)
#         else:
#             # Event ended exactly on a boundary so skip that boundary
#             current_time += STEP

#     # After last busy period, fill remaining day
#     while current_time + meeting_duration <= WORK_END:
#         available_starts.append(to_str(current_time))
#         current_time += STEP
#     return available_starts











