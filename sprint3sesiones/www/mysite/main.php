<!DOCTYPE html>
<html>
<head>
    <title>Título de tu página</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        h1 {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
        h2 {
            color: #0074D9; /* Color azul */
            font-size: 24px;
            margin-top: 10px;
        }
        img {
            max-width: 100%;
            height: auto;
            margin-top: 10px;
        }
        a {
            text-decoration: none;
            color: #FF5733; /* Color naranja */
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        hr {
            border: 1px solid #ddd;
            margin: 20px 0;
        }
    </style>
</head>
<body>

<?php
$db = mysqli_connect("localhost", "root", "1234", "mysitedb") or die("Fallo en la conexión");

if ($db) {
    // La conexión se estableció correctamente
    echo "<h1>Conexión establecida</h1>";

    // LANZAR UNA QUERY
    $query = "SELECT * FROM tPeliculas";
    $result = mysqli_query($db, $query) or die("Error en la consulta");

    // RECORRER EL RESULTADO
    while ($row = mysqli_fetch_array($result)) {
        echo "<div class='container'>"; // Contenedor para mejorar la apariencia
        echo "<h2>{$row['nombre']}</h2>";

        // Obtener la ruta de las imágenes relacionadas con la película
        $queryImagenes = "SELECT url_imagen FROM tPeliculas WHERE id = " . $row['id'];
        $resultImagenes = mysqli_query($db, $queryImagenes);

        // Muestra la imagen correspondiente a la película
        while ($rowImagen = mysqli_fetch_array($resultImagenes)) {
            $imagePath = "/home/pra/compartido/imgPhpSql/" . $rowImagen["url_imagen"];
             echo '<img src="'.$row[2].'" alt="Imagen de la película"/>';
            echo "<br>";
            echo $row[3];
            echo "<br>";
            echo $row[4];
            echo "<br>";
        }

        $id = $row["id"];
        echo "<a href='detail.php?id={$row['id']}'>Detalles</a>";
        echo "<hr>";
        echo "</div>"; // Cierre del contenedor
    }

    mysqli_close($db);

    echo "</body></html>";
} else {
    echo "No se pudo conectar a la base de datos.";
}
?>

</body>
</html>
