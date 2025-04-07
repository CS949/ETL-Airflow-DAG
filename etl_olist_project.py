def run_etl():
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    os.makedirs("reports", exist_ok=True)

    orders = pd.read_csv("data/orders.csv")
    order_items = pd.read_csv("data/order_items.csv")
    customers = pd.read_csv("data/customers.csv")
    reviews = pd.read_csv("data/order_reviews.csv")
    payments = pd.read_csv("data/order_payments.csv")

    total_orders = len(orders)
    total_customers = customers['customer_id'].nunique()
    average_review_score = reviews['review_score'].mean()
    total_items_sold = len(order_items)

    print("Total Orders:", total_orders)
    print("Total Customers:", total_customers)
    print("Average Review Score:", round(average_review_score, 2))
    print("Total Items Sold:", total_items_sold)
    
    merged = orders.merge(order_items, on="order_id")
    merged = merged.merge(payments, on="order_id")
    merged = merged.merge(customers, on="customer_id")

    clv_df = merged.groupby("customer_unique_id")['payment_value'].sum().reset_index()
    clv_df.columns = ['customer_unique_id', 'CLV']
    average_clv = clv_df['CLV'].mean()
    print("Average CLV:", round(average_clv, 2))

    returned_orders = orders[orders['order_status'] != 'delivered']
    return_rate = len(returned_orders) / len(orders)
    print("Return Rate:", round(return_rate * 100, 2), "%")

    orders_with_customers = orders.merge(customers, on="customer_id")
    orders_items_region = orders_with_customers.merge(order_items, on="order_id")
    sales_by_state = orders_items_region.groupby("customer_state")["price"].sum().sort_values(ascending=False)
    print("Top 5 States by Sales:\n", sales_by_state.head())

    plt.figure(figsize=(14, 6))
    sales_by_state.plot(kind='bar', color='skyblue')
    plt.title("Total Sales by State")
    plt.xlabel("State")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("reports/sales_by_state.png")
    plt.close()

    top_10_clv = clv_df.sort_values("CLV", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_clv['customer_unique_id'], top_10_clv['CLV'], color='green')
    plt.xlabel("CLV")
    plt.title("Top 10 Customers by Lifetime Value")
    plt.tight_layout()
    plt.savefig("reports/top_10_clv_customers.png")
    plt.close()

if __name__ == "__main__":
    run_etl()
