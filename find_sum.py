
def find_sum_fast(arr, k):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == k:
            return [arr[left], arr[right]]
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return []

def find_sum_slow(arr, k):
    return next(([x, y] for x in arr for y in arr if x + y == k), [])

if __name__ == "__main__":
    arr1 = [-3, -2, 0, 2, 4, 5]
    k1 = 2
    print(f"Массив: {arr1}, K = {k1}")
    print(f"Результат (медленный): {find_sum_slow(arr1, k1)}")
    print(f"Результат (быстрый): {find_sum_fast(arr1, k1)}")
    
    arr2 = [-1, 0, 2, 3, 4]
    k2 = 3
    print(f"\nМассив: {arr2}, K = {k2}")
    print(f"Результат (медленный): {find_sum_slow(arr2, k2)}")
    print(f"Результат (быстрый): {find_sum_fast(arr2, k2)}") 