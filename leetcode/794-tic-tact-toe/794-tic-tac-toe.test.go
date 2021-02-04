package leetcode0794

import "testing"

func Test_validTicTacToe(t *testing.T) {

	type args struct {
		board []string
	}

	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			args: args{
				board: []string{"XOX", "O O", "XOX"},
			},
			want: true,
		}, {
			args: args{
				board: []string{"XXX", "OOX", "OOX"},
			},
			want: true,
		},
		{

			args: args{
				board: []string{"XXO", "XOX", "OXO"},
			},
			want: false,
		},
	}

	for _, tt := range test {
		t.Run(tt.name, func(t *testing.T) {
			if got := validTicTacToe(tt.args.board); got != tt.want {
				t.Errorf("validTicTacToe()= %v, want %v", got, tt.want)
			}
		})
	}
}
