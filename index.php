<?php
    
    $svg = new SimpleXMLElement( file_get_contents( 'test-svg.xml' )  );
    
    $results = $svg;
    //echo "<pre>".print_r($results)."<pre>";


    // header("Content-type: application/json");
    // echo json_encode($result);
    // die;


    function print_array($arr) {
        foreach($arr as $r) {
            if (is_array($r)) {
                print_array($r);
            }
            else {
                print_r($r);
                echo "<br><br><br>";
            }
        }
    }
?>
