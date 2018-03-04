<?php
$output = shell_exec('python svg_to_json.py test.svg');
echo "<pre>$output</pre>";
?>
