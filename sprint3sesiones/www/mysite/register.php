<?php
// Conectar a la base de  datos
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "mysitedb";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error de conexión a la base de datos: " . $conn->connect_error);
}

// Obtener datos del formulario
$name = $_POST['name'];
$surname = $_POST['surname'];
$email = $_POST['email'];
$password = $_POST['password'];
$confirm_password = $_POST['confirm_password'];

// Validar que las contraseñas coinciden
if ($password !== $confirm_password) {
    die("Error: Las contraseñas no coinciden. <a href='register.html'>Volver al formulario</a>");
}

// Verificar si el correo ya existe en la tabla tUsuarios
$sql = "SELECT * FROM tUsuarios WHERE email = '$email'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    die("Error: El correo ya está registrado. <a href='register.html'>Volver al formulario</a>");
}

// Cifrar la contraseña
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Insertar el nuevo usuario en la tabla tUsuarios
$insert_sql = "INSERT INTO tUsuarios (nombre, apellidos, email, password) VALUES ('$name', '$surname', '$email', '$hashed_password')";

if ($conn->query($insert_sql) === TRUE) {
    echo "Registro exitoso. <a href='login.html'>Iniciar sesión</a>";
} else {
    echo "Error: " . $insert_sql . "<br>" . $conn->error;
}

// Cerrar la conexión a la base de datos
$conn->close();
?>

