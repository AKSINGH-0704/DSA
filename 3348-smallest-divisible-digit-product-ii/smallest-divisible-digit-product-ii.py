class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        cnt_2 = cnt_3 = cnt_5 = cnt_7 = 0

        while temp_t % 2 == 0:
            cnt_2 += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            cnt_3 += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            cnt_5 += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            cnt_7 += 1
            temp_t //= 7

        if temp_t > 1:
            return "-1"

        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        def min_digits_23(r2: int, r3: int) -> int:
            if r2 <= 0 and r3 <= 0:
                return 0
            r2 = max(0, r2)
            r3 = max(0, r3)
            c8 = r2 // 3
            rem2 = r2 % 3
            c9 = r3 // 2
            rem3 = r3 % 2

            if rem2 == 0 and rem3 == 0:
                extra = 0
            elif (
                (rem2 == 0 and rem3 == 1)
                or (rem2 == 1 and rem3 == 0)
                or (rem2 == 1 and rem3 == 1)
                or (rem2 == 2 and rem3 == 0)
            ):
                extra = 1
            else:  
                extra = 2

            return c8 + c9 + extra

        def min_digits(r2: int, r3: int, r5: int, r7: int) -> int:
            return max(0, r7) + max(0, r5) + min_digits_23(r2, r3)

        n = len(num)

        pref_2, pref_3, pref_5, pref_7 = [0] * n, [0] * n, [0] * n, [0] * n
        first_zero = n
        c2 = c3 = c5 = c7 = 0

        for i in range(n):
            if num[i] == "0":
                first_zero = i
                break
            d = int(num[i])
            f2, f3, f5, f7 = factors[d]
            c2, c3, c5, c7 = c2 + f2, c3 + f3, c5 + f5, c7 + f7
            pref_2[i], pref_3[i], pref_5[i], pref_7[i] = c2, c3, c5, c7

        if (
            first_zero == n
            and pref_2[n - 1] >= cnt_2
            and pref_3[n - 1] >= cnt_3
            and pref_5[n - 1] >= cnt_5
            and pref_7[n - 1] >= cnt_7
        ):
            return num

        start_p = min(n - 1, first_zero)
        best_p, best_d = -1, -1

        for p in range(start_p, -1, -1):
            start_digit = int(num[p]) + 1
            p_f2 = pref_2[p - 1] if p > 0 else 0
            p_f3 = pref_3[p - 1] if p > 0 else 0
            p_f5 = pref_5[p - 1] if p > 0 else 0
            p_f7 = pref_7[p - 1] if p > 0 else 0

            found = False
            for d in range(start_digit, 10):
                df2, df3, df5, df7 = factors[d]
                rem2 = max(0, cnt_2 - p_f2 - df2)
                rem3 = max(0, cnt_3 - p_f3 - df3)
                rem5 = max(0, cnt_5 - p_f5 - df5)
                rem7 = max(0, cnt_7 - p_f7 - df7)

                if min_digits(rem2, rem3, rem5, rem7) <= n - 1 - p:
                    best_p, best_d = p, d
                    found = True
                    break
            if found:
                break

        def fill_greedy(
            length: int, start_idx: int, r2: int, r3: int, r5: int, r7: int
        ) -> list[str]:
            res = []
            for i in range(start_idx, length):
                slots_left = length - 1 - i
                for x in range(1, 10):
                    xf2, xf3, xf5, xf7 = factors[x]
                    rem2 = max(0, r2 - xf2)
                    rem3 = max(0, r3 - xf3)
                    rem5 = max(0, r5 - xf5)
                    rem7 = max(0, r7 - xf7)
                    if min_digits(rem2, rem3, rem5, rem7) <= slots_left:
                        res.append(str(x))
                        r2, r3, r5, r7 = rem2, rem3, rem5, rem7
                        break
            return res

        if best_p != -1:
            p, d = best_p, best_d
            p_f2 = pref_2[p - 1] if p > 0 else 0
            p_f3 = pref_3[p - 1] if p > 0 else 0
            p_f5 = pref_5[p - 1] if p > 0 else 0
            p_f7 = pref_7[p - 1] if p > 0 else 0

            df2, df3, df5, df7 = factors[d]
            r2 = max(0, cnt_2 - p_f2 - df2)
            r3 = max(0, cnt_3 - p_f3 - df3)
            r5 = max(0, cnt_5 - p_f5 - df5)
            r7 = max(0, cnt_7 - p_f7 - df7)

            ans = (
                list(num[:p]) + [str(d)] + fill_greedy(n, p + 1, r2, r3, r5, r7)
            )
            return "".join(ans)

        target_len = max(n + 1, min_digits(cnt_2, cnt_3, cnt_5, cnt_7))
        ans = fill_greedy(target_len, 0, cnt_2, cnt_3, cnt_5, cnt_7)
        return "".join(ans)