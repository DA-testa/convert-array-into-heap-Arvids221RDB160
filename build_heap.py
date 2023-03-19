# python3


def build_heap(data):
    swaps = []
    x= len(data)
    for i in range(x//2, -1, -1):
        swaps = heap(data, i, swaps)
    return swaps

def heap(data, i, swaps):
    n=len(data)
    min_idx=i
    z=2*i+1
    v=2*i+2
    if z<n and data[z]<data[min_idx]:
        min_idx=z
    if v<n and data[v]<data[min_idx]:
        min_idx=v
    if i != min_idx:
        data[i], data[min_idx]=data[min_idx], data[i]
        swaps.append(i,min)
        swaps = heap(data, min, swaps)
    return swaps

def main():
    
    mode=input("I or F: ")
    if mode =="I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif mode =="F":
        filename=input("File name: ")
        with open(filename, 'r') as f:
            n=int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
            assert len(data) == n
    else:
        print("Invalid input")

    swaps = build_heap(data)
    for i in range(n//2):
        if 2*i+1 < n and data[i]>data[2*i+1]:
            print("Error")
            return
        if 2*i+2 < n and data[i]>data[2*i+2]:
            print("Error")
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
