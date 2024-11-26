product = [["1. laptop", "$1000"], ["2. phone", "$500"], ["3. headphone", "$100"]]
def main_menu():
   cart = [] 
   print("""
      Main manu
      1. View product
      2. Add to cart
      3. Remove from cart
      4. Checkout
      5. Display cart
      5. Exit""")
   print(f"you have {len(cart)} in your cart")
   
   answer = int(input(": "))
   match answer:
      case 1: view_product()
      case 2: pass
      case 3: pass
      case 4: pass
      case 5: pass


def view_product():
   cart = []
   for number in range(len(product)):
      print(f"{product[number][0]} {product[number][1]}")
   response = int(input(": "))
   match response:
      case 1: cart.append(product[0])  
      case 2: cart.append(product[1])
      case 3: cart.append(product[2])
   main_menu()


main_menu()
   
   
      
