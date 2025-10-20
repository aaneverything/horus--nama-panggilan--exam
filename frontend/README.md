# Exam Frontend (Vue 3 + Vite)

A user management single-page application (SPA) built with Vue 3 and Vite. This app provides for managing users listing, creating, editing, and deleting user accounts, and searching or filtering users. It communicates with a backend API for data and authentication.

## What is this app?

This is a frontend single-page application (SPA) scaffold — not a backend. It is intended to serve as the client-side UI for a web application and is built for fast development and iteration. Key characteristics:

- Built with Vue 3 and Vite for fast hot-reload development.
- Client-side routing with `vue-router`, and global state management with `pinia`.
- Uses `axios` for HTTP communication with an external API (backend).
- Tailwind CSS is included as a utility-first styling tool.
- Typical use cases: admin dashboard, CRUD interfaces, user portals, and other interactive web apps that rely on a separate API.

## Quick start

Install dependencies:

```sh
npm install
```

Run the dev server:

```sh
npm run dev
```

## Tech stack (high level)

- Vue 3
- Vite
- Vue Router
- Pinia
- Axios
- Tailwind CSS
- Prettier

## Notes

- Configure API base URL and other client-visible variables using Vite env variables (prefix with `VITE_`).
- The built app outputs static files (usually to `dist/`) and can be deployed to static hosts (Netlify, Vercel, S3/CloudFront, etc.).
- This README focuses on what the app is and how to get started — extend it with project-specific details (routes, stores, components) as the application grows.
