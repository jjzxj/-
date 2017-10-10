def besearch(data,target):
  long=len(data)-1
  mid=int(long/2)
  high=0
  if target in data:
    while(high<=long):
      if(data[mid]==target):
        return(mid)
      elif(data[mid]>target):
        mid=mid-1
      elif(data[mid]<target):
        mid=mid+1
  else: return None
