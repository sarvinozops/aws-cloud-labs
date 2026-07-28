#!/bin/bash

# Update packages and install Apache with PHP
dnf update -y
dnf install -y httpd php php-fpm php-mysqli

# Enable and start Apache
systemctl enable httpd
systemctl start httpd

# Create a simple test page
cat > /var/www/html/index.html <<'HTML'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AWS VPC Lab</title>
</head>
<body>
    <h1>AWS VPC Networking Lab</h1>
    <p>Apache web server is running successfully.</p>
</body>
</html>
HTML
