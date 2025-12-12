# Kyabaat - Local Setup (Beginner Friendly)

# Here is the full demo of our website
🌐 [**Kyabaat**](https://kyabaat.onrender.com/)

This is a small Flask app that uses MongoDB (PyMongo).

## 👨🏻‍👩🏻‍👦🏻‍👦🏻 Team Members

- Abhay Jajodia
- Nirmala Adhikari
- Misra Parvin Shaikh
- Paras Soni
- Pabisa Sapkota


## Quick start (macOS / Linux):

1. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python3 app.py
   ```

## Quick start (Windows):

1. (Optional but recommended) Create and activate a virtual environment:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```cmd
   python -m pip install -r requirements.txt
   ```

3. Start the app:

   ```cmd
   python app.py
   ```

## Environment Configuration (.env)

If the default MongoDB URI is not working due to IP address access issues, create or update your `.env` file with your own MongoDB URL:

```
MONGO_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/your_database
```

Replace the credentials with your actual MongoDB Atlas connection string. Make sure your IP address is whitelisted in MongoDB Atlas network access settings.

**Note:** Keep your `.env` file private and never commit it to version control (it's already in `.gitignore`).

## Features

### ⭐ Landing Page
- Features a modern auto-timed carousel.
- Allows users to **Login** or **Register**.
![alt text](static/images/image-1.png)

---

## 🔐 User Authentication
- Users can register and log in.
- Authentication system routes users based on role.
- Includes a pre-defined admin account for backend management.

**Admin Credentials**
- **Email:** admin@kyabaat.com  
- **Password:** admin123  

---

## 👤 Normal User Flow

### 🏠 Main Page
After login, normal users access the **Main Website Page**, which includes:
![alt text](static/images/image-2.png)

### 🍽️ Food Ordering System
- A large **Order Now** button leading to the menu page.
- Displays regular menu items.
- **Special Day Meals** are showcased at the top.
- Users can:
  - Browse items  
  - Add items to cart  
  - View their cart through the **Navbar Cart Icon** as 🍴
  - Remove or update items in the cart  
  - And check their order history in **Profile Page**

### 🛒 Checkout & Payment
- Users proceed to **Checkout**
- Choose a **Payment Option**
- Receive a generated **Order ID** after successful payment

## Dietary Restrictions Feature

Customers can specify their dietary preferences during checkout. This helps ensure orders are prepared according to individual needs and restrictions.

### Available Dietary Options
- **Vegan** - No animal products
- **Vegetarian** - No meat
- **Gluten-Free** - Safe for celiac disease or gluten sensitivity
- **Dairy-Free** - No milk or dairy products
- **Nut-Free** - No nuts (for nut allergies)
- **Spicy-Free** - Mild/non-spicy preparation

### How Customers Use This Feature
1. Add items to cart and click the **Cart icon** at the navbar bar 🍴
2. In the cart page, there is a option **Edit dietary**
3. Check relevant dietary restriction boxes for each food item
4. And can proceed to Billling forms
5. Dietary preferences are saved with the order in **Order History**

### Where Dietary Information is Stored
- **Order History** - Customers can view their dietary selections in past orders
- **Database** - Each order item stores the customer's selected dietary restrictions

---

## 🛠️ Admin Panel

![alt text](static/images/image-3.png)
### 🔐 Admin Dashboard
Logging in with admin credentials redirects the user to the **Admin Channel**.

### ✏️ Menu Management
Admins can:
- **Add new food items**
- View all items under the **View** tab
- **Edit** specific items clicking **Update Button**
- **Delete** food items from the menu

This provides full CRUD control over the website’s menu system.

---

## 🎨 Logo & Branding

We created a fully custom **Kyabaat Logo**, exploring:
- Multiple design concepts  
- Various color palettes  
- Branding styles  
- Modern, minimal, and expressive visual combinations  

To learn more about the logo, its design decisions, color themes, and usage guidelines, refer to:  
📄 [**kyabaat_logo_documentation.pdf**](https://github.com/abhayjajodia/full_stack_group_project_kyabaat/blob/main/Kyabaat_Logo_Documentation.pdf)

![alt text](static/images/image.png)

---

## 🗼 Accessibility & Best Practices (Lighthouse)

Lighthouse accessibility and best practice scores for all main pages (as of Dec 2025):

|Page          | Accessibility | Best Practices |
|--------------| :-----------: | :------------: |
|Landing       |     16/17     |        5/5     |
|Login         |     16/17     |        5/5     |
|Register      |     11/12     |        5/5     |
|Home          |     17/18     |        5/5     |
|About Us      |     18/19     |        5/5     |
|Contact Us    |     15/18     |        5/5     |
|Menu          |     18/18     |        5/5     |
|Cart          |     19/21     |        5/5     |
|Check Out     |     17/20     |        5/5     |
|Order         |     14/16     |        5/5     |
|Admin Add     |     17/17     |        5/5     |
|Admin View    |     16/17     |        5/5     |
|Admin Update  |     16/17     |        5/5     |

Screenshot of all Lighthouse reports are avavilable by clicking the link [**Lighthouse screenshot**](https://github.com/abhayjajodia/full_stack_group_project_kyabaat/blob/main/lighthouse_documentation.pdf)

---

## Routing Logic

1. User enters landing page → carousel plays → chooses Login/Register  
2. **Login Flow**
   - Admin credentials → `/admin`
   - Normal user → `/main`
3. **Normal User Flow**
   - Main page → Order Now → Menu → Add to Cart → Checkout → Payment → Order ID  
4. **Admin Flow**
   - Add, edit, or delete menu items  

---

## Tech Stack
*(Update as needed)*  
- **Frontend:** HTML, CSS, JavaScript / React  
- **Backend:** Python / Flask  
- **Database:** MongoDB  
- **Authentication:** Sessions  


## Please provides us your reviews or Feedback for our website
👍😐👎 [**Feedback Form**](https://forms.gle/RnkkazNPhyC73pob7)




```



