# Kyabaat - Local Setup (Beginner Friendly)

# Here is the full demo of our website
🌐 [Kyabaat](https://kyabaat.onrender.com/)

This is a small Flask app that uses MongoDB (PyMongo).

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
  - View their cart through the **Navbar Cart Icon**  
  - Remove or update items in the cart  
  - And check their order history in **Profile Page**

### 🛒 Checkout & Payment
- Users proceed to **Checkout**
- Choose a **Payment Option**
- Receive a generated **Order ID** after successful payment

---

## 🛠️ Admin Panel

![alt text](static/images/image-3.png)
### 🔐 Admin Dashboard
Logging in with admin credentials redirects the user to the **Admin Channel**.

### ✏️ Menu Management
Admins can:
- **Add new food items**
- View all items under the **View** tab
- **Edit** specific items
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
👍😐👎 [Feedback Form](https://forms.gle/RnkkazNPhyC73pob7)
