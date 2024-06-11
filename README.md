# CareerHub

**CareerHub** is a Django-based web application designed to streamline the job posting and subscription processes. It allows users to browse job listings and subscribe to newsletters for updates. This README provides an overview of the setup and functionality of the project.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Models](#models)
- [Templates](#templates)
- [Routes](#routes)
- [Contributing](#contributing)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/CareerHub.git
   cd CareerHub
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Features

- **Job Posting:** Add, view, and manage job postings with details like title, description, salary, location, and required skills.
- **Subscription:** Users can subscribe to newsletters and select their preferred frequency (daily, weekly, or monthly).
- **Admin Interface:** Django's built-in admin interface for managing job posts and subscriptions.

## Usage

### Job Posting

1. **Home Page:**
   - Displays a list of job postings.
   - Located at `/`.

2. **Job Details Page:**
   - Detailed view of a specific job.
   - Located at `/job/<slug>`.

### Subscription

1. **Subscribe Page:**
   - Form to subscribe to newsletters.
   - Located at `/subscribe/`.

2. **Thank You Page:**
   - Redirects to a thank you page after successful subscription.
   - Located at `/thank_you/`.

## Models

### `JobPost`

- `title` (CharField): Title of the job.
- `description` (TextField): Description of the job.
- `date` (DateTimeField): Date when the job was posted.
- `salary` (IntegerField): Salary offered for the job.
- `slug` (SlugField): Unique slug for the job post.
- `expiry` (DateField): Expiry date of the job post.
- `location` (OneToOneField): Location of the job.
- `author` (ForeignKey): Author of the job post.
- `skills` (ManyToManyField): Skills required for the job.
- `type` (CharField): Type of the job (Full Time or Part Time).

### `Location`

- `street` (CharField): Street address.
- `city` (CharField): City name.
- `state` (CharField): State name.
- `country` (CharField): Country name.
- `zip` (CharField): ZIP code.

### `Skill`

- `name` (CharField): Name of the skill.

### `Author`

- `name` (CharField): Name of the author.
- `company` (CharField): Company of the author.
- `designation` (CharField): Designation of the author.

### `Subscribe`

- `first_name` (CharField): Subscriber's first name.
- `last_name` (CharField): Subscriber's last name.
- `frequency` (CharField): Newsletter frequency (Daily, Weekly, Monthly).
- `email` (CharField): Subscriber's email.

## Templates

- **`JobPost/home.html`**: Template for the home page.
- **`JobPost/job_detail.html`**: Template for the job detail page.
- **`Subscribe/subscribe.html`**: Template for the subscription form.
- **`Subscribe/thank_you.html`**: Template for the thank you page.

## Routes

- **Home:** `/` (Displays job postings)
- **Job Details:** `/job/<slug>` (Displays job details)
- **Subscribe:** `/subscribe/` (Subscription form)
- **Thank You:** `/thank_you/` (Subscription confirmation)

## Contributing

1. **Fork the repository** and create your branch:
   ```sh
   git checkout -b feature/your-feature
   ```

2. **Commit your changes**:
   ```sh
   git commit -m 'Add your feature'
   ```

3. **Push to the branch**:
   ```sh
   git push origin feature/your-feature
   ```

4. **Open a Pull Request**


