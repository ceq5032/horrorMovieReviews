<?php
session_start();
include 'db_connect.php'; // Include database connection

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $content = $_POST['content'];
    $user_id = $_SESSION['user_id']; // Assuming the user is logged in
    $thread_id = $_POST['thread_id'];

    $sql = "INSERT INTO posts (content, thread_id, user_id) VALUES ('$content', '$thread_id', '$user_id')";
    if (mysqli_query($conn, $sql)) {
        echo "Reply posted successfully!";
    } else {
        echo "Error: " . mysqli_error($conn);
    }
}
?>

<form action="post_reply.php" method="POST">
    <textarea name="content" placeholder="Your reply..." required></textarea>
    <input type="hidden" name="thread_id" value="THREAD_ID_HERE"> <!-- Replace with thread ID -->
    <button type="submit">Post Reply</button>
</form>
