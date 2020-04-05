
# Kendisine aktarılan bir listenin frekans tablosunu bulup tekrar eden bir fonksiyon yazınız.

# SÖZLÜK(DİCTİONARY) YÖNTEMİ

def my_frequency_dict(list):
  frequency_dict={}
  for item in list:
    if(item in frequency_dict):
      frequency_dict[item]=frequency_dict[item]+1
    else:
      frequency_dict[item]=1
  return frequency_dict

# LİSTE YÖNTEMİ

def my_frequency_list(list_1):
  frequency_list=[]
  for i in range(len(list_1)):
    s=False
    for j in range(len(frequency_list)):
      if(list_1[i]==frequency_list[j][0]):
        frequency_list[j][1]=frequency_list[j][1]+1
        s=True
    if(s==False):
      frequency_list.append([list_1[i],1])
  return frequency_list


my_list1=[2,3,2,5,8,2,8,4,1,2,2,5,8,7,2]
print(my_list1)

result_1=my_frequency_dict(my_list1)
print(result_1)

result_2=my_frequency_list(my_list1)
print(result_2)

