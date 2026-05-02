def mySqrt(x: int) -> int:
    # Edge case
    if x < 2:
        return x

    left, right = 1, x // 2
    ans = 1
    step = 0  # đếm số bước để minh hoạ

    print(f"Tìm sqrt({x}), tìm kiếm trong [{left}, {right}]")
    print("-" * 45)

    while left <= right:
        step += 1
        mid = (left + right) // 2

        print(f"Bước {step}: left={left}, right={right}, "
              f"mid={mid}, mid²={mid*mid}")

        if mid * mid == x:
            print(f"→ Tìm thấy chính xác! sqrt({x}) = {mid}")
            return mid
        elif mid * mid < x:
            ans = mid
            left = mid + 1
            print(f"→ {mid}² < {x}, lưu ans={ans}, tìm bên phải")
        else:
            right = mid - 1
            print(f"→ {mid}² > {x}, tìm bên trái")

    print(f"\n→ Kết quả làm tròn xuống: {ans}")
    return ans


# ========== Test Cases ==========
test_cases = [0, 1, 4, 8, 16, 25, 26, 2147395599]

for x in test_cases:
    print(f"\n{'='*45}")
    result = mySqrt(x)
    print(f"mySqrt({x}) = {result}")