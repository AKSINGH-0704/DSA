class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import defaultdict
        import heapq
        freq = defaultdict(int)
        topMin = []    # min-heap of (freq, val) for elements currently in top set
        restMax = []   # max-heap of (-freq, -val) for other elements
        in_top = set()
        sum_top = 0
        n = len(nums)

        def push_top(f, v):
            heapq.heappush(topMin, (f, v))

        def push_rest(f, v):
            heapq.heappush(restMax, (-f, -v))

        def valid_rest():
            while restMax:
                f, v = restMax[0]
                f = -f; v = -v
                if freq.get(v, 0) != f or v in in_top:
                    heapq.heappop(restMax)
                    continue
                return f, v
            return None

        def valid_top():
            while topMin:
                f, v = topMin[0]
                if freq.get(v, 0) != f or v not in in_top:
                    heapq.heappop(topMin)
                    continue
                return f, v
            return None

        def move_rest_to_top():
            nonlocal sum_top
            item = valid_rest()
            if not item:
                return False
            f, v = item
            heapq.heappop(restMax)
            in_top.add(v)
            push_top(f, v)
            sum_top += f * v
            return True

        def move_top_to_rest():
            nonlocal sum_top
            item = valid_top()
            if not item:
                return False
            f, v = item
            heapq.heappop(topMin)
            in_top.remove(v)
            push_rest(f, v)
            sum_top -= f * v
            return True

        def rebalance():
            nonlocal sum_top
            while len(in_top) < x:
                if not move_rest_to_top():
                    break
            while len(in_top) > x:
                move_top_to_rest()
            while True:
                r = valid_rest()
                t = valid_top()
                if not r or not t:
                    break
                rf, rv = r
                tf, tv = t
                if (rf, rv) > (tf, tv):
                    heapq.heappop(restMax)
                    heapq.heappop(topMin)
                    in_top.remove(tv)
                    in_top.add(rv)
                    push_rest(tf, tv)
                    push_top(rf, rv)
                    sum_top += rf * rv
                    sum_top -= tf * tv
                else:
                    break

        for i in range(k):
            v = nums[i]
            freq[v] += 1
            if v in in_top:
                sum_top += v
                push_top(freq[v], v)
            else:
                push_rest(freq[v], v)
            rebalance()

        ans = [sum_top]
        for i in range(k, n):
            outv = nums[i - k]
            freq[outv] -= 1
            if outv in in_top:
                sum_top -= outv
                if freq[outv] == 0:
                    in_top.remove(outv)
                else:
                    push_top(freq[outv], outv)
            else:
                if freq[outv] > 0:
                    push_rest(freq[outv], outv)
            if freq[outv] == 0:
                del freq[outv]

            inv = nums[i]
            freq[inv] += 1
            if inv in in_top:
                sum_top += inv
                push_top(freq[inv], inv)
            else:
                push_rest(freq[inv], inv)

            rebalance()
            ans.append(sum_top)
        return ans
