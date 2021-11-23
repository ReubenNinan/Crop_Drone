<?php

$user - 'admin';
$password = 'team77_2021';
$db = 'cropdone';
$host = "cropdrone.cp1xd7eoed6m.us-east-2.rds.amazonaws.com";
$port = 3306;

$link = mysqli_init();
$success - mysql_real_connect
(
    $link, 
    $host, 
    $user, 
    $password, 
    $db, 
    $port
);