## 🍕 Pizza Mama App 🍕

Welcome to Pizza Mama, the pizzeria app that lets you explore a delicious menu of pizzas! This app is designed to provide a seamless experience for customers, offering updated pizza information, including prices and ingredients, directly from our Django-based API.

## 🛠 Key Features

- Real-Time Menu Updates: The app automatically fetches the latest pizza data from the Django API, ensuring the menu is always up to date.

- Detailed Pizza Information: View the list of available pizzas with their prices and full ingredient details.

- Easy Integration: Uses a REST API backend to keep the app's data in sync with changes made by the admin.

## How It Works

Backend: A web application built using Django serves as the backend, where the admin can:

- Add new pizzas.

- Modify existing recipes or prices.

- Remove pizzas from the menu.

API: The Django backend exposes a RESTful API that:

- Provides endpoints to retrieve pizza data.

- Supports real-time updates for the app.

- Frontend: The mobile or web app fetches data from the API to display the menu to users.

## 🧰 Technologies Used

Frontend:

- Developed with Kivy.

Backend:

- Built using Django.

- REST framework for API endpoints.

Database MySQL:

- Stores pizza details such as name, price, and ingredients.

API:

- Used to fetch pizza details dynamically from the server.


## 🙌 Contributing

We welcome contributions! If you'd like to improve the app or fix issues:

- Fork the repository.

- Create a new branch:

- git checkout -b feature/your-feature-name

Commit your changes:

- git commit -m "Add your message here"

Push to the branch:

- git push origin feature/your-feature-name

- Open a pull request.
