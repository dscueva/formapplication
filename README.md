# Form Submission Application

This is a full-stack application that allows users to submit a form containing their name, email, and message. The application consists of two parts: a **Next.js** frontend for submitting the form and a **FastAPI** backend using **gRPC** for processing the form data.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [License](#license)

## Overview

This project demonstrates a simple form submission system. Users can enter their details into a form on the frontend, and this data is sent to the backend via gRPC for processing. Both the frontend and backend have their own individual setup instructions in their respective directories.

- The **frontend** is built with **Next.js**, **React Hook Form**, and **TailwindCSS**.
- The **backend** is built with **FastAPI**, using **gRPC** to handle form submissions.

## Technologies Used

- **Frontend**: Next.js, React, TailwindCSS, React Hook Form, TypeScript
- **Backend**: FastAPI, gRPC, Python
- **Communication**: gRPC for communication between frontend and backend

## Project Structure

```
formapplication
├── backend         # Backend (FastAPI + gRPC)
├── frontend        # Frontend (Next.js + React)
├── README.md       # Root project README
└── LICENSE         # License information
```

For detailed setup and instructions, please refer to the respective `README.md` files in the `backend` and `frontend` directories.

## Setup and Installation

To set up the entire project, follow the instructions in the respective directories:

1. **Frontend Setup**: Navigate to the `frontend` directory and follow the instructions in its `README.md`.
2. **Backend Setup**: Navigate to the `backend` directory and follow the instructions in its `README.md`.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.