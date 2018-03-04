<?php
$xmlDoc = new DOMDocument();
$xmlDoc->load("test.svg");

$x = $xmlDoc->documentElement;
foreach ($x->childNodes AS $item) {
  print $item->nodeName . " = " . $item->nodeValue . "<br>";
}
?>
