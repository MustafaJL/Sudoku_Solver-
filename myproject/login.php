<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/login1.css">
     <title>Login</title>
</head>
<body>
    <center><p>Please Login to use this application</p></center>
    <div class="login-box">
        <h2>Login</h2>
        <form action="login.php" method="post">
          <div class="user-box">
            <input type="text" name="Email" required="">
            <label>Username</label>
          </div>
          <div class="user-box">
            <input type="password" name="Password" required="">
            <label>Password</label>
          </div>
          <a href="#">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <input class="btn" value="Login" type="submit">
          </a>
          <br><br>
        <center><span id="alert" style="display: none; color:#FF0000">Incorrect Password or Username</span></center>
        </form>
      </div>
</body>
</html>
<?php

session_start();

include('connection.php');


$email = isset($_POST['Email']) ? $_POST['Email'] : "";
$password = isset($_POST['Password']) ? $_POST['Password'] : "";


if($username != "" && $password  != ""){

    $query = 'SELECT * FROM user WHERE email=?';

    $stmt = $conn->prepare($query);

    $stmt->bind_param('s', $email);

    $stmt->execute();


    $row = $stmt->get_result();

    $user = $row->fetch_assoc();
    if($user){

        if($password==$user["password"]){

            print_r($user['Password']);
            print_r($password);

            $_SESSION['Email'] = $user['Email'];
            header('Location: ./html/index.html');
            exit();
            
        }
        else{
            echo '<script>document.getElementById("alert").style.display = "block"</script>';
        }
        
    }
    else{
        echo '<script>document.getElementById("alert").style.display = "block"</script>';
    }
    
}

?>