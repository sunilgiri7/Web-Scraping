from bs4 import BeautifulSoup
import requests
import pickle
import sys

# If ascess is denied we use this line
# # headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

print("<h1>Gaming Producta</h1>")
print("Put some product name that you don't want to see")
unwanted = input(">")
print(f'Filtering Out {unwanted} For You....')
html_text = requests.get('https://www.flipkart.com/gaming/pr?sid=4rr&fm=neo%2Fmerchandising&iid=M_afd8e33c-5ce0-45c1-bf68-5418a2051d8a_1_372UD5BXDFYS_MC.T6Z44HHCR56C&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Gaming~All_T6Z44HHCR56C&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=T6Z44HHCR56C').text
soup = BeautifulSoup(html_text, 'html.parser')
# product = soup.find('div', class_='_13oc-S')
product = soup.find('div', class_='_1YokD2 _3Mn1Gg')

data = []
for gaming in product:
    product_name_tags = gaming.find('a', class_='s1Q9rs')
    product_name = product_name_tags.text if product_name_tags else "No Name Avilable"

    product_rating_tags = gaming.find('span', class_='_1lRcqv')
    product_rating = product_rating_tags.text if product_rating_tags else "No Rating Avilable"

    product_price_tags = gaming.find('div', class_='_30jeq3')
    product_price = product_price_tags.text if product_price_tags else "No Price Avilable"

    product_discount_tags = gaming.find('div', class_='_3Ay6Sb')
    product_discount = product_discount_tags.text if product_discount_tags else "No Discount Avilable"

    more_info = gaming.find('herf', class_='s1Q9rs')
    # more_info = more_info_tags.text if more_info_tags else "No Link Avilable"

    if unwanted not in product_name:
            print(f'''product_name': {product_name.strip()}
            'Product_Price': {product_price.strip()}
            'Product_Rating': {product_rating.strip()}
            'Product_Discount': {product_discount.strip()}
            'More_Info': {more_info}''')
            print('')
            
#         data.append({
            # 'product_name': product_name.strip(),
            # 'product_price': product_price.strip(),
            # 'product_rating': product_rating.strip(),
            # 'product_discount': product_discount.strip(),
            # 'more_info': more_info
#         })

# # Pickle the data
# with open('gaming_products.pkl', 'wb') as f:
#     pickle.dump(data, f)