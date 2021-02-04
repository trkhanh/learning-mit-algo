import ("fmt"
"strconv"
"strings"
)

func isAdditiveNumber(num string) bool {
for i := 1; i < len(num); i++ {
	for j := i + 1; j < len(num); j++ {
		first, second, remainder := num[:i], num[i:j], num[j:]
		if strings.HasPrefix(first, "0") && first != "0" {
			return false
		}
		if strings.HasPrefix(second, "0") && second != "0" {
			break
		}
		for len(remainder) > 0 {
			firstInt, _ := strconv.Atoi(first)
			secondInt, _ := strconv.Atoi(second)
			third := strconv.Itoa(firstInt + secondInt)
			fmt.Println(third)
			if strings.HasPrefix(remainder, third) {
				remainder = strings.Replace(remainder, third, "", 1)
				first, second = second, third
			} else {
				break
			}
		}
		if len(remainder) == 0 {
			return true
		}
	}
}
return false
}