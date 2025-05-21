def main():
    import sys

    def read_input(input_lines):
        if not input_lines:
            return []
        return [input_lines[0]] + read_input(input_lines[1:])

    def process_tests(test_lines, index, n_cases, accumulated_results):
        if index >= len(test_lines) or len(accumulated_results) == n_cases:
            return accumulated_results
        try:
            count = int(test_lines[index])
            if index + 1 >= len(test_lines):
                return process_tests(test_lines, index + 2, n_cases, accumulated_results + [-1])
            numbers = list(map(int, test_lines[index + 1].strip().split()))
            if len(numbers) != count:
                return process_tests(test_lines, index + 2, n_cases, accumulated_results + [-1])
            result = sum_of_powers(numbers)
            return process_tests(test_lines, index + 2, n_cases, accumulated_results + [result])
        except ValueError:
            return process_tests(test_lines, index + 2, n_cases, accumulated_results + [-1])

    def sum_of_powers(nums):
        def helper(lst):
            if not lst:
                return 0
            head, *tail = lst
            return (head ** 4 if head <= 0 else 0) + helper(tail)
        return helper(nums)

    lines = sys.stdin.read().splitlines()
    all_lines = read_input(lines)
    if not all_lines:
        return

    try:
        n_cases = int(all_lines[0])
        results = process_tests(all_lines[1:], 0, n_cases, [])
        print("\n".join(map(str, results)))
    except ValueError:
        pass


if __name__ == "__main__":
    main()
