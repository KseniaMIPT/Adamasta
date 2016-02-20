rating = list(map(int, str(input()).split()))
rating_sort = [rating[i] for i in range(len(rating) - 1) if rating[i] !=2 and rating[i + 1] != 5] + [rating[-1]]
print(sum(rating_sort)/len(rating_sort)//1)
