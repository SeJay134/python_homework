import pandas as pd
import sqlite3

# connect to db
conn = sqlite3.connect("../db/lesson.db")

"""
line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and 
the product table. Hint: Your ON statement would be ON line_items.product_id = products.product_id.
"""
query = ("SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id")

df = pd.read_sql_query(conn, query)
print(df.head())
print()

df['total'] = df['quantity'] * df['price']
print(df.head())
print()

"""
Add groupby() code to group by the product_id. Use an agg() method 
that specifies 'count' for the line_item_id column, 'sum' for the total column, 
and 'first' for the 'product_name'. Print out the first 5 lines of the resulting DataFrame. 
Run the program to see if it is correct so far.
Sort the DataFrame by the product_name column.
"""
sum_data = df.groupby('product_id').agg({'line_item_id': 'count', 'total column': 'sum', 'product_name': 'first'})




