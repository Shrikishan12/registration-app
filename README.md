# AWS Load-Balanced Registration Application with Auto Scaling and DynamoDB

This project demonstrates a production-style AWS architecture for a web-based registration application. The application is deployed on EC2 instances behind an Application Load Balancer, uses Auto Scaling for high availability, and stores user registration data securely in Amazon DynamoDB. DNS routing is handled using Amazon Route 53.

---

## Architecture

User  
→ Route 53 (Custom Domain)  
→ Application Load Balancer (HTTPS)  
→ Auto Scaling Group  
→ EC2 (Flask Application)  
→ DynamoDB

---

## AWS Services Used

- Amazon EC2  
- Application Load Balancer  
- Auto Scaling Group  
- Amazon DynamoDB  
- Amazon Route 53  
- AWS IAM  

---

## Application Stack

- Frontend: HTML, CSS  
- Backend: Python (Flask)  
- Web Server: Gunicorn  
- Database: DynamoDB  
- Operating System: Amazon Linux 2  

---

## Folder Structure

```

registration-app/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html

app.py: Flask backend logic
templates/: HTML templates
requirements.txt: Python dependencies

```

---

## Application Workflow

1. User accesses the application using a custom domain.
2. Route 53 routes traffic to the Application Load Balancer.
3. The Load Balancer distributes requests across EC2 instances in the Auto Scaling Group.
4. The Flask application processes the registration request.
5. User data is stored in Amazon DynamoDB.
6. A success response is returned to the user.

---

## Database Design

**DynamoDB Table**
- Table Name: `registration-table`
- Partition Key: `email` (String)

The application is stateless, and DynamoDB is used for scalability and high availability.

---

## Security Implementation

- IAM Role attached to EC2 for DynamoDB access
- No hard-coded AWS credentials
- Application Load Balancer as the only public entry point

---

## Auto Scaling Configuration

- Minimum instances: 2  
- Desired instances: 2  
- Maximum instances: 4  
- Scaling based on CPU utilization  

This ensures high availability and automatic recovery.

---

## Deployment Details

EC2 instances are launched using a Launch Template with a user-data script.  
This script bootstraps each instance automatically at launch.

### Instance Bootstrapping

The user-data script performs the following actions:
- Installs required system packages
- Clones the GitHub repository
- Installs Python dependencies
- Starts the Flask application using Gunicorn in the background

```bash
#!/bin/bash

# Update system
yum update -y

# Install required packages
yum install -y python3 python3-pip git

# Upgrade pip
python3 -m pip install --upgrade pip

# Clone application repository
cd /home/ec2-user
git clone https://github.com/Shrikishan12/registration-app.git
cd registration-app

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Run application using Gunicorn
nohup gunicorn -b 0.0.0.0:5000 app:app &
```

---

## Outcome

This project demonstrates real-world AWS deployment practices including load balancing, auto scaling, secure IAM usage, DNS routing, HTTPS configuration, and NoSQL database integration.

---

## Future Enhancements

- Add AWS WAF
- Enable CloudWatch logging and alarms
- Convert Gunicorn process to systemd service
- Implement CI/CD pipeline
