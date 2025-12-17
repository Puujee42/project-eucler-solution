def count_sundays():
    # Mapping days: 0=Mon, 1=Tue, ..., 5=Sat, 6=Sun
    # Jan 1, 1900 was Monday (0). 
    # 1900 had 365 days. 365 % 7 = 1.
    # So Jan 1, 1901 was Tuesday (1).
    
    current_day = 1  # Tuesday
    sunday_count = 0
    
    # Standard days in months
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for year in range(1901, 2001): # 1901 to 2000 inclusive
        
        # Determine if leap year
        # Rule: Divisible by 4, unless century not divisible by 400.
        # In range 1901-2000, only 2000 is a century year, and it IS a leap year.
        # So standard % 4 check works for this specific range logic, 
        # but we'll write the full logic for completeness.
        if year % 4 == 0:
            if year % 100 == 0:
                is_leap = (year % 400 == 0)
            else:
                is_leap = True
        else:
            is_leap = False
            
        for month in range(12):
            # Check if the 1st of the current month is a Sunday (6)
            if current_day == 6:
                sunday_count += 1
            
            # Add days of the current month to advance to the next month
            days = days_in_months[month]
            if month == 1 and is_leap: # February
                days = 29
                
            current_day = (current_day + days) % 7
            
    return sunday_count

if __name__ == "__main__":
    result = count_sundays()
    print(f"Number of Sundays on the first of the month: {result}")