

def output_profit_data(stock_items, no_of_items_bought, item_cost, buy_commission,
                        no_of_items_sold, item_sale_price, sale_commission):


    for number in range(0, len(stock_items)):
        #make sure you multiply the lists by index [number]
        # money spent all items
        msai = no_of_items_bought[number] * item_cost[number]
        #money earned all items
        meai = no_of_items_bought[number] * item_sale_price[number]
        # money spent buying shoes after buy commission
        msbs = item_cost[number] * no_of_items_bought[number] + (item_cost[number] * buy_commission[number])
        #money earned selling shoes after sales commission
        mess = (item_sale_price[number] * no_of_items_sold[number]) * (1 - sale_commission[number])
        #profit
        profit = mess - item_cost[number] * no_of_items_bought[number]

        
        print("================================\n")
        print(f"{no_of_items_bought[number]} {stock_items[number]} bought for £{item_cost[number]} each ( {buy_commission[number]} % Buy commission )")
        print(f"\nMoney spent buying {stock_items[number]} was £{msbs:.2f}\n ")
        print(f"{no_of_items_sold[number]} for £{item_sale_price[number]} each ( {sale_commission[number]} % sale commission ) \n ")
        print(f"Money earned selling shoes was £{mess:.2f}\n ")
        print(f"Profit for shoes was £{profit:.2f}\n ")
        print("================================")



    
#function to open purchase_data.txt
def load_purchase_data(filename):
#try exept loop
    try:
# With statement encapulates cleanup tasks on exit, So you dont have to close the file in  the code eg f.close()
        with open(filename, 'r') as f:
            stock_items = []        #list of strings local varibles. 
            no_of_items_bought = [] 
            item_cost = []          
            buy_commission = []     

            line = f.readline().strip()
            while True:
                #print(line) #debugging
                stock_items.append(line) #reads first line of stock file and then appends the line into memory.
                line = f.readline().strip()
                #print(line) #debugging
                no_of_items_bought.append(int(line))
                line = f.readline().strip()
                #print(line) #debugging
                item_cost.append(float(line))
                line = f.readline().strip()
                #print(line) #debugging
                buy_commission.append(float(line))
                line = f.readline().strip()
                if not line:
                    break
    except IOError: # on input output error
        print("Cannot open file!")
    
    return stock_items, no_of_items_bought, item_cost, buy_commission
    
    

def load_sales_data(filename):
    #try exept loop
    try:
# With statement encapulates cleanup tasks on exit, So you dont have to close the file in  the code eg f.close()
        with open(filename, 'r') as f:
            stock_items = []        #list of strings local varibles. 
            no_of_items_sold = [] 
            item_sale_price = []          
            sale_commission = []     

            line = f.readline().strip()
            while True:
                #print(line) #debugging
                stock_items.append(line) #reads first line of stock file and then appends the line into memory.
                line = f.readline().strip()
                #print(line) #debugging
                no_of_items_sold.append(int(line))
                line = f.readline().strip()
                #print(line) #debugging
                item_sale_price.append(float(line))
                line = f.readline().strip()
                #print(line) #debugging
                sale_commission.append(float(line))
                line = f.readline().strip()
                if not line:
                    break
    except IOError: # on input output error
        print("Cannot open file!")
    
    return stock_items, no_of_items_sold, item_sale_price, sale_commission

if __name__ == '__main__':
    stock_items = []        #list of strings
    no_of_items_bought = [] 
    item_cost = []          
    buy_commission = []     
    no_of_items_sold = []   
    item_sale_price = []    
    sale_commission = []

     
    stock_items, no_of_items_bought, item_cost, buy_commission = load_purchase_data("purchase_data.txt")
    #print(stock_items, no_of_items_bought, item_cost, buy_commission)
    
    stock_items, no_of_items_sold, item_sale_price, sale_commission = load_sales_data("sales_data.txt")

    output_profit_data(stock_items, no_of_items_bought, item_cost, buy_commission,
                            no_of_items_sold, item_sale_price, sale_commission)
