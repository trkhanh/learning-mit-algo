package leetcode1185

// @lc code=start
import "time"

func dayOfTheWeek(day int, month int, year int) string {
	const BaseDay = 4
	MonthDays := [...]int{-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30}
	yearDays := 0
	for y := 1971; y < year; y++ {
		yearDays += 365
		if isLeapYear(y) {
			yearDays += 1
		}
	}
	monthDays := day
	for m := 1; m < month; m++ {
		monthDays += MonthDays[m]
	}
	if month > 2 && isLeapYear(year) {
		monthDays += 1
	}
	countDays := yearDays + monthDays + BaseDay
	return time.Weekday(countDays % 7).String()
}

// w = (day + 2month + 3(month+1)/5 + year + year/4 - year/100 + year/400 + 1) % 7
func isLeapYear(year int) bool {
	return (year%4) == 0 && (year%100) != 0 || (year%400) == 0
}

func dayOfTheWeekKim(day int, month int, year int) string {
	var w int
	if month == 1 || month == 2 {
		month += 12
		year--
	}
	w = (day + 2*month + 3*(month+1)/5 + year + year/4 - year/100 + year/400 + 1) % 7
	return time.Weekday(w).String()
}
