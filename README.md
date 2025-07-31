
# <center> Hotel Reservation System</center>
  <center> <img alt="Static Badge" src="https://img.shields.io/badge/Contributors-2-green?style=flat-square"> <img alt="Static Badge" src="https://img.shields.io/badge/Python%20Flask-FFFF00?style=flat-square">
 <img alt="Static Badge" src="https://img.shields.io/badge/PostgreSQL-008bb9?style=flat-square"> .
</center>
 
## Table of Contents
- [Overview](#overview)
	- [Built with](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgements](#Acknowledgements)
- [Developers](#developers)

## Overview

 :clipboard: This project is a collaboration side project. Made as a hotel reservation system prototype for booking guest reservations online, and built with a front desk management system. The system is designed for online bookings, track rooms, guest management, and employee management.

> ⚠️ **Note:** This project is still a work-in-progress and some features are incomplete due to contributor availability. Contributions are welcome.
 ### Built With

This section lists major frameworks/libraries used.

<img alt="Static Badge" src="https://img.shields.io/badge/Flask-FFD43B?style=for-the-badge&logo=flask&logoSize=auto">

<img alt="Static Badge" src="https://img.shields.io/badge/SQLAlchemy-white?style=for-the-badge&logo=sqlalchemy&logoSize=auto&logoColor=black">

<img alt="Static Badge" src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoSize=auto&logoColor=white">

<img alt="Static Badge" src="https://img.shields.io/badge/Redis-cc7979?style=for-the-badge&logo=redis&logoSize=auto&logoColor=white">

<img alt="Static Badge" src="https://img.shields.io/badge/TailwindCSS-a5f3fc?style=for-the-badge&logo=tailwindcss&logoSize=auto&logoColor=white">

## Features
### :notebook_with_decorative_cover:  List of features
- Assign date of check in and checkout
- Automatic computation of prices
- Track rooms
- Manage guests and reservation (Front desk role)
- Manage Employees (Admin role)
- 
> ### 🚧 In Progress / To-Do
> - Filtering of rooms in check availability
> - Design Confirmation Screen
> - CRUD Operations for reservation list
> - CRUD Operations for managing employees
## Requirements

-  #### :memo:  This app uses Python version 3.13 and above
-  #### :floppy_disk:  Install PostgreSQL 16.3, compiled by Visual C++ build 1939, 64-bit
-  #### :file_folder:  Get Package Manager: [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

 :open_file_folder: This site uses python Flask. To avoid setting up backend enviroment, the site uses Docker Container it wraps the Python dependencies into an isolate container. Follow the instructions below:
 
-  ### :github: Install via git clone.
1.  **Fork** the project
2. In your terminal, run the ``` git clone https://github.com/cent-ivan/hotel-booking-site.git```
3. Download npm, and run the ``` npm install```, to generate your own node_modules directory
4. Run this command,``` npm dev run```, to generate a tailwind file
5. Set up the backend container by running, `docker compose up -d backend` (Make sure you have Docker installed).
6. To turn off contianer, run `docker compose down`


## Usage

-  ### :minidisc:   How to Develop with Python Flask (Containerized) with Tailwind (via Host)?

1. Run `docker compose up -d backend`
2. Run this command,``` npm dev run```
3. Code some changes, save it and tailwind cli will automatically regenerate.

## Contributing

 :handshake:  The developer welcome contributions from the community! To get started:

1.  **Create a new branch** for your feature or fix:

```bash git checkout -b your-branch-name```

2.  **Add and commit** your code:

```bash
git  add  filename
git  commit  -m  "short and meaningful message"
```
3.  **Push** to your branch:

```bash git push origin your-branch-name```

4.  **Open a Pull** Request from the main repository


## Acknowledgements

-  :right_anger_bubble: Some of the Features are still in development. **This project is temporarily paused.**

## Developers
- [Kane Stephene Frogosa](https://github.com/eScayne) **🎨:man_technologist:  Front-end / UI Designer**
- [Vincent Ivan Palomata](https://github.com/cent-ivan) **⚒️:man_technologist:  Back-end**