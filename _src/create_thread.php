<?php
session_start();
include 'db_connect.php'; // Include database connection

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $title = $_POST['title'];
    $user_id = $_SESSION['user_id']; // Assuming the user is logged in

    $sql = "INSERT INTO threads (title, user_id) VALUES ('$title', '$user_id')";
    if (mysqli_query($conn, $sql)) {
        echo "New thread created successfully!";
    } else {
        echo "Error: " . mysqli_error($conn);
    }
}
?>

<form action="create_thread.php" method="POST">
    <input type="text" name="title" placeholder="Thread Title" required>
    <button type="submit">Create Thread</button>
</form>
