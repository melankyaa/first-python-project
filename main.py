from flask import Flask, render_template

app = Flask(__name__)

cards_data = [
    {
        'title': 'caesar salad',
        'text': 'a classic and refreshing dish known for its crisp texture and rich, creamy flavor.',
        'imageSrc': 'https://cdn.loveandlemons.com/wp-content/uploads/2024/12/caesar-salad.jpg'
    },
    {
        'title': 'khinkali',
        'text': 'Khinkali are traditional Georgian dumplings, often considered one of the countrys signature dishes. They are flavorful, hearty, and perfect for anyone who enjoys a comforting, savory bite.',
        'imageSrc': 'https://kulinaria.ge/media/recipe-images/2017/04/xinkali.jpg'
    },
    {
        'title': 'beef',
        'text': 'Beef is the meat derived from cattle, and its one of the most widely consumed types of meat in the world.',
        'imageSrc': 'https://embed.widencdn.net/img/beef/gh6lzohosy/exact/Ridiculously%20Tasty%20Roast%20Beef%2002.tif?keep=c&u=7fueml'
    },
    {
        'title': 'acharuli khachapuri',
        'text': 'a delicious and iconic dish from Georgia, a country in the Caucasus region. Its a type of Khachapuri (a traditional Georgian cheese-filled bread), but with a unique twist.',
        'imageSrc': 'https://bittmanproject.com/wp-content/uploads/GettyImages-1207355985-1600x1067.jpg'
    },
    {
        'title': 'pizza',
        'text': 'Pizza is one of the most beloved and iconic dishes around the world. Originating in Italy, its a savory dish typically made with a round, flat dough base topped with a variety of ingredients, baked in an oven.',
        'imageSrc': 'https://www.allrecipes.com/thmb/0xH8n2D4cC97t7mcC7eT2SDZ0aE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6776_Pizza-Dough_ddmfs_2x1_1725-fdaa76496da045b3bdaadcec6d4c5398.jpg'
    },
    {
        'title': 'taco',
        'text': 'A taco is a quintessential Mexican dish known for its versatility, bold flavors, and simplicity. Its essentially a folded or rolled tortilla filled with a variety of fillings, toppings, and condiments.',
        'imageSrc': 'https://danosseasoning.com/wp-content/uploads/2022/03/Beef-Tacos-1024x767.jpg'
    },
    {
        'title': 'Breast with Red Wine Sauce',
        'text': 'Breast with Red Wine Sauce typically refers to a dish where a chicken breast (or sometimes duck breast) is cooked and served with a rich, flavorful red wine sauce.',
        'imageSrc': 'https://img.taste.com.au/ezVPv-Cn/w720-h480-cfill-q80/taste/2016/11/duck-breast-with-spiced-red-wine-and-orange-sauce-83452-1.jpeg'
    },
    {
        'title': 'Spaghetti Bolognese',
        'text': 'Spaghetti Bolognese is a classic Italian dish that features a rich, flavorful meat sauce served over a bed of pasta.',
        'imageSrc': 'https://www.maggi.co.nz/sites/default/files/styles/home_stage_944_531/public/srh_recipes/c8c982f9afbe1f16d6a432d70b3affa4.jpg?h=bbce836c&itok=T4bDlldj'
    }
]

@app.route('/')
def index():
    return render_template('index.html', cards=cards_data)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)