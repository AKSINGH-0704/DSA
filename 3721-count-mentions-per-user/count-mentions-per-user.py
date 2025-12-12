class Solution:
    def countMentions(self, numberOfUsers, events):
        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers

        evs = []
        for ev in events:
            t = int(ev[1])
            if ev[0] == "OFFLINE":
                evs.append((t, 0, ev))
            else:
                evs.append((t, 1, ev))

        evs.sort(key=lambda x: (x[0], x[1]))

        for t, _, ev in evs:
            if ev[0] == "OFFLINE":
                u = int(ev[2])
                offline_until[u] = t + 60
            else:
                tokens = ev[2].split()
                for tok in tokens:
                    if tok == "ALL":
                        for u in range(numberOfUsers):
                            mentions[u] += 1
                    elif tok == "HERE":
                        for u in range(numberOfUsers):
                            if offline_until[u] <= t:
                                mentions[u] += 1
                    else:
                        u = int(tok[2:])
                        mentions[u] += 1

        return mentions
