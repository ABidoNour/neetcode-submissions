class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        curr_sum = 0
        for op in operations:
            if op == "+":
                val = record[-1] + record[-2]
                curr_sum += val
                record.append(val)
            elif op == "C":
                curr_sum -= record.pop()
            elif op == "D":
                val = record[-1] * 2
                curr_sum += val
                record.append(val)
            else:
                op = int(op)
                curr_sum += op
                record.append(op)
        return curr_sum
