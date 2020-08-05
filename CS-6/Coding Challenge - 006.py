#Most Water
def mostW(arr,n) : 
    arr=list(map(int,arr)) 
    res = 0;  
    for i in range(1, n - 1) :    
        left = arr[i];  
        for j in range(i) : 
            left = max(left, arr[j]);  
        right = arr[i];  
        for j in range(i + 1 , n) :  
            right = max(right, arr[j]); 
        res=res+(min(left, right) - arr[i]);
    return res;  

resList=[]
while True:
    response=input("Type 'ok' when you are done: ")
    resList.append(response)
    if response.lower()=="ok": 
        resList.pop()  
        result=mostW(resList,len(resList))
        print(result)
        break