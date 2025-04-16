import numpy as np
import matplotlib.pyplot as plt

sales_data = np.array([
    [1,2000, 1500, 1800, 1700, 2200],   # Day 1
    [2, 5000, 2300, 1900, 2400, 2800],   # Day 2
    [3,6000, 2100, 2500, 2200, 2600],   # Day 3
    [4,10000, 3200, 2700, 3000, 3500],  # Day 4
    [5,8000, 2900, 3100, 2700, 3300],   # Day 5
])

print(sales_data.sum)
print(sales_data.mean)
print(sales_data[:2])  ##fancy way of writing code
print (sales_data[:2,:])

# ##finding total sum

print (np.sum(sales_data,axis=0))
yearly_total =np.sum(sales_data[:,1:],axis=0)
print("yearly",yearly_total)

# ##Minimum sales per resturant

min_sales=np.min(sales_data[:,:],axis=1)
print("min",min_sales)
##maxximum sales per year
max_sale=np.max(sales_data[:,1:],axis=0)
print("max" ,max_sale)


##Average sales per resturant 
avg_sales=np.mean(sales_data[:,:],axis=1)
print("average",avg_sales)
plt.figure(figsize=(5,6))
plt.plot(np.mean(avg_sales,axis=0))
plt.title("average cumsum accross all of them ")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()


# ##cumsum

cumsum=np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)
plt.figure(figsize=(5,6))
plt.plot(np.mean(cumsum,axis=0))
plt.title("average cumsum accross all of them ")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()

#vector multiplication

vector1=np.array([1,2,3,4])
vector2=np.array([5,6,7,8])

print("vector mulitplication",(vector1 * vector2))


restaurant_sales = np.array([
    [1, 2000, 1500, 1800, 1700, 2200],
    [2, 5000, 2300, 1900, 2400, 2800],
    [3, 6000, 2100, 2500, 2200, 2600],
    [4,10000, 3200, 2700, 3000, 3500],
    [5, 8000, 2900, 3100, 2700, 3300],
    [6, 7500, 3100, 3300, 2800, 3600],
    [7, 7200, 3000, 3200, 2750, 3450],
    [8, 8100, 2950, 3100, 2600, 3550],
    [9, 8500, 3050, 3000, 2900, 3700],
    [10, 9000, 3150, 2950, 2850, 3800],
])

days = restaurant_sales[:, 0]
sales = restaurant_sales[:, 1:]

plt.figure(figsize=(8, 5))
for i in range(sales.shape[1]):
    plt.plot(days, sales[:, i], marker='o', label=f'Restaurant {i+1}')
plt.title("Restaurant Performance Over Days")
plt.xlabel("Day")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


total_per_day = np.sum(sales, axis=1)

plt.figure(figsize=(8, 4))
plt.bar(days, total_per_day, color='teal')
plt.title("Overall Daily Sales from All Restaurants")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 4))
plt.imshow(sales, cmap='YlGnBu', aspect='auto')
plt.colorbar(label='Sales Value')
plt.title("Heatmap: Restaurant Sales by Day")
plt.xlabel("Restaurant")
plt.ylabel("Day")
plt.tight_layout()
plt.show()


plt.figure(figsize=(9, 5))
plt.stackplot(days, sales.T, labels=[f'Restaurant {i+1}' for i in range(sales.shape[1])])
plt.title("Stacked View: Sales Trends by Restaurant")
plt.xlabel("Day")
plt.ylabel("Sales Value")
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
