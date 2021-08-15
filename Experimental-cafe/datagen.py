import os, sys, random
from time import sleep
import time
from copy import deepcopy
from itertools import islice
from mysqlwork import Database, Pretty_print, Write_csv
from termcolor import cprint

writer = Write_csv()
data = Database()
printer = Pretty_print()


def print_prod_db():
    prod_result = data.load_product()
    if prod_result == []:
        print(f'\nYou have no item in stock')
    elif len(prod_result) == 1:
        print(f'\nYou have {len(prod_result)} item in stock: \n\n{prod_result}\n')
    else:
        print(f'\nYou have {len(prod_result)} items in stock: \n\n{prod_result}\n')

def print_cour_db():
    cour_result = data.load_courier()       
    if cour_result == []:
        print(f'\nYou have no courier service')
    elif len(cour_result) == 1:
        print(f'\nYou have {len(cour_result)} courier in your service today: \n\n{cour_result}\n')    
    else:
        print(f'\nYou have {len(cour_result)} couriers in your service today: \n\n{cour_result}\n')

    
def instructions():
    '''This displays a set of instructions'''
    cprint('\nWELCOME TO ORDERIT', 'yellow', attrs=['blink'])
    print('\nPlease follow the following instructions')
    print()
    print('##########################################')
    print()


def main_function():
    
    use_prod_list = deepcopy(data.load_product())
    use_cour_list = deepcopy(data.load_courier())
    use_ord_dict = deepcopy(data.load_order())
    prod_dict = {}
    cour_dict = {}
    
    while True: # The app keeps running until users input 0 in the main menu or encounter uncaught error
        try:
            user_input = int(input('Input 0 to exit the app and save your progress \n1 to progress to product menu \n2 to courier menu \n3 to order menu: '))
        except Exception:
            print('\nPlease, input an integer\n')
            continue
        
        if user_input == 1: #progress to product menu
                        
            def user_input_1():
                
                print()
                try:
                    user_input_2 = int(input('Input: \n0 to return to main menu \n1 to print product menu \
                                        \n2 to add a new product and display stock \n3 to print index and items in stock, and update items \
                                        \n4 to remove an item from stock \n5 to clear the screen \
                                        \n6 to clear stock: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return user_input_2
            
            input_result_prod = user_input_1()
            
            if input_result_prod == 1: #print product list
                print()
                if use_prod_list:
                    print(f'You have {use_prod_list} in stock\n')
                else:
                    print(f'You have no product in stock\n')
            
            elif input_result_prod == 2: #get new item
                
                def if_user_input_is_2():
                    print()
                    user_input_3 = input('Type in the name of the item you wish to add: ').lower()
                    user_input_3_price = input('Type in the price of the item you wish to add: ')
                    prod_dict.clear()
                    prod_dict['product_id'] = int(use_prod_list[-1]['product_id']) + 1
                    prod_dict['item_name'] = user_input_3
                    prod_dict['price'] = float(user_input_3_price) if '.' in user_input_3_price else int(user_input_3_price)
                    copy_product_dict = deepcopy(prod_dict)
                    use_prod_list.append(copy_product_dict)
                    
                    print(f'\nYou now have {use_prod_list} in stock\n')
                
                if_user_input_is_2()
                
            elif input_result_prod == 3: #update product list
                
                def if_user_input_is_3():
                    
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index + 1), '\t', str(items))
                        print()
                        try:
                            user_input_ind = int(input(f'you may update your items \nInput the product id of the item you wish to update: '))
                            user_input_item = input('\nPlease, type in the replacement name: ')
                            user_input_item_price = input('\nPlease, type in the item price: ')
                            
                            if user_input_item:
                                prod_dict.clear()
                                prod_dict['item_name'] = user_input_item
                                prod_dict['price'] = float(user_input_item_price) if '.' in user_input_item_price else int(user_input_item_price)
                                copy_product_dict2 = deepcopy(prod_dict)
                                use_prod_list[user_input_ind - 1] = copy_product_dict2
                                print()
                                print(f'You now have {use_prod_list} in stock\n')
                            else:
                                print('\nItem name missing; thus, item not added. Returning to main menu\n')
                        except Exception as ex:
                            print(f'\n {ex} \n')      
                            print('Returning to main menu\n')
                
                    else:
                        print('\nNo product in stock yet\n')
                        
                if_user_input_is_3()    
                
            elif input_result_prod == 4: #delete product
                
                def if_user_input_is_4():
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index + 1), '\t', str(items))
                        print()
                        
                        get_info = f'Please, input the product id to remove your product: '
                        try:
                            new_user_input_ind = int(input(get_info))
                            del use_prod_list[new_user_input_ind - 1]
                            if use_prod_list:
                                print(f'\nYou now have {use_prod_list} in stock\n')
                            else:
                                print(f'\nYou now have no product in stock\n')  
                        except IndexError as e: 
                            print(f'\n {e} \n')
                            print('Returning to main menu\n')
                        except ValueError:
                            print('\nPlease, input an integer\n')
                            print('Returning to main menu\n')
       
                    else:
                        print('\nYou cannot delete any product as your stock is empty\n')
                        
                if_user_input_is_4()
                    
            elif input_result_prod == 5:
                os.system('cls || clear')
                
            elif input_result_prod == 6:
                use_prod_list.clear()
                print(f'\nYour stock is now empty\n')
                
            elif not input_result_prod: # If the user input 0 above
                print()
                print_product_menu = instructions()
            else:
                print('\nPlease, you should type in a number between 0 and 6\n')
                
        elif user_input == 2:
            
            def user_input_2():
                print()
                try:
                    sub_user_input = int(input('Input: \n0 to return to main menu \n1 to print courier list \
                                            \n2 to add a new courier and print list \n3 to print index and names in your courier and update courier \
                                            \n4 to remove a courier \n5 to clear the screen \
                                            \n6 to clear courier list: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return sub_user_input
            
            input_result_cour = user_input_2()
            
            if input_result_cour == 1:
                if use_cour_list:
                    if len(use_cour_list) == 1:
                        print(f'\nYou have {use_cour_list} courier at your service\n')
                    else:
                        print(f'\nYou have {use_cour_list} couriers at your service\n')
                else:
                    print(f'\nYou have no courier service\n')
                
            elif input_result_cour == 2:
                
                def if_user_input_2_is_2():
                    
                    sub_user_input_3 = input('\nPlease, type in a courier name to add to your service: ').title()
                    sub_user_input_3_ph = input('Please, type in the courier phone number: ')
                    cour_dict.clear()
                    cour_dict['courier_id'] = int(use_cour_list[-1]['courier_id']) + 1
                    cour_dict['courier'] = sub_user_input_3
                    cour_dict['phone'] = sub_user_input_3_ph
                    copy_courier_dict1 = deepcopy(cour_dict)
                    use_cour_list.append(copy_courier_dict1)
                
                    if len(use_cour_list) == 1:
                        print(f'You now have {use_cour_list} courier at your service\n')
                    else:
                        print(f'\nYou now have {use_cour_list} couriers at your service\n') 
                
                if_user_input_2_is_2()
                
            elif input_result_cour == 3:
                
                def if_user_input_2_is_3():
                    
                    if use_cour_list:
                        print()
                        print('index \t courier')
                        for index, items in enumerate(use_cour_list):
                            print(str(index + 1), '\t', str(items))
                        print()   
                     
                        try:
                            sub_user_input_ind = int(input(f'you may update your courier service \nInput the courier_id for the courier you wish to update: '))
                            sub_user_input_name= input('\nPlease, type in the replacement: ')
                            sub_user_input_ph = input('\nPlease, type in the courier phone number: ')
                            
                            if sub_user_input_name:
                                cour_dict.clear()
                                cour_dict['courier'] = sub_user_input_name
                                cour_dict['phone'] = sub_user_input_ph
                                copy_courier_dict2 = deepcopy(cour_dict)
                                use_cour_list[sub_user_input_ind - 1] =  copy_courier_dict2
                                print()
                                print(f'You now have {use_cour_list} at your courier service\n')
                            else:
                                print('\nCourier name missing; thus, courier not added. Returning to main menu\n')
                                
                        except Exception as ex:
                            print(f'\n {ex} \n')
                            print('Returning to main menu\n')
                    else:
                        print('\nNo courier in service yet\n')
                                                    
                if_user_input_2_is_3()
                                                            
            elif input_result_cour == 4:   
                
                def if_user_input_2_is_4():
                    if use_cour_list:
                        print()
                        print('index \t courier')
                        for index, items in enumerate(use_cour_list):
                            print(str(index + 1), '\t', str(items))
                        print()
                        get_info_cour = f'Input the courier id for the courier you wish to remove: '
                        
                        try:
                            new_user_cour_ind = int(input(get_info_cour))
                            del use_cour_list[new_user_cour_ind - 1]
                            if use_cour_list:
                                print(f'\nYou now have {use_cour_list} at your courier service\n')
                            else:
                                print(f'\nYou now have no courier service\n')
                        except IndexError as e:
                            print(f'\n {e} \n')
                        except ValueError:
                            print('\nPlease, input an integer\n')
                            print('Returning to main menu\n')
                            
                    else:
                        print('\nYou cannot delete any courier as you have none\n')
                        
                if_user_input_2_is_4()
                    
            elif input_result_cour == 5:
                os.system('cls || clear')
            
            elif input_result_cour == 6:
                use_cour_list.clear()
                print(f'\nYou now have no courier service\n')
          
            elif not input_result_cour:
                print_courier_menu = instructions()
            else:
                print('\nPlease, type in a number between 0 and 6')   
                
        elif user_input == 3:
            
            def user_input_3():
                print()
                try:
                    ord_user_input = int(input('Input: \n0 to return to main menu \n1 to print list of available orders \
                                        \n2 to add your order \n3 to print index, available orders, and change your order status \
                                        \n4 to change your order \n5 to delete your order \
                                        \n6 to clear the screen: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return ord_user_input
             
            input_result_ord = user_input_3() 
                
            if input_result_ord == 1:
                if use_ord_dict:
                    if len(use_ord_dict) == 1:
                        print(f'\nYou have this order: {use_ord_dict}\n')
                    else:
                        print(f'\nYou have the following orders: {use_ord_dict}\n')
                else:
                    print(f'\nThere is no order\n')

            elif input_result_ord == 2: #add order
                
                def if_user_input_3_is_2():
                    print()
                    ord_user_input_name = input('Please, type in your full name: ').title()
                    ord_user_input_add = input('Please, type in your address: ').title()
                    ord_user_input_ph = input('Please, type in your phone number: ')
                    
                    if use_prod_list:
                        print('\nindex \t product category')
                        for index, items in enumerate(use_prod_list):
                            print(str(index + 1), '\t', str(items))
                        print()
                        
                        ord_user_input_item = input(f'Please, make an order by inputting the product id from the categories above \
                                \nYou can make multiple orders by inserting ids separated by commas: ')
                        try:
                            int_ord_user_input_item = [int(i) for i in ord_user_input_item.strip(' ').split(',')]
                        except Exception as e:
                            print(f'\n {e} \n')
                            
                    # if use_prod_list:
                        print('\nindex \t couriers')
                        if use_cour_list:
                            temp_cour_list = use_cour_list
                            for index, courier in enumerate(use_cour_list):
                                print(str(index + 1), '\t', str(courier))
                    
                            ord_user_input_cour = input(f'\nPlease, choose a courier by inputing the courier id from the available courier(s) above: ').title()
                            try:
                                ord_user_input_cour_try = int(ord_user_input_cour)
                            except Exception as e:
                                print(e)
                            else:
                                ord_user_input_cour_choice = temp_cour_list[ord_user_input_cour_try -1]['courier']
                            print()
                            ord_status = 'PREPARING'
                            cprint('\nWELCOME TO ORDERIT', 'yellow', attrs=['blink'])
                            print()
                            printer.blink(3, ord_status)
                            printer.loading()
                            printer.order_stat(d=ord_status)
                            print()
                            
                            mini_ord_dict = {}
                            mini_ord_dict_items = {'item_id': []}
                            mini_ord_dict['order_id'] = int(use_ord_dict[-1]['order_id']) + 1
                            mini_ord_dict['name'] = ord_user_input_name 
                            mini_ord_dict['address'] = ord_user_input_add 
                            mini_ord_dict['phone'] = ord_user_input_ph
                            mini_ord_dict['courier'] = ord_user_input_cour_choice
                            mini_ord_dict['status'] = ord_status
                            mini_ord_dict_items['item_id'].extend(int_ord_user_input_item) #extend instead of append; so users can choose 1 or more products
                            
                            for id in mini_ord_dict_items['item_id']:
                                mini_ord_dict['item_id'] = id #add product id to dictionary
                                use_ord_dict.append(deepcopy(mini_ord_dict)) #deepcopy here prevents appending only last dict
                            print(f'\n{use_ord_dict}\n')
                            
                        else:
                            print('No courier available to pickup your order at the moment. Check back in few minutes')    
                            
                    else:
                        print('\nDue to recent surge in demand we have no product in stock. We will refill in 2 hours and alert you\n')   
                    
                if_user_input_3_is_2() 
                        
            elif input_result_ord == 3: #change order status
                
                def if_user_input_3_is_3():
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index + 1), '\t', str(items))
                        print()
                        try:
                            order_user_input_ind = int(input(f'you may change your order status\nInput the order id of your order: '))
                            print('Your order is: ', use_ord_dict[order_user_input_ind - 1])
                            print(f'\nFind below available order status options : \n')
                            ord_status_sample = ['OUT FOR DELIVERY', 'DELIVERED', 'DELAYED', 'CANCELLED']
                            print('Index \t Status')
                            for index, items in enumerate(ord_status_sample):
                                print(str(index + 1), '\t', str(items))
                            print()
                                
                            order_user_input_index = int(input('Input the index number from above to replace order status : '))
                            use_ord_dict[order_user_input_ind - 1]['status'] = ord_status_sample[order_user_input_index - 1]
                            print()
                            print(f'Your order status has been updated: ', use_ord_dict[order_user_input_ind -1])
                        except Exception as ex:
                            print(ex)
                    else:
                        print('\nThere is no order yet\n')
                        
                if_user_input_3_is_3()
                        
            elif input_result_ord == 4: #update order
                
                def if_user_input_3_is_4():
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index + 1), '\t', str(items))
                        print()
                        try:
                            ord_user_input_ind = int(input(f'You may change your existing order\nInput your order id from the above list: '))
                            print('\nYour order is: ', use_ord_dict[ord_user_input_ind - 1])
                            ord_user_input_item = input('\nPlease, type in the order category you wish to change: ')
                            new_ord_user_input_item = input('\nPlease, type in the replacement: ')
                            
                            if new_ord_user_input_item:
                                use_ord_dict[ord_user_input_ind - 1][ord_user_input_item] = new_ord_user_input_item
                                print('\nYour updated order is: ', use_ord_dict[ord_user_input_ind - 1])
                                print()
                            else:
                                print('\nOrder category missing; thus, order not updated. Returning to main menu')
                                
                        except Exception as e:
                            print(f'\n {e} \n')
                    else:
                        print('\nThere is no order yet')

                if_user_input_3_is_4()
                
            elif input_result_ord == 5: #delete order
                
                def if_user_input_3_is_5():
                    
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index), '\t', str(items)) 
                            
                            get_del_ord_ind = f'Please, input your order id to remove your order\nor -1 if your order is not here: ' 
                        try:
                            print()
                            new_user_input_ind = [int(i) for i in input(get_del_ord_ind).strip(' ').split(',')] #in case users have multiple items #int(input(get_del_ord_ind))
                            if new_user_input_ind == -1:
                                pass 
                            else: 
                                for i in new_user_input_ind:
                                    del use_ord_dict[i - 1]
                                print(f'\nYour order has been deleted\n')
                            
                        except IndexError as e:
                            print(f'\n {e} \n')
                            print('Returning to main menu\n')
                        except ValueError:
                            ('\nPrint, please input an integer\n')
                            print('Returning to main menu\n')
                            
                    else:
                        print('\nThere is no order yet\n')
                             
                if_user_input_3_is_5()    
                    
            elif input_result_ord == 6:
                os.system('cls || clear')
                
            elif not input_result_ord: # If the user input 0 above
                print()
                print_courier_menu = instructions()
            else:
                print('\nPlease, type in a number between 0 and 6\n')     
                        
        elif not user_input: #After every operation, users can input 0 to save and exit
            
            """Call class Database setters and getters methods to take items for inserting in database
            We need two functions for this: one to remove all PKs from dicts and second that returns the list of tuples needed"""

            def id_remover(dict_list, id): #Remove ids form the list of dictionaries
                for dct in dict_list:      #So, the database will autoincrement the id columns
                    dct.pop(id, None)  
                return dict_list
            
            def chunk(it, size): #Returns a list of tuples to pass to to cursor.execute() in pymysql
                it = iter(it)
                return iter(lambda: tuple(islice(it, size)), ())

            it_prod = [v for item_dict in id_remover(deepcopy(use_prod_list), 'product_id') for v in item_dict.values() if item_dict] #ignore empty dicts
            it_cour = [v for item_dict in id_remover(deepcopy(use_cour_list), 'courier_id') for v in item_dict.values() if item_dict]
            it_ord = [v for item_dict in id_remover(deepcopy(use_ord_dict), 'order_id') for v in item_dict.values() if item_dict] 

            def data_product():
                data.val_prod = list(chunk(it_prod, 2))
                return data.val_prod
            
            def data_courier():
                data.val_cour = list(chunk(it_cour, 2))
                return data.val_cour
            
            def data_order():
                data.val_ord = list(chunk(it_ord, 6))
                return data.val_ord
            
            # Each class Database insert method has a getter variable named val_prod or val_cour or val_ord
                    
            inv_writer = data.insert_product #database inserter functions from class Database
            cou_writer = data.insert_courier 
            ord_writer = data.insert_order
            
            # Each class Writer_csv writer method has a getter variable named val_prod_csv or val_cour_csv or val_ord_csv
            writer.val_prod_csv = use_prod_list
            writer.val_cour_csv = use_cour_list
            writer.val_ord_csv = use_ord_dict
            
            inv_writer_csv = writer.inventory_writer_csv #csv_writer functions from class Write_csv
            cou_writer_csv = writer.courier_writer_csv
            ord_writer_csv = writer.order_writer_csv
            
            """All setter functions will only be called when needed. Each will then fill
               in the getter variable. This is advantageous as it won't attempt the costly
               operation of writing empty strings to database. This is also true for the csv writers
            """
            
            if use_prod_list and use_cour_list and use_ord_dict:                
                data_product(), data_courier(), data_order()    
                return inv_writer(), cou_writer(), ord_writer(), inv_writer_csv(), cou_writer_csv(), ord_writer_csv() 
            
            elif use_prod_list and use_cour_list and not use_ord_dict:
                data_product(), data_courier()
                return inv_writer(), cou_writer(), inv_writer_csv(), cou_writer_csv()
                
            elif use_prod_list and use_ord_dict and not use_cour_list:
                data_product(), data_order() 
                return inv_writer(), ord_writer(), inv_writer_csv(), ord_writer_csv()
            
            elif use_cour_list and use_ord_dict and not use_prod_list:
                data_courier(), data_order() 
                return cou_writer(), ord_writer(), cou_writer_csv(), ord_writer_csv()
            
            elif use_prod_list:
                data_product()
                return inv_writer(), inv_writer_csv()
            
            elif use_cour_list:
                print(use_cour_list)
                data_courier()
                return cou_writer(), cou_writer_csv()
            
            elif use_ord_dict:
                data_order()
                return ord_writer(), ord_writer_csv()
                        
            else:
                raise SystemExit
        else:
            print('\nPlease input an integer between 0 and 3\n')        
    
if __name__ == '__main__':
    instructions() 
    print_prod_db() 
    print_cour_db()  
    main_function() 
    