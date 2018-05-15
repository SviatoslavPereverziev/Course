x=int(input())
y=int(input())

if x>0 and y>0:
	print("I четверть")
	
elif x<0 and y>0:
	print("II четверть")

elif x<0 and y<0:
	print("III четверть")
	
elif x>0 and y<0:
	print("IV четверть")
	
elif x==0 and y!=0:
	print("На оси у") 
	
elif x!=0 and y==0:
	print("На оси х")
	
else:
	print("Начало координат")
	

