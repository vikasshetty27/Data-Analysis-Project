import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
# Preparing data for combined bar chart visualization 
f
 ig = make_subplots(rows=1, cols=1, shared_xaxes=True, subplot_titles=["Platform Comparison 
Metrics"]) 
# Adding User Rating Bar 
f
 ig.add_trace(go.Bar( 
x=platform_means['Platform'], 
y=platform_means['User_Rating'], 
name='User Rating', 
marker_color='blue' 
)) 
# Adding Price Consistency Bar 
f
 ig.add_trace(go.Bar( 
x=platform_means['Platform'], 
y=platform_means['Price_Consistency'], 
name='Price Consistency', 
marker_color='orange' 
)) 
# Adding Customer Service Bar 
f
 ig.add_trace(go.Bar( 
x=platform_means['Platform'], 
y=platform_means['Customer_Service'], 
name='Customer Service', 
marker_color='green' 
)) 
 
# Update layout for combined bar chart 
fig.update_layout( 
    title="Platform Comparison Dashboard", 
    barmode='group', 
    xaxis_title="Platform", 
    yaxis_title="Metrics", 
    legend_title="Metrics", 
    template="plotly_white" 
) 
 
# Adding slicer functionality with dropdown menus 
fig.update_layout( 
    updatemenus=[ 
        dict( 
            type="dropdown", 
            direction="down", 
            x=1.1, 
            y=1.15, 
            showactive=True, 
            buttons=[ 
                dict(label="All Metrics", 
                     method="update", 
                     args=[{"visible": [True, True, True]}]), 
                dict(label="User Rating", 
                     method="update", 
                     args=[{"visible": [True, False, False]}]), 
                dict(label="Price Consistency", 
                     method="update", 
                     args=[{"visible": [False, True, False]}]), 
                dict(label="Customer Service", 
                     method="update", 
                     args=[{"visible": [False, False, True]}]), 
            ] 
        ) 
    ] 
) 
 
# Adding 3D Scatter plot 
scatter_3d = px.scatter_3d( 
    data_combined, 
    x='User_Rating', 
    y='Price_Consistency', 
    z='Customer_Service', 
    color='Platform', 
    symbol='Category', 
    title="3D Scatter Plot: Metrics Comparison", 
    labels={"x": "User Rating", "y": "Price Consistency", "z": "Customer Service"} 
) 
 
# Save the visualizations as an HTML file 
dashboard_path = "/mnt/data/ECommerce_Dashboard.html" 
fig.write_html(dashboard_path) 
scatter_3d.write_html(dashboard_path, include_plotlyjs="cdn", full_html=True) 
 
dashboard_path 