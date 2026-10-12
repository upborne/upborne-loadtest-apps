<?php
// One write and one read, as a page view with a counter would do.
$db = new mysqli(getenv('WORDPRESS_DB_HOST'), getenv('WORDPRESS_DB_USER'), getenv('WORDPRESS_DB_PASSWORD'), getenv('WORDPRESS_DB_NAME'));
$db->query("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)");
$db->query("INSERT INTO visits () VALUES ()");
header('Content-Type: application/json');
echo json_encode(['n' => (int) $db->query("SELECT count(*) FROM visits")->fetch_row()[0]]);
