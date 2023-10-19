<?php
  $db = mysqli_connect("localhost", "root", "1234", "mysitedb") or die ("Fail");
?>
<html>
 <body>
   <h1>Conexión establecida</h1>
   <?php
	//LANZAR UNA QUERY
	$query = "SELECT * FROM tPeliculas";
	$result = mysqli_query($db, $query) or die ("Query");
	//RECORRER EL RESULTADO
	while($row = mysqli_fetch_array($result)){
	echo $row["nombre"];
	echo "<br>;
	echo $row[2]";
	echo "<br>";
}
mysqli_close($db);
   ?>
 </body>
</html>

