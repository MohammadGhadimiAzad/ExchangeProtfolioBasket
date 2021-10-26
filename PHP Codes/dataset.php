<?php
include 'brands.php';
include 'dbconf.php';

//For next index from Cron Jobs
$sql = "SELECT i FROM counter";
$result = $conn->query($sql);

exit(0);

$i = 0;

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $i = $row["i"];
  }
} else {
  echo "-1";
}

/* *********************** */

if ($i<=count($brands))
{
    /*
    //Insert by json data
    $path = 'https://ghadimiazad.ir/arshad/files/'.$url_brands[$i].'.json';
    $data = file_get_contents(utf8_encode($path));
    $jsondata = json_decode($data)->list;
    */
    
    //Insert by download data from fipiran website
    $url = "https://www.fipiran.com/Symbol/HistoryPricePaging?symbolpara=".($url_brands[$i])."&rows=3000&page=1&sidx=DEven&sord=desc";
    $data = file_get_contents($url);
    $json = json_decode($data)->data;
    $res_data = array();
    $others = array();
    foreach ($json as $v) {
        $date = $v->gDate;
        $timestamp = strtotime($date);
        $v->date = date('Y-m-d', $timestamp);
        array_push($jsondata, $v);
    }
    // print_r($jsondata);

    foreach ($jsondata as $v) {
        $sql = "INSERT INTO `dataset`(`gDate`, `DEven`, `ZTotTran`, `QTotTran5J`, `QTotCap`, `PClosing`, `PcCh`, `PcChPercent`, `PDrCotVal`, `LTPCh`, `LTPChPercent`, `PriceYesterday`, `PriceMin`, `PriceMax`, `PriceFirst`, `date`, `Brand`)
        VALUES ('$v->gDate','$v->DEven','$v->ZTotTran','$v->QTotTran5J','$v->QTotCap','$v->PClosing','$v->PcCh','$v->PcChPercent','$v->PDrCotVal','$v->LTPCh','$v->LTPChPercent','$v->PriceYesterday','$v->PriceMin','$v->PriceMax','$v->PriceFirst','$v->date','$brands[$i]')";
        
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully<br/>";
        } else {
            echo "Error ...";
        }
    }

    $i++;
    $sql = "UPDATE `counter` SET `i`=$i";
    $conn->query($sql);
    $conn->close();
}
