class RankingBoard:
    def __init__(self):
        self.records = []

    def add_record(self, nickname, tries):
        record = {
            "name": nickname,
            "tries": tries
        }

        self.records.append(record)

    def show_ranking(self):
        if len(self.records) == 0:
            print("등록된 기록이 없습니다.")
            return

        self.records.sort(key=lambda x: (x["tries"], x["name"]))

        print("----명예의 전당----")

        for i in range(min(3, len(self.records))):
            print(f"{i + 1}위 {self.records[i]['name']} {self.records[i]['tries']}회")