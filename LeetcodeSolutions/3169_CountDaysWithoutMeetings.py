def countDays( days, meetings):
        if not meetings:
            return days  
        
        meetings.sort()
        
     
        total_occupied = 0
        prev_start, prev_end = meetings[0]
        
        for start, end in meetings[1:]:
            if start <= prev_end:  
                prev_end = max(prev_end, end)
            else: 
                total_occupied += (prev_end - prev_start + 1)
                prev_start, prev_end = start, end
        

        total_occupied += (prev_end - prev_start + 1)

        return days - total_occupied


