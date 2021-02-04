package leetcode0794

func validTicTacToe(board []string) bool {
	var xCount, oCount int
	var xWins, oWins, xLeftDiag, xRightDiag, oLeftDiag, oRightDiag int
	var xRows, oRows [3]int
	for i, s := range board {
		if s == "XXX" {
			xWins++
		} else if s == "OOO" {
			oWins++
		}

		for j, r := range s {
			if r == 'X' {
				xCount++
				xRows[j]++
				if i == j {
					xLeftDiag++
				}
				if i+j == 2 {
					xRightDiag++
				}
			} else if r == 'O' {
				oCount++
				oRows[j]++
				if i == j {
					oLeftDiag++
				}
				if i+j == 2 {
					oRightDiag++
				}
			}
		}
	}

	for _, r := range xRows {
		if r == 3 {
			xWins++
		}
	}

	for _, r := range oRows {
		if r == 3 {
			oWins++
		}
	}

	if xLeftDiag == 3 {
		xWins++
	}

	if xRightDiag == 3 {
		xWins++
	}

	if oLeftDiag == 3 {
		oWins++
	}
	if oRightDiag == 3 {
		oWins++
	}
	if xCount != oCount && xCount-oCount != 1 {
		return false
	}

	if xWins > 2 || oWins > 2 {
		return false
	}

	if xWins > 0 && oWins > 0 {
		return false
	}
	if xWins > 0 && xCount == oCount {
		return false
	}

	if oWins > 0 && xCount > oCount {
		return false
	}

	return true
}
