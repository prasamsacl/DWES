<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
 <body>
<?php
//ejercico 4
//se usa para  crear una sesión nueva
session_start();
$user_id_a_insertar = 'NULL';
if (!empty($_SESSION['user_id'])) {
$user_id_a_insertar = $_SESSION['user_id'];
}
  $id = $_POST['id'];
 $comentario = $_POST['new_comment'];
 $query = "INSERT INTO tComentarios(comentario, usuario_id,pelicula_id) VALUES ('".$comentario."',NULL,".$id.",".$user_id_a_insertar.")";
   mysqli_query($db, $query) or die('Error');
 echo "<p>Nuevo comentario ";
 echo mysqli_insert_id($db);
 echo " añadido</p>";

 echo "<a href='/detail.php?id=".$id."'>Volver</a>";
 mysqli_close($db);
 ?>
</body>
</html>
