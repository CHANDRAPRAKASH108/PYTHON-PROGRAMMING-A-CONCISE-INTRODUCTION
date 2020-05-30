hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
#%%
def problem2_8(temp_list):
    length=len(temp_list)
    sum=0
    for i in range(0,len(temp_list)):
        sum=sum+temp_list[i]
    average=sum/length
    print(average)
    print("High: ",max(temp_list))
    print("Low: ",min(temp_list))