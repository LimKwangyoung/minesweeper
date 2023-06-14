import random

LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)


def main():
    def create_board() -> list[list]:
        # create an initial board of size (width * height).
        arr = [[0] * width for _ in range(height)]

        # set mines randomly.
        mine_cnt = 0
        while mine_cnt < mine:
            row, col = random.randint(0, height - 1), random.randint(0, width - 1)
            if arr[row][col] != '*':
                arr[row][col] = '*'
                mine_cnt += 1

                # increase the number around a mine.
                if (row - 1) >= 0 and (col - 1) >= 0 and arr[row - 1][col - 1] != '*':
                    arr[row - 1][col - 1] += 1
                if (row - 1) >= 0 and arr[row - 1][col] != '*':
                    arr[row - 1][col] += 1
                if (row - 1) >= 0 and (col + 1) <= (width - 1) and arr[row - 1][col + 1] != '*':
                    arr[row - 1][col + 1] += 1
                if (col - 1) >= 0 and arr[row][col - 1] != '*':
                    arr[row][col - 1] += 1
                if (col + 1) <= (width - 1) and arr[row][col + 1] != '*':
                    arr[row][col + 1] += 1
                if (row + 1) <= (height - 1) and (col - 1) >= 0 and arr[row + 1][col - 1] != '*':
                    arr[row + 1][col - 1] += 1
                if (row + 1) <= (height - 1) and arr[row + 1][col] != '*':
                    arr[row + 1][col] += 1
                if (row + 1) <= (height - 1) and (col + 1) <= (width - 1) and arr[row + 1][col + 1] != '*':
                    arr[row + 1][col + 1] += 1

        return arr

    def draw_board(arr: list[list]) -> None:
        for row in range(height):
            for col in range(width):
                print(arr[row][col], end='  ')
            print()

    while True:
        level = input('난이도를 입력하세요 (초급, 중급, 고급): ')
        if level in LEVEL_SET:
            width, height, mine = LEVEL_SET[level]
            break
        print('난이도를 다시 입력하시오.')

    board = create_board()
    draw_board(board)


if __name__ == '__main__':
    main()
