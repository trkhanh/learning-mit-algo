import "strconv"

func summaryRanges(nums []int) []string {
	l := len(nums)
	if l == 0 {
		return []string{}
	} else if l == 1 {
		return []string{strconv.Itoa(nums[0])}
	}
	var ans []string
	var min = nums[0]
	var max = nums[0]
	for i := 1; i < l; i++ {
		n := nums[i]
		if n-max == 1 {
			max = n
			continue
		} else {
			ans = appendAns(ans, min, max)
			min = n
			max = n
		}
	}
	ans = appendAns(ans, min, max)
	return ans
}

func appendAns(ans []string, min, max int) []string {
	if min == max {
		return append(ans, strconv.Itoa(min))
	} else {
		return append(ans, strconv.Itoa(min)+"->"+strconv.Itoa(max))
	}
}