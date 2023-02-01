class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        for x in trainers:
            if players[count] > x:
                continue
            count += 1
            if count == len(players):
                break
        return count
