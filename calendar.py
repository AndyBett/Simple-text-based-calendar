import calendar

def display_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()
    
    # Display the month
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

# Input year and month
year = int(input("Enter year (e.g., 2024): "))
month = int(input("Enter month (1-12): "))

# Display the calendar
display_calendar(year, month)