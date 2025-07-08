def birthdayCakeCandles():
    length = int(input())
    candles = list(map(int, input().split()))
    candles.sort()
    max = candles[-1]
    count = candles.count(max)
    return count

if __name__ == "__main__":
        print(birthdayCakeCandles())