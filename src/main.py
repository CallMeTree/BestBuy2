import products
import store
import promotions


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    while True:
        print("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        option = input("Please choose a number: ")
        print("")
        # OPTION 1
        if option == "1":
            count = 1
            print("------")
            for product in best_buy.get_all_products():
                print(product.show())

                count += 1
            print("------")

        # OPTION 2
        elif option == "2":
            total_items = 0
            for product in best_buy.get_all_products():
                total_items += product.quantity
            print("---------------------------------------")
            print(f"Total of {total_items} items in store")
            print("---------------------------------------")

        # OPTION 3
        elif option == "3":
            key_loop = True  # This key loop use for exit the coming while loop
            shopping_cart = []
            while key_loop:
                try:
                    count = 1
                    print("------")
                    for product in best_buy.get_all_products():
                        print(f"{count}.", product.show())
                        count += 1
                    print("------")
                    print("When you want to finish order, enter empty text.")

                    while True:
                        try:
                            product_option = input("Which product # do you want? ")
                            if product_option == '':
                                print("-----------------")
                                print("Thanks for order!")
                                print("-----------------")
                                key_loop = False
                                break
                            if int(product_option) <= 0 or int(product_option) > len(best_buy.get_all_products()):
                                print("------")
                                print("Please enter valid option!")
                                break
                            else:
                                product_option = int(product_option) - 1

                            product_quantity = input("What amount do you want? ")
                            if product_quantity == '':
                                print("-----------------")
                                print("Thanks for order!")
                                print("-----------------")
                                key_loop = False
                                break
                            if int(product_quantity) <= 0:
                                print("------")
                                print("Please enter valid quantity!")
                                break

                            chosen_item = best_buy.get_all_products()[product_option]
                            chosen_quantity = int(product_quantity)
                            shopping_list = (chosen_item, chosen_quantity)
                            shopping_cart.append(shopping_list)
                            print("Product add to cart!")
                        except ValueError:
                            print("Please enter valid option!")
                    print(f"You order total is ${best_buy.order(shopping_cart)}")
                except products.NegativeNumber:
                    print("Error while making order! Quantity larger than what exists.")

        # OPTION 4
        elif option == "4":
            quit()
        else:
            print("Invalid option, please enter again!")


if __name__ == "__main__":
    main()



