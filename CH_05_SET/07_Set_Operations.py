
A = {1, 2, 3, 4, 5}
B = { 4, 5, 6, 7, 8}

#1.Union(|or union()) -> Combines all unique elements from both set
print(A|B)      # using | operator   -{1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))  # using functions -{1, 2, 3, 4, 5, 6, 7, 8}

#2. Intersection (& or intersection())
#Returns common elements of both set
print(A & B)              #output: {4, 5}
print(A.intersection(B))  #output: {4, 5}

#3.Difference (- or difference())
#Returns elements that are in A but no in B
print(A - B)
print(A.difference(B))    #output:{1, 2, 3}

#4.Symmetric Difference ( ^ or symmetric_difference())
#Returns elements that are in either set but not in both
print(A ^ B)
print(A.symmetric_difference(B))    #{1, 2, 3, 6, 7, 8}
