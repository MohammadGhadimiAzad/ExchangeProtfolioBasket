<?php
$servername = "localhost";
$username = "cp32823_arshadproject";
$password = 'V^3n}PyrM+}$';
$dbname = "cp32823_arshadproject";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
mysqli_set_charset($conn,"utf8");

