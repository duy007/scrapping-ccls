import pandas

def solution(data, n): 
    if (len(data) < 100):
        if type(data) is not list:
            data = list(data)
        count = {}
        for i in range(len(data)):
            if data[i] in count:
                count[data[i]] += 1
            else:
                count[data[i]] = 1
        for num in count:
            if count[num] > int (n):
                for i in range(count[num]):
                    data.remove(num)
        return data

data = solution([5, 10, 15, 10, 7], 2)
print(data)

print(pandas.__version__)

# added a comment