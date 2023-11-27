<?php
//ejercicio 5
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
// Verificar si el usuario está autenticado
if(isset($_SESSION['usuario_id'])) {
    echo "<p>Bienvenido, Usuario</p>";
    echo "<a href='logout.php'>Cerrar sesión</a>";
} else {
    echo "<p>¡Hola, invitado! Por favor, <a href='login.html'>inicia sesión</a></p>";
}

if (!isset($_GET['id'])) {
    die('No se ha especificado una película');
}

$id = $_GET['id'];
$query = 'SELECT * FROM tPeliculas WHERE id=' . $id;
$result = mysqli_query($db, $query) or die('Query error');
$only_row = mysqli_fetch_array($result);
echo '<img src=' . $only_row['url_imagen'] . '></img>';
echo '<h1>' . $only_row['autor'] . '</h1>';
echo '<h2>' . $only_row['genero'] . '</h2>';
?>
<h3>Comentarios:</h3>
<ul>
    <?php
    $query2 = 'SELECT * FROM tComentarios WHERE id=' . $id;
    $result2 = mysqli_query($db, $query2) or die('Query error');
    while ($row = mysqli_fetch_array($result2)) {
        echo '<li>';
             echo '<p>' . $row['comentario'] . ' - ' . $row['FechaComentario'] . date('Y-m-d', time()) >
        echo '</li>';
    }
    mysqli_close($db);
    ?>
</ul>
<form action="/comment.php" method="post">
        <textarea rows="6" cols="50" name="new_comment"></textarea><br>
        <input type="hidden" name="id" value="<?php echo $id; ?>">
        <input type="hidden" name="fecha" value="<?php echo date('y-m-d', time()); ?>"> 
       <input type="submit" value="Comentar">
    </form>
</body>
</html>

