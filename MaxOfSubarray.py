def max_of_subarrays(self,arr,n,k):
       
        res = []
        d = deque()
    
        #iterating over first k elements or first window of array.
        for i in range(k):
            
            #for every element, the previously smaller elements 
            #are useless so removing them from deque.
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
            
            #adding new element at back of deque.
            d.append(i)
    
        #iterating over the rest of the elements.
        for i in range(k,n):
            
            #the element at the front of the deque is the largest 
            #element of previous window, so adding it to the list.
            res.append (arr[d[0]])
            
            #removing the elements which are out of this window.
            while len(d) and d[0]<=i-k:
                d.popleft()
                
            #removing all elements smaller than the element being  
            #added currently (removing useless elements). 
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
                
            #adding new element at back of deque.
            d.append(i)
    
    
        #the element at the front of the deque is the largest 
        #element of last window, so adding it to the list.
        res.append (arr[d[0]])
        d.popleft()
        
        #returning the list.
        return res
