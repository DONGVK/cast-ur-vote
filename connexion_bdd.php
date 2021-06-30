<?php
   try{
      $pdo=new PDO("mysql:host=localhost;dbname=sf",);
   }
   catch(PDOException $e){
      echo $e->getMessage();
   }

   
?>