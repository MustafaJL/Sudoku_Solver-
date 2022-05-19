<?php

$servername= "localhost";
$db_name= "python_project";
$username = "root";
$password = "";


$conn = mysqli_connect($servername, $username, $password, $db_name);

if(!$conn){
    echo "Not connected";
}



?>