import random


class UpDownGame:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.target = random.randint(start, end)
        self.tries = 0

    def input_number(self):
        while True:
            try:
                number = int(input("숫자를 입력하세요: "))
                return number
            except ValueError:
                print("숫자만 입력해주세요.")

    def give_hint(self, guess):
        if guess < self.target:
            print("UP")
        elif guess > self.target:
            print("DOWN")

    def give_extra_hint(self, guess):
        difference = abs(self.target - guess)

        if difference <= 5:
            print("힌트: 거의 다 왔습니다.")
        elif difference <= 15:
            print("힌트: 가까워지고 있습니다.")
        else:
            print("힌트: 아직 멉니다.")

    def play(self):
        print(f"{self.start}부터 {self.end} 사이의 숫자를 맞혀보세요.")

        while True:
            guess = self.input_number()
            self.tries += 1

            if guess == self.target:
                print(f"정답입니다! 시도 횟수: {self.tries}회")
                nickname = input("닉네임을 입력하세요: ")
                return nickname, self.tries

            self.give_hint(guess)
            self.give_extra_hint(guess)