
BAR GRAPHS WITH CUSTOMER DETAILS  
# Bar chart for User Rating 


plt.figure(figsize=(12, 6)) 
sns.barplot(data=platform_means, x='Platform', y='User_Rating') 
plt.title("Average User Rating by Platform") 
plt.ylabel("User Rating") 
plt.xlabel("Platform") 
user_rating_path = "/mnt/data/User_Rating_Bar_Chart.png" 
plt.savefig(user_rating_path) 
graph_paths.append(user_rating_path) 
plt.close() 
# Bar chart for Price Consistency


plt.figure(figsize=(12, 6)) 
sns.barplot(data=platform_means, x='Platform', y='Price_Consistency') 
plt.title("Average Price Consistency by Platform") 
plt.ylabel("Price Consistency") 
plt.xlabel("Platform") 
price_consistency_path = "/mnt/data/Price_Consistency_Bar_Chart.png" 
plt.savefig(price_consistency_path) 
graph_paths.append(price_consistency_path) 
plt.close() 
# Bar chart for Customer Service 


plt.figure(figsize=(12, 6)) 
sns.barplot(data=platform_means, x='Platform', y='Customer_Service') 
plt.title("Average Customer Service by Platform") 
plt.ylabel("Customer Service") 
plt.xlabel("Platform") 
customer_service_path = "/mnt/data/Customer_Service_Bar_Chart.png" 
plt.savefig(customer_service_path) 
graph_paths.append(customer_service_path) 
plt.close() 
graph_paths 