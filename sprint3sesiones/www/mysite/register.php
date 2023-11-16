<?php
// Conectar a la base de datos
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

// Obtener datos del formulario
$name = $_POST['name'];
$surname = $_POST['surname'];
$email = $_POST['email'];
$password = $_POST['password'];
$confirm_password = $_POST['confirm_password'];

// Validar que las contraseñas coincidan
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

// Verificar la inserción de datos
if ($conn->query($insert_sql) === TRUE) {
    echo "Registro exitoso. <a href='login.html'>Iniciar sesión</a>";

    // Puedes agregar aquí el formulario de inicio de sesión o un enlace al formulario de inicio de sesión
    echo '<br><a href="login.html">Ir al formulario de inicio de sesión</a>';
} else {
    echo "Error al insertar datos: " . $conn->error;
}

// Cerrar la conexión a la base de datos
$conn->close();
?>


